from django.contrib import admin
from .models import Business, Job, JobSeekerEmail

# Register your models here.
admin.site.register(Business)
admin.site.register(Job)
admin.site.register(JobSeekerEmail)
