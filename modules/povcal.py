import numpy as np
import urllib
from google.appengine.api import urlfetch


def constructor(country, povline, proportion=True):

    base = "http://iresearch.worldbank.org/PovcalNet/PovcalNetAPI.ashx"
    yearlist = ','.join([str(x) for x in np.arange(1970, 2018)])

    payload = {
        "Y0": yearlist,
        "PL0": povline,
        "C0": country + "_3",
        "GroupedBy": "false"
    }

    url = base + "?" + urllib.urlencode(payload)
    data = urlfetch.fetch(url=url).content.split("\n")
    header, items = data[0], data[1:]

    header = [x.strip("'") for x in header.split("\t")]

    res = []
    for xx in [i.split("\t") for i in items]:
        values = [x.strip("'") for x in xx]
        d = dict(zip(header, values))
        try:
            pop = int(float(d["ReqYearPopulation"])*1000000)
            res += [{
                "year": int(d["RequestYear"]),
                "population": pop,
                "impoverished": int(pop*float(d["HeadCount"]))
            }]

        except Exception:
            pass

    return dict(
        country=country,
        count=len(res),
        results=res,
        poverty_line=povline
    )
