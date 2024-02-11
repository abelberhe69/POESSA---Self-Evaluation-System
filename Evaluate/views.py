from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
import random
from Account.models import CustomUser
from Account.forms import CustomUserCreationForm
from Account.decorater import *
from django.contrib.auth.decorators import login_required
from Account.views import *

@login_required
def homepage(request):
    context = {
        'user' : request.user,
    }
    return render(request, 'Expert/homepage.html', context)


### ADMIN ###
@admin_user_required
@login_required
def admin_dashboard(request):
    return render(request, 'Admin/index.html')

@login_required
def userList(request):
    context = {
        'userList' : CustomUser.objects.all()
    }
    return render(request, 'Admin/user_list.html', context)

def deleteUser(request, id):
    deleteuser = get_object_or_404(CustomUser, pk=id)
    context = {'deleteuser': deleteuser}    
    
    if request.method == 'GET':
        return render(request, 'Admin/delete_user.html',context)
    elif request.method == 'POST':
        deleteuser.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('userList')

@login_required
def editUser(request, id):
    edituser = get_object_or_404(CustomUser, id=id)

    if request.method == 'GET':
        context = {'form': CustomUserCreationForm(instance=edituser), 'id': id}
        return render(request,'Admin/edit_user.html',context)
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=edituser)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'Admin/edit_user.html',{'form':form})


### Director ###
@director_user_required
@login_required
def director_index(request):
    return render(request, 'Director/index.html')


### Team-Leader ###
@team_leader_user_required
@login_required
def team_leader_index(request):
    return render(request, 'Team Leader/index.html')


# የ6ወር ስኮርካርድ እቅድ ቅፅ
@login_required
def Add_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ(request):
    form = የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_form()
    if request.method == 'POST':
        form = የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_form(request.POST)
        if form.is_valid():
            formAdd = form.save(commit=False)
            formAdd.user = request.user
            form.save()
        else:
            form = የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_form(request.POST)
    context = {
        'የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_form':form
    }
    return render(request, 'Expert/የ6ወር ስኮርካርድ እቅድ ቅፅ/Add የ6ወር ስኮርካርድ እቅድ ቅፅ.html', context)

@login_required
def View_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ(request):
    user = request.user
    context = {
        'View_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_list' : የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model.objects.filter(user = user)
    }
    return render(request, 'Expert/የ6ወር ስኮርካርድ እቅድ ቅፅ/View የ6ወር ስኮርካርድ እቅድ ቅፅ.html', context)

@login_required
def Print_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ(request, form_id):
    context = {
        'Print_የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_form' : የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model.objects.filter(id=form_id)
    }
    return render(request, 'Expert/የ6ወር ስኮርካርድ እቅድ ቅፅ/Print የ6ወር ስኮርካርድ እቅድ ቅፅ.html', context)


# የ6ወር የባህሪ መመዘኛ ቅፅ 1
@login_required
def Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1(request):
    form1 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_form()
    if request.method == 'POST':
        form1 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_form(request.POST)
        if form1.is_valid():
            form = form1.save(commit=False)
            form.user = request.user
            form.save()
        else:
            form1 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_form(request.POST)
    context = {
        'የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_form':form1
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 1/Add የ6ወር የባህሪ መመዘኛ ቅፅ 1.html', context=context)

@login_required
def View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1(request):
    context = {
        'View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_list' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model.objects.all()
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 1/View የ6ወር የባህሪ መመዘኛ ቅፅ 1.html', context)

@login_required
def Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1(request, form_id):
    context = {
        'Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_form' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model.objects.filter(id=form_id)
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 1/Print የ6ወር የባህሪ መመዘኛ ቅፅ 1.html', context)


# የ6ወር የባህሪ መመዘኛ ቅፅ 2
@login_required
def Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2(request):
    form2 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_form()
    if request.method == 'POST':
        form2 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_form(request.POST)
        if form2.is_valid():
            form = form2.save(commit=False)
            form.user = request.user
            form.save()
        else:
            form2 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_form(request.POST)
    context = {
        'የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_form':form2
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 2/Add የ6ወር የባህሪ መመዘኛ ቅፅ 2.html', context=context)

@login_required
def View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2(request):
    context = {
        'View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_list' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model.objects.all()
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 2/View የ6ወር የባህሪ መመዘኛ ቅፅ 2.html', context)

@login_required
def Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2(request, form_id):
    context = {
        'Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_form' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model.objects.filter(id=form_id)
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 2/Print የ6ወር የባህሪ መመዘኛ ቅፅ 2.html', context)


# የ6ወር የባህሪ መመዘኛ ቅፅ 3
@login_required
def Add_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3(request):
    form3 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_form()
    if request.method == 'POST':
        form3 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_form(request.POST)
        if form3.is_valid():
            form = form3.save(commit=False)
            form.user = request.user
            form.save()
        else:
            form3 = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_form(request.POST)
    context = {
        'የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_form':form3
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 3/Add የ6ወር የባህሪ መመዘኛ ቅፅ 3.html', context=context)

@login_required
def View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3(request):
    context = {
        'View_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_list' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model.objects.all()
    }
    return render(request, 'የ6ወር የባህሪ መመዘኛ ቅፅ/View የ6ወር የባህሪ መመዘኛ ቅፅ 3.html', context)

@login_required
def Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3(request, form_id):
    context = {
        'Print_የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_form' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model.objects.filter(id=form_id)
    }
    return render(request, 'Expert/የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 3/Print የ6ወር የባህሪ መመዘኛ ቅፅ 3.html', context)


# የድርጊት መርሃ ግብር ቅፅ
@login_required
def Add_የድርጊት_መርሃ_ግብር_ቅፅ(request):
    form = የድርጊት_መርሃ_ግብር_ቅፅ_form()
    if request.method == 'POST':
        form = የድርጊት_መርሃ_ግብር_ቅፅ_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        else:
            form = የድርጊት_መርሃ_ግብር_ቅፅ_form(request.POST)
    context = {
        'የድርጊት_መርሃ_ግብር_ቅፅ_form':form
    }
    return render(request, 'Expert/የድርጊት መርሃ ግብር ቅፅ/Add የድርጊት መርሃ ግብር ቅፅ.html', context=context)

@login_required
def View_የድርጊት_መርሃ_ግብር_ቅፅ(request):
    context = {
        'View_የድርጊት_መርሃ_ግብር_ቅፅ_list' : የድርጊት_መርሃ_ግብር_ቅፅ_model.objects.all()
    }
    return render(request, 'Expert/የድርጊት መርሃ ግብር ቅፅ/View የድርጊት መርሃ ግብር ቅፅ.html', context)

@login_required
def Print_የድርጊት_መርሃ_ግብር_ቅፅ(request, form_id):
    context = {
        'Print_የድርጊት_መርሃ_ግብር_ቅፅ_form' : የድርጊት_መርሃ_ግብር_ቅፅ_model.objects.filter(id=form_id)
    }
    return render(request, 'Expert/የድርጊት መርሃ ግብር ቅፅ/Print የድርጊት መርሃ ግብር ቅፅ.html', context)