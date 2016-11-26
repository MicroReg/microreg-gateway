'''
Microreg API Gateway interface
Utilizes MicroReg to reroute calls
'''
from api.MicroReg import MicroRegClient
from RequestHandler import RequestHandler
import web


class Server:
    '''
    Run the API Gateway server using the web.py library and reroute to the
    requests to the correct MicroService
    '''

    def __init__(self, host, port):
        '''
        Initialize the server and set the connecting points
        '''

        self.__web_urls = (
            '/(.*)', 'RequestHandler'
        )
        web.service_reg = MicroRegClient(host, port)
        self.__web_server = web.application(self.__web_urls, globals())

    def start_server(self):
        '''
        Start the webserver
        '''

        self.__web_server.run()
