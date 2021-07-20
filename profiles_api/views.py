from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets

from profiles_api import serializers

from profiles_api import models

from profiles_api import permissions

from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings




class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        an_apiview = ['get, post ,patch ,update , delete : this is  lsit of apiviews' ]
        return Response({'an_apiview':an_apiview})




    def post(self, request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response({'message':message})

        else :
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, PK=None):

        return Response({'method' : 'PUT'})



    def patch(self,request, PK=None):

        return Response({'method' : 'PATCH'})


    def delete(self,request, PK=None):

        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

        serializer_class = serializers.HelloSerializer


        def list(self, request):

            a_viewsets = ['list, create , retrive, update, partial_update']

            return Response({'message':'hello', 'a_viewsets':a_viewsets})


        def create(self, request):
              serializer =self.serializer_class(data=request.data)
              if serializer.is_valid():
                    name = serializer.validated_data.get('name')
                    message = f'hello{name}'
                    return Response({'message':message})
              else:
                 return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def retrive(slef, request, pk=None):
            return Response({'method_http':'GET'})

        def update(self, request, pk=None):
            return Response({'method_http':'PUT'})

        def partial_update(self, request, pk=None):
            return Response({'method_http':'PATCH'})

        def destroy(self, request, pk=None):
            return Response({'method_http':'DELETE'})



class UseerProfileViewSet(viewsets.ModelViewSet):

        serializer_class = serializers.UserProfileSerializer
        queryset = models.UserProfile.objects.all()
        authentication_classes = (TokenAuthentication,)
        permission_classes = (permissions.updateOwnProfile,)
        filter_backends = (filters.SearchFilter,)
        search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
