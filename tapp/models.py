
from django.db import models
from django.contrib import auth
# Create your models here.
# accounts.models.py
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# accounts.models.py

class UserManager(BaseUserManager):
    def create_user(self, email,rollnumber=None,phone=None,username=None,backlogs=None,resume=None,branch=None,gender=None, year=None, section=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('User must have an Password')
        user = self.model(
            email=self.normalize_email(email),

        )
        user.username=username
        user.year=year
        user.section=section
        user.gender=gender
        user.branch=branch
        user.backlogs=backlogs
        user.resume=resume
        user.phone=phone
        user.rollnumber=rollnumber
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,

        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_studentuser(self, email,password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,

        )
        user.student = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.student = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username=models.CharField(
    max_length=30,
    null=True,blank=True
     )
    g_choices=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
    )
    gender=models.CharField(max_length=10,null=True,blank=True,choices=g_choices)
    y_choices=(('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
    ('4th','4th'),)
    year=models.CharField(max_length=10,null=True,blank=True,choices=y_choices)
    s_choices=(
    ('Section A','Section A'),
    ('Section B','Section B'),
    ('Section C','Section C'),
    ('Section D','Section D'),)
    section=models.CharField(max_length=10,null=True,blank=True,choices=s_choices)
    b_choices=(
    ('M.C.A','M.C.A'),
    ('M.B.A','M.B.A'),
    ('E.C.E','E.C.E'),
    ('E.E.E','E.E.E'),
    ('C.S.E','C.S.E'),
    ('IT','IT'      ),
    ('CIVIL','CIVIL'),
    )
    back_choices=(
        ('0','0'),
        ('1','1'),
        ('Above one','Above one')
    )
    backlogs=models.CharField(max_length=10,null=True,blank=True)
    resume=models.FileField(upload_to='resume',blank=True) 
    branch=models.CharField(max_length=10,null=True,blank=True,choices=b_choices)
    phone=models.IntegerField(unique=True,null=True,blank=True)
    rollnumber=models.CharField(max_length=10,null=True,blank=True,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False)
    datejoined = models.DateTimeField(default=timezone.now)
     # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects=UserManager()


    def get_username(self):

        return self.email

    def get_rollnumber(self):

        return self.email

    def get_phone(self):

        return self.email

    def get_branch(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
            # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    # @property
    # def is_student(self):
    #     "Is the user a member of stusent?"
    #     return self.student

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


class add(models.Model):
    subject = models.CharField(max_length=300,blank=False)
    d_choices=(
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard'),
    )
    deficulty = models.CharField(max_length=10,blank=False,choices=d_choices)
    question= models.CharField(max_length=5000,blank=False,)
    Option1= models.CharField(max_length=1000,blank=False,)
    Option2= models.CharField(max_length=1000,blank=False,)
    Option3= models.CharField(max_length=1000,blank=False,)
    Option4= models.CharField(max_length=1000,blank=False,)
    o_choices=(
    ('Option1','Option1'),
    ('Option2','Option2'),
    ('Option3','Option3'),
    ('Option4','Option4'),
    )
    option= models.CharField(max_length=1000,blank=False,choices=o_choices)

    def __str__(self):
        return self.subject
    def __str__(self):
        return self.deficulty
