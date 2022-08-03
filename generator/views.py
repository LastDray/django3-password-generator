from operator import length_hint
from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for character in range(length):
        thepassword += random.choice(characters)

    
    return render(request, 'generator/password.html', {'password':thepassword})

def description(request):
    return render(request, 'generator/description.html')