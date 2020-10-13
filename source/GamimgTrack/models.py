from django.db import models

# Create your models here.

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
