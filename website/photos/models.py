from django.db import models
from django.contrib.auth.models import(
     AbstractBaseUser, BaseUserManager

)


# Create your models here.
'''class Albums(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
    #    return '%s %s' % (self.album_title, self.artist)
        return self.album_title + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Albums,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
        '''
class UserManager(BaseUserManager):
    def create_user(self,password=None,mob_no=0,is_active=True,is_patient=False,is_admin=False,is_org=False):
        if not mob_no:
            raise ValueError("Users must have a contact number")
        if not password:
            raise ValueError("User must have a password")
        user_obj=self.model()

        user_obj.set_password(password)

        user_obj.patient= is_patient
        user_obj.org = is_org
        user_obj.admin = is_admin
        user_obj.active = is_active

        user_obj.save(using=self._db)
        return user_obj

    def create_patient(self,password,mob_no):
        user_patient=self.create_user(
            password=password,
            is_patient=True
        )
        return user_patient

    def create_org(self,password,mob_no):
        user_patient=self.create_user(
            password=password,
            is_org=True
        )
        return user_patient

    def create_admin(self,password,mob_no):
        user_patient=self.create_user(
            password=password,
            is_admin=True
        )
        return user_patient

    def create_patient(self,password,mob_no):
        user_patient=self.create_user(
            password=password,
            is_patient=True
        )
        return user_patient

class User(AbstractBaseUser):

    mob_no= models.IntegerField(max_length=10)
    #mob_no= models.CharField(max_length=10)
    patient= models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    org= models.BooleanField(default=False)
    admin= models.BooleanField(default=False)

    def __str__(self):
        return

    @property
    def is_patient(self):
        return self. patient

    @property
    def is_active(self):
        return self. active
    @property
    def is_org(self):
        return self.org

    @property
    def is_admin(self):
        return self.admin

    USERNAME_FIELD = 'mob_no'

