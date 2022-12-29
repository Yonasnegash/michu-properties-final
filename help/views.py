from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Help

def help(request):
    if request.method == 'POST':
        name = request.POST['message-name']
        email = request.POST['message-email']
        message = request.POST['message']

        send = Help(fullname=name, email=email, message=message)
        send.save()
        messages.success(request, 'Your has been submitted, Thank you!')
        return redirect('/')
        # if send:
        #     messages.error(request, 'Your message is not submitted. Please try again')
        #     return redirect('/')
        # else:
        #     messages.success(request, 'Your has been submitted, Thank you!')
        #     return redirect('/')