from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def signup_view(request):
    # form = UserCreationForm()
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user=form.save()
    #         return redirect('posts:list')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'accounts/signup.html',{'form': form })
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            # log in the user
            user = form.get_user()
            login(request,user)
            return redirect('posts:list')   
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')   



