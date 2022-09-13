from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    _list = [x for x in range(10)]
    #_list = []
    context = {
        'name': "ANTOINE",
        'mylist': _list,
	}
    return render(request, 'page_home/index.html', context)
