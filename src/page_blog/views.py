from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'name': "ANTOINE",
	}
    return render(request, 'page_blog/index.html', context)
