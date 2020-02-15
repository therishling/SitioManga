from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Modelo usuario
class ManejadorUsuario(BaseUserManager):

    def create_user(self, correo, password = None):
        if not correo:
            raise ValueError('Usuarios deben tener un correo valido.')
        
        usuario = self.model(correo = self.normalize_email(correo), )
        usuario.set_password(password)
        usuario.save(using = self._db)
        return usuario
    
    def create_staffuser(self, correo, password):
        usuario = self.create_user(correo, password=password)
        usuario.staff = True
        usuario.save(using = self._db)
        return usuario

    def create_superuser(self, correo, password):
        usuario = self.create_user(correo, password=password)
        usuario.staff = True
        usuario.admin = True
        usuario.save(using = self._db)
        return usuario



class Admin(AbstractBaseUser):
    usuario = models.CharField(max_length=200)
    correo = models.EmailField(verbose_name='correo',max_length=100, unique=True)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.usuario
    
    def get_short_name(self):
        return self.usuario
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
    def __str__(self):
        return self.usuario


#MODELOS MANGA
class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

class Manga(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class Capitulo(models.Model):
    numero = models.IntegerField()
    manga = models.ForeignKey(Manga, null=True, blank=True, on_delete=models.CASCADE)

class ImagenesCapitulo(models.Model):
    capitulo = models.ManyToManyField(Capitulo, blank = True)
    images = models.ImageField(upload_to='manga') 