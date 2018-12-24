from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("hello customers")


def about(request):
	return HttpResponse("with our website you can shop anything at anytime and from anywhere")