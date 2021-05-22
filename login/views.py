from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password

class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        # user_id에 대한 검증 로직이 들어감.
        #

        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is not None:
            return Response(dict(msg="동일한 아이디가 있습니다."))

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw)

        data = dict(
            user_id=user_id,
            user_pw=user_pw
        )

        return Response(data)

