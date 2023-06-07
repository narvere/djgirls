from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Tere maailm. I'm here!")
