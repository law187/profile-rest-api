from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """docstring for ."""

    def get(self, request, format=None):
        an_apiview = ['get, post ,patch ,update , delete : this is  lsit of apiviews' ]
        return Response({'an_apiview':an_apiview})
