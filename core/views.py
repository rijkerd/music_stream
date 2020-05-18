from django.shortcuts import redirect
from django.http import request


def HomePage(request):
    return redirect('/api/v1/users')
