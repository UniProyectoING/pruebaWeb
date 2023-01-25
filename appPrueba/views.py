from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home (request):

    #for i in Incripcion.objects:
    #   col.append(i)
    # noticias = Noticias.objects.all()

    # if request.method=="POST":
    #     subject="Requisitos de inscripción"
    #     message="Saludos, estimados representantes, se adjunta los requisitos de inscripción para nuevos estudiantes."
    #     email_from=settings.EMAIL_HOST_USER
    #     email = request.POST["email"]
    #     recipient_list=[f"{email}"]
    #     send_mail(subject, message, email_from, recipient_list)
    #     return render(request,'index.html',{"noticias":noticias})
    return render(request,'index.html')

def index (request):
    return render(request,'')