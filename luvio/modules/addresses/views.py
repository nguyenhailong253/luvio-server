from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class AddressList(APIView):
    """
    [Return list of suggested address]
    """
    def post(self, request, format=None):
        # Parse request body to get a list of searched suburbs
        req_body = request.data
        print(req_body)
        # Send GET request to Domain website to get a list of result listings
        # Convert listings to list of property ids
        # Call Domain API using those ids
        # Return the list of listings
        return Response("Addresses")