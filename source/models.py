# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    email = models.TextField()
    password = models.TextField()
    login = models.TextField()
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='lastLogin', blank=True, null=True)  # Field name made lowercase.
    permissionlevel = models.IntegerField(db_column='permissionLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
