from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import loginUser

class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")

        loginUser.objects.create(user_id=user_id, user_pw=user_pw)

        data = dict(
            user_id=user_id,
            user_pw=user_pw
        )

        return Response(data=data)

