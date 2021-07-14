from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    '''register a new user'''
    if request.method != 'POST':
        #blank registration
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)
        
        if form.is_valid():
            new_user = form.save()
            #log them in and redirect to index
            login(request, new_user)
            return redirect('UnicornLog_REST:index')
    #display blank form
    context= {'form' : form}
    return render(request, 'registration/register.html', context)