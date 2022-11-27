from django.shortcuts import render

# Create your views here.

def invoice(request):
    return render(request, 'pages/examples/invoice.html')

def invoice_print(request):
    return render(request, 'pages/examples/invoice-print.html')

def profile(request):
    return render(request, 'pages/examples/profile.html')

def e_commerce(request):
    return render(request, 'pages/examples/e-commerce.html')

def projects(request):
    return render(request, 'pages/examples/projects.html')

def project_add(request):
    return render(request, 'pages/examples/project-add.html')

def project_edit(request):
    return render(request, 'pages/examples/project-edit.html')

def project_detail(request):
    return render(request, 'pages/examples/project-detail.html')

def contacts(request):
    return render(request, 'pages/examples/contacts.html')

def faq(request):
    return render(request, 'pages/examples/faq.html')

def contact_us(request):
    return render(request, 'pages/examples/contact-us.html')