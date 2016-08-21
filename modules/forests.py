import urllib
import json
from google.appengine.api import urlfetch


def constructor(country, begin, end):
    # Scrape and restructure the FORMA data from the GFW API

    base = "http://api.globalforestwatch.org/forest-change/forma-alerts/admin"
    base_country = base + "/" + country

    # Define payload.
    payload = {
        "period": begin + "," + end
    }

    url = base_country + "?" + urllib.urlencode(payload)
    data = json.loads(urlfetch.fetch(url=url).content)

    return dict(
        country=country,
        deforestation=data['value'],
        meta=data['meta'],
        download_url=data['download_urls']['csv']
    )
