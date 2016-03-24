import json
import webapp2
from modules import povcal


class PovcalHandler(webapp2.RequestHandler):
    def get(self):

        # headers
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.headers['Content-Type'] = 'application/json'

        # parameters
        country = self.request.get('country')
        povline = float(self.request.get('povline'))
        proportion = bool(self.request.get('proportion', False))

        # response
        res = povcal.constructor(country, povline, proportion=proportion)
        self.response.write(json.dumps(res))


handlers = webapp2.WSGIApplication(
    [
        ('/povcal', PovcalHandler)
    ], debug=True
)
