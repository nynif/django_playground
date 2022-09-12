from django.shortcuts import render, redirect

def home(request):
    return redirect("page_home:index") # redirect to your page