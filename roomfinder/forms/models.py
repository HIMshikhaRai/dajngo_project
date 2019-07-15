from django.db import models

# Create your models here.
class RenterForm(models.Model):
	first_name = models.CharField(verbose_name = "First Name", max_length = 160)
	last_name = models.CharField(verbose_name = "Last Name", max_length = 160)
	email = models.EmailField(verbose_name = "Email", max_length = 160)
	password = models.CharField(verbose_name = "Password", max_length = 160)
	gender = models.CharField(verbose_name = "gender", max_length = 160)

class LandlordForm(models.Model):
	first_name = models.CharField(verbose_name = "First Name", max_length = 160)
	last_name = models.CharField(verbose_name = "Last Name", max_length = 160)
	email = models.EmailField(verbose_name = "Email", max_length = 160)
	password = models.CharField(verbose_name = "Password", max_length = 160)
	gender = models.CharField(verbose_name = "gender", max_length = 160)