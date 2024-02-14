from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View define application logic extending a base class APIView"""
    serializer_class = serializers.HelloSerializer
     

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

        return Response({'messagge': 'Hello ', 'an_apiview': an_apiview  })
    
    def post(self, request):
        """Create a Hello Message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})