This project is meant to serve as the coorindating layer for data across the GPSDD's partners, numbering in the hundreds.  The service runs on [Google App Engine](https://cloud.google.com/appengine/docs) and provides a set of standardized REST endpoints for data that report on the Sustainable Development Goals (SDGs).  

The documentation for each endpoint is in the Wiki.  A current list of available resources is compiled here:

1. PovcalNet

### Developing

Any help is greatly appreciated.  First, fork the repository.  Edit the code, add services, contribute at will.  To run the service locally, run `dev_appserver.py .` and navigate to `localhost:8080` with the appropriate structure and parameters.  For example, if .  Submit a pull request.  Core members will be able to push directly to App Engine for the live service, once the version in `app.yaml` is appropriately set.  You will need to request authority to push directly from [danhammer](https://github.com/danhammer).  The command to push to App Engine follows.

```bash
appcfg.py update --oauth2 .
```

The production APIs will be available at `https://gpsdd-service.appspot.com` and evenutally at `https://api.data4sdgs.org/vX`.


### The value proposition and the role of the GPSDD

