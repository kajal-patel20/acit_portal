from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import AssetRequestForm
from .models import AssetRequest


def login_view(request):
    """Handles HOD login."""
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request, 'requests_app/login.html', {'form': form, 'title': 'HOD Login'})

@login_required
def logout_view(request):
    """Handles HOD logout."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')


@login_required
def dashboard_view(request):
    """Shows all requests submitted by the logged-in HOD."""
    requests = AssetRequest.objects.filter(user=request.user).order_by('-date_submitted')
    
    context = {
        'requests': requests,
        'title': f"{request.user.username}'s Dashboard"
    }
    return render(request, 'requests_app/dashboard.html', context)

@login_required
def new_request_view(request):
    """Handles the new asset request form submission."""
    if request.method == 'POST':
        form = AssetRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user 
            new_request.save()
            messages.success(request, 'Your request has been submitted successfully! Status: Pending.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AssetRequestForm() 
        
    context = {
        'form': form,
        'title': 'Send a New Request'
    }
    return render(request, 'requests_app/send_request.html', context)
