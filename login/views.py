from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password
from .serializer import LoginUserSerializer

class AppLogin(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        user = LoginUser.objects.filter(user_id = user_id).first()

        if not user:
            return Response(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공", user_id = user.user_id, birth_day = user.birth_day,
                                 gender = user.gender, email = user.email, name = user.name, age = user.age))
        else:
            return Response(dict(msg="비밀번호가 틀렸습니다."))


class RegistUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(request.data)

        if LoginUser.objects.filter(user_id = serializer.data['user_id']).exists():
            user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()

            data = dict(
                msg="이미 존재하는 아이디입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw
            )

            return Response(data)

        user = serializer.create(request.data)

        return Response(data=LoginUserSerializer(user).data)


# class RegistUser(APIView):
#     def post(self, request):
#         user_id = request.data.get('user_id', "")
#         user_pw = request.data.get('user_pw', "")
#
#         birth_day = request.data.get('birth_day', None)
#         gender = request.data.get('gender', "male")
#         email = request.data.get('email', "")
#         name = request.data.get('name', "")
#         age = request.data.get('age', 20)
#         user_pw_encrypted = make_password(user_pw)
#
#         # user_id에 대한 검증 로직이 들어감.
#
#         if LoginUser.objects.filter(user_id=user_id).exists():
#             user = LoginUser.objects.filter(user_id=user_id).first()
#
#             data = dict(
#                 msg="이미 존재하는 아이디입니다.",
#                 user_id=user.user_id,
#                 user_pw=user.user_pw
#             )
#
#             return Response(data)
#
#         LoginUser.objects.create(user_id=user_id, user_pw=user_pw_encrypted)
#
#         data = dict(
#             user_id=user_id,
#             user_pw=user_pw_encrypted,
#             birth_day=birth_day,
#             gender=gender,
#             email=email,
#             name=name,
#             age=age
#         )
#
#         # 위와 같이 필드가 많아질 경우 Serializer를 통해 단순하게 만든다.
#         # data = Serialize(User)
#
#         return Response(data)
