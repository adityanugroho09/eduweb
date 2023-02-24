from .forms import UserRegisterForm, UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from librariesApp.models import Library ,LibraryItem
from django.utils.decorators import method_decorator
import datetime
from django.db.models import Q
from django.core.paginator import Paginator

@login_required(login_url='login_page')
def profilePage(request):
    user = request.user
    page = 'library'

    try:
        library = Library.objects.get(student=user)
    except Library.DoesNotExist:
        library = None
        
    items = request.GET.get('items') if request.GET.get('items') != None else ''

    try:
        library_items = library.libraryitem_set.filter(
            Q(course__course_name__icontains=items) |
            Q(course__content_type__type_name__icontains=items) |
            Q(course__topic__topic_name__icontains=items)
        )
    except AttributeError:
        library_items = None
    
    p = Paginator(library_items, 6)
    paginator_page = request.GET.get('page')
    item_list = p.get_page(paginator_page)

    context = {
        'user':user, 
        'library_items':library_items, 
        'page':page,
        'item_list':item_list
        }
    return render(request, 'users/profile_page.html', context)

def userRegister(request):
    page = 'register'
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login_page')
    else:
        form = UserRegisterForm
    
    currentTime = datetime.datetime.now()
    greeting = ''
    if currentTime.hour < 12:
        greeting = 'Good Morning'
    elif 12 <= currentTime.hour < 18:
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'
        
    context = {'form':form, 'page':page, 'greeting':greeting}
    return render(request, 'users/login_page.html', context)

def userLogin(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')       

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')  
                 
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Username or Password does not exist')
    
    currentTime = datetime.datetime.now()
    greeting = ''
    if currentTime.hour < 12:
        greeting = 'Good Morning'
    elif 12 <= currentTime.hour < 18:
        greeting = 'Good Afternoon'
    else:
        greeting = 'Good Evening'

    context = {'page':page, 'greeting':greeting}
    return render(request, 'users/login_page.html', context)

@login_required(login_url='login_page')
def userLogout(request):
    logout(request)
    return redirect('home_page')

@login_required(login_url='login_page')
def editProfile(request):
    page = 'edit profile'

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('profile_page')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    context = {'user_form': user_form, 'profile_form': profile_form, 'page':page}
    return render(request, 'users/profile_page.html', context)

@method_decorator(login_required(login_url='/login'), name='dispatch')
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/profile_page.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('user_logout')