from django.shortcuts import render
from .models import User


# Create your views here.


def user_list(request):
	users = User.objects.all()
	male_count = User.objects.filter(gender__iexact='male').count()
	back_count = User.objects.filter(department__iexact='backend').count()
	front_count = User.objects.filter(department__iexact='frontend').count()
	qa_count = User.objects.filter(department__iexact='qa').count()
	female_count = User.objects.filter(gender__contains='female').count()

	beg_count = User.objects.filter(experience__iexact='beginner').count()
	inter_count = User.objects.filter(experience__iexact='intermediate').count()
	exp_count = User.objects.filter(experience__iexact='expert').count()

	
	context = {
		"users" : users, 
		'male_count' : male_count,
		'female_count': female_count,
		'back_count': back_count,
		'front_count': front_count,
		'qa_count': qa_count,
		'beg_count': beg_count,
		'inter_count': inter_count,
		'exp_count': exp_count,
	}

	return render(request, 'users/user-list.html', context)