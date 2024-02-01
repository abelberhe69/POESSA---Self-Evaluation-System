from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
import random
from Account.models import CustomUser
from Account.forms import CustomUserCreationForm

# Create your views here.

def የ6ወር_ስኮርካርድ_እቅድ_ቅፅ(request):
    context = {
        'የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_view' : የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model.objects.all(),
    }
    return render(request, 'demo1.html', context)

def የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1(request):
    context = {
        'የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_view' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model.objects.all(),
    }
    return render(request, 'የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 1.html', context)

def የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2(request):
    context = {
        'የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_view' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model.objects.all(),
    }
    return render(request, 'የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 2.html', context)

def የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3(request):
    context = {
        'የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_view' : የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model.objects.all(),
    }
    return render(request, 'የ6ወር የባህሪ መመዘኛ ቅፅ/የ6ወር የባህሪ መመዘኛ ቅፅ 3.html', context)

def የድርጊት_መርሃ_ግብር_ቅፅ(request):
    context = {
        'የድርጊት መርሃ ግብር ቅፅ' : Employee.objects.all(),
    }
    return render(request, 'የድርጊት መርሃ ግብር ቅፅ/የድርጊት መርሃ ግብር ቅፅ.html', context)

def formAdd(request):
    form = demoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = demoForm()
    context = {
        'demoForm':form
    }
    return render(request, 'demo1.html', context)




def formView(request):
    user = request.user
    context = {
        'formList' : demoModel.objects.filter(user = user)
    }
    return render(request, 'admin_list.html', context)

def homepage(request):
    context = {

    }
    return render(request, 'homepage.html', context)

def printForm(request):
    context = {
        'printForm' : demoModel.objects.all()
    }
    return render(request, 'print_form.html', context)

# User
def userList(request):
    context = {
        'userList' : CustomUser.objects.all()
    }
    return render(request, 'user_list.html', context)

def deleteUser(request, id):
    deleteuser = get_object_or_404(CustomUser, pk=id)
    context = {'deleteuser': deleteuser}    
    
    if request.method == 'GET':
        return render(request, 'delete_user.html',context)
    elif request.method == 'POST':
        deleteuser.delete()
        messages.success(request,  'The list has been deleted successfully.')
        return redirect('userList')
    
def editUser(request, id):
    edituser = get_object_or_404(CustomUser, id=id)

    if request.method == 'GET':
        context = {'form': CustomUserCreationForm(instance=edituser), 'id': id}
        return render(request,'edit_user.html',context)
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=edituser)
        if form.is_valid():
            form.save()
            messages.success(request, 'The list has been updated successfully.')
            return redirect('userList')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'edit_user.html',{'form':form})
