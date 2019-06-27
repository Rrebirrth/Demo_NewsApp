from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateFrom, ProfileUpdateFrom
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You may now login as {username}!')
            return redirect('login')


    else:    
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateFrom(request.POST,instance=request.user)
        p_form = ProfileUpdateFrom(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.success(request, 'Your profile has not been updated, there was an error in your submission')
            return redirect('profile')


    else:
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }


    return render(request, 'users/profile.html',context)














