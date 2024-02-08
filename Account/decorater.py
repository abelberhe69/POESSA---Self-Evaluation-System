from django.http import HttpResponse
from django.shortcuts import redirect

def admin_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to access this content.')
    return wrapper_func

def director_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == 'director':
            return view_func(request, *args, **kwargs)
        else:
             return HttpResponse('You are not authorized to access this content.')
    return wrapper_func

def team_leader_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == 'team_leader':
            return view_func(request, *args, **kwargs)
        else:
             return HttpResponse('You are not authorized to access this content.')
    return wrapper_func

def expert_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role == 'expert':
            return view_func(request, *args, **kwargs)
        else:
             return HttpResponse('You are not authorized to access this content.')
    return wrapper_func
