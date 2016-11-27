'''
Request Handler for API Gateway server
Handles the client request from the Gateway and reroutes it to the
appropriate service, collecting the data and sending it back to the client
'''
import requests
import web


class RequestHandler:
    '''
    Request Handling facilities to handle GET and POST request
    '''

    API_URLS = {
        'auth': 'auth_service',
        'auth/check': 'auth_service',
        'news': 'news_service',
        'logout': 'logout_service',
        'profile': 'profile_service'
    }

    def GET(self, name):
        '''
        GET request handler
        '''

        if name in self.API_URLS:
            location = web.service_reg.get_service_details(self.API_URLS[name])
            print web.input()
            api_path = location[0] + ':' + str(location[1]) + '/' + name
            req = requests.get(api_path)
            return req.text
        else:
            print "Service not found"

    def POST(self, name):
        '''
        POST Request handler
        '''

        if name in self.API_URLS:
            location = web.service_reg.get_service_details(self.API_URLS[name])
            api_path = location[0] + ':' + str(location[1]) + '/' + name
            print dict(web.input())
            req = requests.post(api_path, json = dict(web.input()))
            return req.text
        else:
            print "Service not found"
