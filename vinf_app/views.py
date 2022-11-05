from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Post


# context dictionary

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'vinf_app/index.html', context)

def about(request):
    return render(request, 'vinf_app/about.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email= request.POST['email'] 
        subject = request.POST['subject'] 
        message = request.POST['message']

        #sending the email
        send_mail(
            name,
            message,
            email,
            ['kartikanand.champ2@gmail.com'],
        )
        return render(request, 'vinf_app/contact.html', {'name': name, 'email':email})
    else:
        return render(request, 'vinf_app/contact.html', {})


def gallery(request):
    return render(request, 'vinf_app/instructor.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'vinf_app/blog.html', context)

def blogPage(request):
    return render(request, 'vinf_app/blog_details.html')

def courses(request):
    return render(request, 'vinf_app/courses.html')