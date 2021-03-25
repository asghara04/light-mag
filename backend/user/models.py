from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from image.models import Image
from category.models import Category
import jdatetime

def set_jdate(gdate):
	jdatetime.set_locale("fa_IR")
	if gdate:
		return jdatetime.datetime.fromgregorian(year=gdate.year,month=gdate.month,day=gdate.day).strftime("%A, %d %B %Y")
	return None

class UserManager(BaseUserManager):
	def create_user(self, email, username, name, password=None):
		if not email:
			raise VueError("Enter an email please")
		elif not username:
			raise ValueError("Enter an username please")
		elif not name:
			raise ValueError("Enter a name please")

		user = self.model(email = self.normalize_email(email), username = username, name = name)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, username, name, password):
		if not email:
			raise ValueError("Enter an email please")
		elif not username:
			raise ValueError("Enter an username please")
		elif not name:
			raise ValueError("Enter a name please")
		elif not password:
			raise ValueError("Enter a password please")

		user = self.create_user(email = self.normalize_email(email), password = password, username = username, name = name)
		user.is_staff = True
		user.save(using=self._db)
		return user


class ActiveUser(models.Manager):
	def get_queryset(self):
		return super(ActiveUser,self).get_queryset().filter(is_active=True,is_staff=True)


class User(AbstractBaseUser):
	email = models.EmailField(max_length=30, unique=True)
	username = models.SlugField(max_length=30, unique=True)
	name = models.CharField(max_length=35)
	prof_picture = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
	join_date = models.DateField(auto_now_add=True)
	last_login = models.DateField(auto_now=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	pubmail = models.EmailField(max_length=30, unique=True, blank=True, null=True)
	bio = models.TextField(max_length=400, blank=True, null=True)
	about = models.TextField(max_length=400, blank=True, null=True)
	favorite_cat = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	instagram_link = models.URLField(max_length=35, blank=True, null=True)
	facebook_link = models.URLField(max_length=35, blank=True, null=True)
	github_link = models.URLField(max_length=35, blank=True, null=True)
	birthday  = models.DateField(blank=True, null=True)

	objects = UserManager()
	actives = ActiveUser()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ("username", "name")

	def jjoin(self):
		return set_jdate(self.join_date)
	def jlast(self):
		return set_jdate(self.last_login)
	def jbirth(self):
		return set_jdate(self.birthday)
	def pubartcount(self):
		return self.arts.filter(status="عمومی").count()
	def artcount(self):
		return self.arts.all().count()
	def __str__(self):
		return self.username
	def has_perm(self,  perm, obj=None):
		return self.is_staff
	def has_module_perms(self, app_label):
		return True
