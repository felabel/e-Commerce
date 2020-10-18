from django.contrib.auth import authenticate, login, get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        "title":"hello world",
        "content":"welcome to the homepage",
        

    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAAHHHH"

        

    return render(request, "home_page.html", context)

def about(request):
    context = {
        "title":"xup with u",
        "content":"welcome to the about page"
    }
    return render(request, "about.html", context)

def product(request):
    context = {
        "title":"we have really awesome gadgets that you can purchase at ur convenience",
        "content":"za product page"
    }
    return render(request, "product.html", context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"lets connect",
        "content":"hoola",
        "form":contact_form
        # "brand": "new brand Name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST": 
        # print(request.POST)
        # print(request.POST.get('fname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('message'))
    return render(request, "contact/contact.html", context)

    #  login page
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("user logged in")
    # print(request.user.is_authenticated) 
    if form.is_valid():
        print(form.cleaned_data)
        
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            # redirect to success page
            # context['form'] = LoginForm()
            # context['form'] = LoginForm()
            return redirect("/login")
        else:
            # return an ivalid error message
            print("error")
    
    
    return render(request, "auth/login.html", context)
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request,"auth/register.html", context)

