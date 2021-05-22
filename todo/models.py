from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user_id = models.CharField(max_length = 20, null = False, default = False)
    name = models.CharField(max_length = 256, null = False, default = '', verbose_name = "작업이름")
    start_date = models.DateField(default = timezone.now, verbose_name = "시작날짜")
    end_date = models.DateField(null = True, verbose_name = "마감날짜")
    finish_date = models.DateField(null = True, verbose_name = "완료날짜")
    state = models.IntegerField(null = False, default = 0, verbose_name = "상태")

    class Meta:
        db_table = 'task'
        verbose_name = '작업(to-do) 테이블'