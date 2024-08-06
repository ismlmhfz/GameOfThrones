from django.shortcuts import render
from .models import Case

# Create your views here.
def home(request):
    cases = Case.objects.all()
    return render(request, 'home.html', {'cases': cases})

#search function for cases
def search(request):
    query = request.GET['query']
    cases = Case.objects.filter(title__icontains=query)
    return render(request, 'home.html', {'cases': cases})

#view case function
def case_view(request):
    return render(request, 'case_view.html')