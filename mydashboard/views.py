from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def signin_page(request):
    return render(request,'mydashboard/signin.html')

def signin(request):
    """
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        else:
            return render(request,'mydashboard/signin.html',{'failed_message':'Please enable cookies and try again.'})
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username = username,
            password = password)
    if user is not None:
        login(request,user)
        return redirect('index')
    else:
        return render(request,'mydashboard/signin.html',{'failed_message':'user or password error'})

def index(request):
    if request.user.is_authenticated:
        return render(request,'mydashboard/index.html')
    else:
        return redirect('signin_page')

def order(request):
    return render(request,'mydashboard/order.html')

def reporter(request):
    return render(request,'mydashboard/reporter.html')

def employee_management(request):
    return render(request,'mydashboard/employee_management.html')

def settings(request):
    return render(request,'mydashboard/settings.html')

def res(request):
    return render(request,'mydashboard/res.html')

def marketing(request):
    return render(request,'mydashboard/marketing.html')
