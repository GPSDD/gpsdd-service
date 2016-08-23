This project is meant to serve as the coorindating layer for data across the GPSDD's partners, numbering in the hundreds.  The service runs on [Google App Engine](https://cloud.google.com/appengine/docs) and provides a set of standardized REST endpoints for data that report on the Sustainable Development Goals (SDGs).  

The documentation for each endpoint is in the [Wiki](https://github.com/GPSDD/gpsdd-service/wiki).  A current list of available resources is compiled here:

1. [PovcalNet](https://github.com/GPSDD/gpsdd-service/wiki/PovcalNet)
2. [Forest Clearing Alerts](https://github.com/GPSDD/gpsdd-service/wiki/Forest-Clearing-Alerts)

### Developing

Any help is greatly appreciated.  The proposed workflow follows:

- Fork the repository.
- Download and install the [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads).  This will include the [Python Development Server](https://cloud.google.com/appengine/docs/python/tools/devserver), launched using the `dev_appserver.py` script (which will be appropriately placed on your Path during install).
- Edit the code, add features, add tests, whatever.  Test the service locally by running `dev_appserver.py .` from within the `gpsdd-service` directory (at the same level as `app.yaml`).  The default local server will run at `localhost:8080`.  So, for example, if you are working with the [PovcalNet](https://github.com/GPSDD/gpsdd-service/wiki/PovcalNet) service, you would navigate to
```bash
http://localhost:8080/povcal?country=AUS&povline=1.9
```
```json
{
    "count": 8, 
    "results": [
        {"impoverished": 149272, "year": 1981, "population": 14927000}, 
        {"impoverished": 157736, "year": 1985, "population": 15758000}, 
        {"impoverished": 113668, "year": 1989, "population": 16814400}, 
        {"impoverished": 242504, "year": 1995, "population": 18072000}, 
        {"impoverished": 261296, "year": 2001, "population": 19413000}, 
        {"impoverished": 269977, "year": 2003, "population": 19895400}, 
        {"impoverished": 141725, "year": 2008, "population": 21249200}, 
        {"impoverished": 147825, "year": 2010, "population": 22031800}
    ], 
    "poverty_line": 1.9, 
    "country": "AUS"
}
```
- Submit a pull request.  The repo administrators will test the new service, run it against our [TravisCI](https://travis-ci.org/) tests. If it passes muster, the administrators will push directly to App Engines production servers.    The command to push to App Engine follows.

```bash
appcfg.py update --oauth2 .
```

- The production APIs will be available at `https://gpsdd-service.appspot.com` and evenutally at `https://api.data4sdgs.org/vX`. You will need to request authority to push directly from [danhammer](https://github.com/danhammer).

### The value proposition and the role of the GPSDD

Business Insider published a list of "53 startups that will be huge in 2016, according to venture capitalists.""  The list included enterprise and consumer apps that ranged from men's fashion to big data.  Notably, five of the startups organized data for third-party developers.  The startup Segment, for example, provisions "a single place that collects all customer data that can then be used by many other apps."  Segment received $44.7 million over 4 rounds from 7 different investors.   There are dozens of other companies, like Quandl, Enigma.io, and DataSift, that have raised a similar amount for similar infrastructure to do similar things.  None have built this data infrastructure for environmental or social information, mainly because the returns (natural and financial) cannot be entirely captured by investors.  The venture market clearly believes that companies building data infrastructure are driving the digital economy.   The non-market, social benefits suggest that only an organization like **the Global Partnership for Sustainable Development Data (GPSDD) is uniquely positioned to provision this global data infrastructure for the SDGs**. 

Open, structured access to data on sustainable development and specifically the Sustainable Development Goals (SDGs) is a public good.  The investment in the infrastructure is localized, but the benefits are broad and distributed.  Public goods are the domain of the public or social sector, even if most of the work is done by the private sector.  There is a level of trust and camaraderie that can only be achieved by a convening organization with the public good as *the* first-order consideration.  The Global Partnership has been appointed to be this convening group, with the **primary objective of elevating the work of both public- and private-sector Partners**.

[Quandl](https://www.quandl.com) has a useful and simple graphic (below) to describe the type of interaction we are building for data to monitor SDGs.  The data reside on the servers of our Partners, and GPSDD provisions structured, stable endpoints to harmonize the data (along with a few select client libraries).  A reasonable question is, "how can the GPSDD replicate the work of a tech startup with hundreds of millions of dollars in funding?"  The GPSDD benefits from the generous resources and time granted by the Partners.  Companies and multinational organizations like Esri, the World Bank, Nielsen, and many others have contributed a significant amount of information and tech resources to stabilize their data streams.  This project merely hopes to collate the broad and powerful effort to better monitor the SDGs for global good.

![](http://s22.postimg.org/xeqhiqbjl/Screen_Shot_2016_03_31_at_1_42_19_PM.png)

If you represent a company that is interested in becoming a partner, please visit the [GPSDD website](https://www.data4sdgs.org) and submit a [Champion Application Commitment Form](https://www.surveymonkey.com/r/GPCommitmentForm). The current class of Champions number in the hundreds and have made significant committments to this collaborative effort.

### History of the GPSDD

On September 27th 2015, **193 world leaders** committed to **17 Global Goals** to achieve **3 extraordinary things** in the next **15 years**. *End extreme poverty. Fight inequality & injustice. Fix climate change.* 

To reach these **Sustainable Development Goals** (The SDGs), we will need to confront a crisis at the heart of solving many of the world’s most pressing issues—a crisis of poor use, accessibility, and production of high quality data that is stunting the fight to overcome global challenges in every area—from health to gender equality, human rights to economics, and education to agriculture. The availability and access to high quality data is essential to measuring and achieving the Sustainable Development Goals.

On September 28th, 2015, The **Global Partnership for Sustainable Development Data** officially launched.

We are an unprecedented, multi-stakeholder group consisting of governments, civil society, private sector, international organizations, academic, statistical and data communities, and networks who represent all sectors of society, dedicated to achieving the Sustainable Development Goals by 2030.
