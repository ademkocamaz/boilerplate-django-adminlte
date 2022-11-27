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

def login(request):
    return render(request, 'pages/examples/login.html')

def register(request):
    return render(request, 'pages/examples/register.html')

def forgot_password(request):
    return render(request, 'pages/examples/forgot-password.html')

def recover_password(request):
    return render(request, 'pages/examples/recover-password.html')

def login_v2(request):
    return render(request, 'pages/examples/login-v2.html')

def register_v2(request):
    return render(request, 'pages/examples/register-v2.html')

def forgot_password_v2(request):
    return render(request, 'pages/examples/forgot-password-v2.html')

def recover_password_v2(request):
    return render(request, 'pages/examples/recover-password-v2.html')

def lockscreen(request):
    return render(request, 'pages/examples/lockscreen.html')

def legacy_user_menu(request):
    return render(request, 'pages/examples/legacy-user-menu.html')