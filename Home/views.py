from django.shortcuts import render
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=phone, message=message, date=date)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')

        html = render_to_string('emails/contact.html', {'name': name, 'email': email, 'phone': phone, 'message': message})
        send_mail(
            'Message from Portfolio website',
            'You have received a new message from your portfolio. Please check the admin panel for more details.','noreply@mahfujarr.com', ['mahfujarrahmanjoy@gmail.com'], html_message=html)
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'resume.html')
