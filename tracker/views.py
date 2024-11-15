from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

@login_required
def job_list(request):
    # Fetch job applications for the logged-in user
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'job_list.html', {'applications': applications})

@login_required
def job_add(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the logged-in user with the job application
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'job_form.html', {'form': form, 'action': 'Add'})

@login_required
def job_edit(request, pk):
    # Ensure the user can only edit their own applications
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'job_form.html', {'form': form, 'action': 'Edit'})

@login_required
def job_delete(request, pk):
    # Ensure the user can only delete their own applications
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        application.delete()
        return redirect('job_list')
    return render(request, 'job_confirm_delete.html', {'application': application})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('job_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('job_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
