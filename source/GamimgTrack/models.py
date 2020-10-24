from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    email = models.TextField()
    password = models.TextField()
    login = models.TextField()
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='lastLogin', blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='permissionLevel', blank=True, null=True, default=1)  # Field name made lowercase.

"""
permissionlevel:
    1 = normal_user
    2 = ?
    3 = tutor
    4 = moderator
    5 = administrador
"""

class Postagem(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    content = models.TextField()
    title = models.TextField()
    creation_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    user_criador = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    
