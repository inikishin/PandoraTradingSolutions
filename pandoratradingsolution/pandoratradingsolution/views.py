from django.shortcuts import render, redirect

from dailyAnalysis.models import Post
from .form import SignUpForm

def mainpage(request):
    post_list = Post.objects.order_by('-date_analysis')[:30]

    context = {'post_list': post_list}

    return render(request, 'pandoratradingsolution/ms_index.html', context)

def handler404(request, exception):
    return render(request, 'pandoratradingsolution/error404.html', status=404)

def handler500(request):
    return render(request, 'pandoratradingsolution/error500.html', status=500)

def profile_view(request):
    return render(request, 'pandoratradingsolution/ms_profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("1")
        if form.is_valid():
            print("2")
            new_user = form.save()
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            return redirect('mainpage')
        else:
            form = SignUpForm(request.POST)
            return render(request, 'pandoratradingsolution/ms_signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'pandoratradingsolution/ms_signup.html', {'form': form})

def contact(request):
    return render(request, 'pandoratradingsolution/ms_contact.html')

def about(request):
    return render(request, 'pandoratradingsolution/ms_about.html')