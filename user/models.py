from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.utils import timezone

import uuid
from django.utils.text import slugify
from . utils import slug_config

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		
		user = self.model(
			email=self.normalize_email(email),
			username=username,		
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username			
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

def get_profile_image_filepath(self, filename):
	return 'profile/' + str(self.username) + '/profile_image.png'

def get_default_profile_image():
	return "profile/default.png"

GENDER = (
    ('MALE', 'M'),
    ('FEMALE', 'F'),
)
CATEGORY = (
    ('Seller', 'Seller'),
    ('Buyer', 'Buyer'),
)
class User(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	first_name 				= models.CharField(max_length=120, blank=True, null=True)
	last_name 				= models.CharField(max_length=120, blank=True, null=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	email_verified	 		= models.CharField(max_length=30, default='No')
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	
	gender = models.CharField(choices=GENDER, max_length=50, blank=True, null=True) 
	date_of_birth = models.DateTimeField(blank=True, null=True)
	gender = models.CharField(choices=GENDER, max_length=50, blank=True, null=True)
	hide_email				= models.BooleanField(default=True)
	profile_image			= models.ImageField(
		max_length=255, blank=True, null=True, upload_to=get_profile_image_filepath, 
		default=get_default_profile_image)
	updated = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(blank=True, null=True)
	

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username',]

	objects = MyAccountManager()

	class Meta:
		verbose_name = 'User'

	def save(self, *args, **kwargs):		
		if self.slug is None:
			slg = str(uuid.uuid4())[:7]
			self.slug = "{}-{}".format(slugify(self.username), slugify(slug_config(slg))) 
		if self.slug is not None:
			self.slug = "{}-{}".format(slugify(self.username), self.slug[-12:])
		super().save(*args, **kwargs)

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
	
	@property
	def full_name(self):
		return "{} {}".format(self.first_name, self.last_name)
	