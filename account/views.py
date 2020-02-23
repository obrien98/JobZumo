from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required



def user_login(request):
    if request.method == 'POST': # when user submits form via POST
        form = LoginForm(request.POST) # instantiate form with submitted data
        if form.is_valid(): # if not valid we display the form errors in our template (ex: the user didn't fill in one of the fields)
            cd = form.cleaned_data # while you can access request.POST directly. cleaned_data not only validates the data for you but also converts it into the relevant python types
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('log in success')
                else:
                    return HttpResponse('Disabled account.')
            else:
                return('Invalid login.')
    else:
        form = LoginForm() # when view is called with a GET reqeust, instantiate a new login form to display in the template
    return render(request, 'core/login.html', {'form':form} )

def signup(request):
    if request.method == 'POST': # if method is post, user submitted form with data (or blank but thats unlikely)
        print('working')
        form = SignUpForm(request.POST) # create instance of form with data attached to it?
        if form.is_valid():
            form.save() # forms come with save() that saves object to db i think
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # verifies a set of credentials, returns User object if they are valid
            login(request, user) # attach authenticated user to current session
            return redirect('business_registration')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
