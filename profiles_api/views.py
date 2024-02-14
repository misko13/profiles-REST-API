from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View define application logic extending a base class APIView"""

    def get(self, request, format=None):
        """Returns a LIST of APIView Features - HTTP get requests"""    
        an_apiview =[
            'Uses HTTP method as fiunction (get, post, patch, put, delete)',
            'Is very similar as traditional Django View',
            'Gives You the most controll over you apploication logic',
            'Is mapped to URLs',
        ]
        """ This is a sample list, we look tyo get a response OBJECT converted to JSON  - it must be a list or a dictionary"""
        """We pass bellow the dictionary"""

        return Response({'messagge': 'Hello World', 'an_apiview': an_apiview  })