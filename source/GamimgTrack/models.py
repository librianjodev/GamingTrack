import re

from django.db import models
from django.core import validators
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, permissionlevel, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(
            login=username,
            email=email,
            is_staff=is_staff,
            ##is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            creationdate=now,
            permissionlevel=permissionlevel,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email=None, password=None, **extra_fields):
        return self._create_user(login, email, password, False, False, 1, **extra_fields)

    def create_superuser(self, login, email, password, **extra_fields):
        user = self._create_user(login, email, password, True, True, 5, **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        _('Login'),
        max_length=25,
        unique=True,
        help_text=_('Requer 25 caracteres ou menos. Letras, números e caracteres especiais @/./+/-/_'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Entre com um login válido.'), _('Inválido'))]
    )
    nome = models.CharField(_('Nome completo'), max_length=255, null=True)
    email = models.EmailField(_('E-mail válido'), max_length=255, unique=True)
    photo = models.BinaryField(blank=True, null=True)
    password = models.CharField(_('Senha'), max_length=128)
    last_login = models.DateTimeField(
        _('Último login'),
        db_column='lastLogin',
        blank=True,
        null=True
    )
    creationdate = models.DateTimeField(
        _('Data de criação'),
        db_column='creationDate',
        auto_now_add=True
    )
    permissionlevel = models.IntegerField(
        _('Permissões: 1 = normal_user, 2 = ?, 3 = tutor, 4 = moderator, 5 = administrador'),
        db_column='permissionLevel',
        blank=True,
        null=True,
        default=1
    )
    is_staff = models.BooleanField(_('Status de equipe'), default=False, help_text=_('Define se é admin do site'))
    is_superuser = models.BooleanField(_('Superuser'), default=False)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email', 'nome']

    objects = UserManager()

    class Meta:
        unique_together = ['login', 'email']
        verbose_name = _('user')
        verbose_name_plural = _('users')


'''
class User(models.Model):
    id = models.AutoField(primary_key=True)
     nome = models.TextField(blank=True, null=True)
     photo = models.BinaryField(blank=True, null=True)
     email = models.TextField()
     password = models.TextField()
     login = models.TextField()
     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True,
                                        auto_now_add=True)  # Field name made lowercase.
     lastlogin = models.DateTimeField(db_column='lastLogin', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
     permissionlevel = models.IntegerField(db_column='permissionLevel', blank=True, null=True,
                                          default=1)  # Field name made lowercase.

    class Meta:
        unique_together = ['email', 'login']

    def __str__(self):
        return self.nome


"""
permissionlevel:
    1 = normal_user
    2 = ?
    3 = tutor
    4 = moderator
    5 = administrador
"""
'''


class Postagem(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    content = models.TextField()
    title = models.TextField()
    creation_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    user_criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class LikePostagens(models.Model):
    id = models.AutoField(primary_key=True)
    user_like = models.ForeignKey(User, on_delete=models.CASCADE)
    postagem_like = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __int__(self):
        return self.user_like


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    relative_image = models.BinaryField(blank=True, null=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=True, null=True)
    save_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['name', 'description']

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    content = models.TextField()
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    user_criador = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class ComentariosPostagens(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    comentario = models.TextField(default="")

class ComentariosReview(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comentario = models.TextField(default="")

class Amizade(models.Model):
    id = models.AutoField(primary_key=True)
    amigo = models.ForeignKey(User, related_name='amigo', on_delete=models.CASCADE)
    amigo2 = models.ForeignKey(User, related_name='amigo2', on_delete=models.CASCADE)
    class Meta:
        unique_together = ['amigo', 'amigo2']

class ConviteAmizade(models.Model):
    id = models.AutoField(primary_key=True)
    quem_enviou = models.ForeignKey(User, related_name='enviou',on_delete=models.CASCADE)
    quem_recebeu_o_pedido = models.ForeignKey(User, related_name='recebeu', on_delete=models.CASCADE)
    class Meta:
        unique_together = ['quem_enviou', 'quem_recebeu_o_pedido']