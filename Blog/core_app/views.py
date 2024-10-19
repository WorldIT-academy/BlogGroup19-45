from django.shortcuts import render

# Create your views here.

def render_home(request):
    return render(template_name= 'core_app/home.html', request= request)

def render_authorization(request):
    return render(template_name= 'core_app/authorization.html', request= request)

def render_registration(request):
    return render(template_name= 'core_app/registration.html', request= request)