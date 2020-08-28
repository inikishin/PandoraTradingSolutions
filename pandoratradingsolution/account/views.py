from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile
from .forms import UserEditForm, ProfileEditForm

def profile_view(request):
    return render(request, 'account/ms_profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            form = SignUpForm(request.POST)
            return render(request, 'account/ms_signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'account/ms_signup.html', {'form': form})

def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})