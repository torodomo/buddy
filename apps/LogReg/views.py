#LogReg
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import userDB

def log_reg(request):
    if request.method == "POST":
        if request.POST['attempt'] == "register":
            response = userDB.objects.check_create(request.POST)
        elif request.POST['attempt'] == 'login':
            response = userDB.objects.check_login(request.POST)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('travel:main')
        else:
            request.session['user'] = {
                'name': response[1].name,
                'username' : response[1].username,
                'id': response[1].id,
            }
        return redirect('travel:dashboard')
    return redirect('travel:main')

def logout(request):
    request.session.clear()
    return redirect('travel:main')
