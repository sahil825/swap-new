from django.shortcuts import render
from rest_framework import request, views
from .models import swapkit
from django.contrib.auth.models import Permission, User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import filters
from django.conf import UserSettingsHolder
from rest_framework import response
from rest_framework.views import APIView
from django.contrib.auth import authenticate , login
from .helper import *
from blog.home.helper import generate_random_string
from .models import Profile


class swapkit(viewsets.modelsViewSet):
    def post(self, request):
        request = request.swapkit()
        serializer_class = requestSerializer
        permission_classes = [
        permission.isUser, Permission.isAunthenticationOrGetonly]
    filter_backends = [filters.searchFilter]

    try:
        data = request.data

        if data.get('request') is True:
            Response['massage'] = 'random string number'
            
        if not Profile.objects.filter(user = check_user).first().is_verified:
            response['massage'] = 'your Profile is not verified'
            raise Exception('profile not verified')

            user_obj = authenticate(Username = data.get('username'))
        if user_obj:
            response['status'] = '200'
            response('massage') = 'welcome'
        else:
            response['massage'] = 'invalid password'
            raise Exception('ivalid password')
        
        except Exception as e:
            print(e)

        return Response(response)
