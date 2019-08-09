from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
)
# Create your views here.

def register(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can login.')
            return redirect('login')

    else:
        form = UserRegisterForm(request.POST)
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(requset):

    if requset.method == 'POST':
        u_form = UserUpdateForm(requset.POST, instance=requset.user)
        p_form = ProfileUpdateForm(requset.POST, requset.FILES, instance=requset.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(requset, f'your account has been updated!')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=requset.user)
        p_form = ProfileUpdateForm(instance=requset.user.profile)

    context = {
        'u_form':u_form,
        'p_form': p_form
    }
    return render(requset, 'users/profile.html', context)



