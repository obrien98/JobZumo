from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Business, Job
from .forms import JobForm, BusinessRegistrationForm, JobSeekerEmailForm
from pyzipcode import ZipCodeDatabase
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'job/index.html')

@login_required
def business_registration(request):
    if request.method == 'POST':
        form = BusinessRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user= request.user # set user
            instance.save()
            return redirect('dashboard')
    else:
        form = BusinessRegistrationForm()
    return render(request, 'job/business_registration.html', {'section': 'dashboard', 'form':form})


def search_results(request):
    query =request.GET.get('query') # grab user query
    zcdb = ZipCodeDatabase() # create instance of zip code database object
    zipcode = zcdb[query] # not too sure. Maybe this is a really long list of zip codes and this is how you access one?
    zip_codes_in_radius = [z.zip for z in zcdb.get_zipcodes_around_radius(query, 15)]
    jobs = []
    for zip in zip_codes_in_radius:
        jobs_in_zip = Job.objects.filter(business__zip_code = zip)
        if jobs_in_zip:
            jobs += jobs_in_zip
    form = JobSeekerEmailForm() # pass email subscription from to template
    return render(request, 'job/search_results.html', {'query':query, 'jobs': jobs, 'form':form})

@login_required # if the user isn't logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Ex: /accounts/login?next=/polls/3
def dashboard(request):
    jobs = Job.objects.filter(business__user=request.user)
    new_job = False
    for job in jobs:
        if job.new:
            new_job = True
            job.new = False # set to false so it's not considered new next time dashboard is loaded
            job.save()
    return render(request, 'job/dashboard.html', {'section': 'dashboard', 'jobs':jobs, 'new_job': new_job})

@login_required # if the user isn't logged in, redirect to settings.LOGIN_URL, passing the current absolute path in the query string. Ex: /accounts/login?next=/polls/3
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.business= Business.objects.get(user=request.user)
            instance.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'job/post_job.html', {'section': 'dashboard', 'form':form})

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'job/edit_job.html'

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'job/delete_job.html'
    success_url = reverse_lazy('dashboard')

def job_seeker_email(request):
    return HttpResponse('fu')
