from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import People

def index(request):
    context = {
        "list_people": People.objects.all(),
	}
    return render(request, 'page_team/index.html', context)

def detail(request, id_people):
	people = get_object_or_404(People, pk=id_people)
	context = {
		'people': people,
		'img_url': '/'.join(str(people.main_picture).split("/")[1:])
	}
	return render(request, 'page_team/detail.html', context)