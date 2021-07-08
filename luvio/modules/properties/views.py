from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class PropertyList(APIView):
    """
    [Return list of properties]
    """
    def post(self, request, format=None):
        # Parse request body to get a list of searched suburbs
        suburbs = request.data["suburbs"]
        print(suburbs)
        # Send GET request to Domain website to get a list of result listings
        # Convert listings to list of property ids
        # Call Domain API using those ids
        # Return the list of listings
        return Response("Hello world")