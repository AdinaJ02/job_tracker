from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm

def job_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'job_list.html', {'applications': applications})

def job_add(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'job_form.html', {'form': form, 'action': 'Add'})

def job_edit(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'job_form.html', {'form': form, 'action': 'Edit'})

def job_delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('job_list')
    return render(request, 'job_confirm_delete.html', {'application': application})
