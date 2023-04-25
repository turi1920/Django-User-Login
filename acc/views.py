from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'data.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
   
    if request.method=='post':
        uname=request.post['username']
        passw=request.post['password']
        user = authenticate(username='uname', password='passw')
        if user is not None:
            login(request,user)
        else:
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def data(request):
    return render(request,'data.html')