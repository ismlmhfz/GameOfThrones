from django.shortcuts import render
from .models import Case

# Create your views here.
def home(request):
    cases = Case.objects.all()
    return render(request, 'home.html', {'cases': cases})

