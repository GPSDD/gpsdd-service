import json
import webapp2
from modules import povcal
from modules import forests


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


class ForestHandler(webapp2.RequestHandler):
    def get(self):

        # headers
        self.response.headers.add_header("Access-Control-Allow-Origin", "*")
        self.response.headers['Content-Type'] = 'application/json'

        # parameters
        country = self.request.get('country')
        begin = self.request.get('begin')
        end = self.request.get('end')

        # response
        res = forests.constructor(country, begin, end)
        self.response.write(json.dumps(res))


handlers = webapp2.WSGIApplication(
    [
        ('/1/povcal', PovcalHandler),
        ('/15/forma', ForestHandler)
    ], debug=True
)
