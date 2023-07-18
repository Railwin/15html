from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Person
from .models import rap
from .models import info
from .models import look
from .models import famous

# Create your views here.
def home(request):
    return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def index(request):
    text = Person.objects.order_by('name')
    context = {'text': text}
    return render(request, 'my1.html', context)

def index2(request):
    text = info.objects.order_by('opred')
    context = {'text': text}
    return render(request, 'my2.html', context)

def index3(request):
    text = famous.objects.order_by('Person')
    context = {'text': text}
    return render(request, 'my3.html', context)

def index4(request):
    text = rap.objects.order_by('type')
    context = {'text': text}
    return render(request, 'my4.html', context)

def index5(request):
    text = look.objects.order_by('types')
    context = {'text': text}
    return render(request, 'my5.html', context)