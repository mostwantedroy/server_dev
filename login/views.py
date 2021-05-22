from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password

class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id = user_id).first()

        if not user:
            return Response(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공"))
        else:
            return Response(dict(msg="비밀번호가 틀렸습니다."))


class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_pw_encrypted = make_password(user_pw)

        # user_id에 대한 검증 로직이 들어감.
        #

        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is not None:
            return Response(dict(msg="동일한 아이디가 있습니다."))

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encrypted)

        data = dict(
            user_id=user_id,
            user_pw=user_pw_encrypted
        )

        return Response(data)

