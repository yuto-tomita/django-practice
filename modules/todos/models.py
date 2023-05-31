from django.db import models
from users.models import User
from django.utils import timezone

# django では `primary_key=True` を設定しない場合、自動的に主キーを設定するための IntegerField を追加する
# https://docs.djangoproject.com/ja/4.2/topics/db/models/#automatic-primary-key-fields
class Todo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
  title = models.CharField(max_length=200)
  description = models.CharField(default="")
  date = models.DateField(default=timezone.now)
  created_at = models.DateTimeField(default=timezone.now)
  
  STATUS = [
    ("todo", "未着手"),
    ("in_progress", "進行中"),
    ("completed", "完了")
  ]
  status = models.CharField(max_length=20, choices=STATUS, default="todo")
