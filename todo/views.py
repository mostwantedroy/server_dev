from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from datetime import datetime

class TaskCreate(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        name = request.data.get('name', "")
        end_date = request.data.get('end_date', None)

        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        task = Task.objects.create(user_id=user_id, name=name, end_date=end_date)

        return Response(dict(msg="To-Do 생성 완료", name=task.name, start_date=task.start_date.strftime('%Y-%m-%d'), end_date=task.end_date))


class TaskSelect(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")

        tasks = Task.objects.filter(user_id=user_id)
        task_list = []

        for task in tasks:
            task_list.append(dict(name=task.name, start_date=task.start_date, end_date=task.end_date, state=task.state))

        return Response(dict(task=task_list))