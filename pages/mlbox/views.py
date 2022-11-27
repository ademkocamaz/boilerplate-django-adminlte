from django.shortcuts import render

# Create your views here.

def mailbox(request):
    return render(request, 'pages/mailbox/mailbox.html')

def compose(request):
    return render(request, 'pages/mailbox/compose.html')

def read_mail(request):
    return render(request, 'pages/mailbox/read-mail.html')