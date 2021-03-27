from django.db import models

# Create your models here.


class User(models.Model):
	gender_choice = (
			('male', 'Male'),
			('female', 'Female')
		)

	exp_choice = (
			('beginner', 'Beginner'),
			('intermediate', 'Intermediate'),
			('expert', 'Expert')
		)

	dept_choice = (
			('backend', 'Backend'),
			('frontend', 'Frontend'),
			('qa', 'QA')
		)

	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	age = models.IntegerField()
	gender = models.CharField(choices=gender_choice, max_length=80)
	experience = models.CharField(choices=exp_choice, max_length=80)
	department = models.CharField(choices=dept_choice, max_length=80)
	joined = models.DateField(auto_now_add=True)


	def __str__(self):
		return self.first_name