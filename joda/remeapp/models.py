
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# class User(AbstractUser):
#   tel = models.CharField("Телефон", max_length=15, blank=True, null=True)

class Cells(models.Model):
  content = models.TextField(blank=True, verbose_name="Контент")
  time_create = models.DateTimeField(auto_now_add=True)
  time_update = models.DateTimeField(auto_now=True)
  tags = models.ManyToManyField('Tags')
  user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
  # print(User.objects.get(pk=2), 11111111111111111111111)
  
  def set_cell_tags(self, tags, user_id):
    set_tags_list = []  
    if tags:
      for tag in tags:
        tag_new, bol = Tags.objects.get_or_create(name=tag, user_id=user_id)
        print(tag_new, bol, 'tag_new, bol')
        set_tags_list.append(tag_new)
      self.tags.set(set_tags_list)
    return self

  # def __str__(self):
  #   return self.content

class Tags(models.Model):
  name = models.TextField(blank=True, verbose_name="Имя")
  time_create = models.DateTimeField(auto_now_add=True)  
  user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
  
  # print(cells, 'cells ------------------11111111')
  def __str__(self):
    return self.name

# class Ids_cells_tags(models.Model):
#   t_id = models.ManyToManyField(Tags)