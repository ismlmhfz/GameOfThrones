from django.shortcuts import render
from .models import Case

# Create your views here.
def home(request):
    query = request.GET.get('query', '')
    
    if query:
        cases = Case.objects.filter(case_id__icontains=query)
    else:
        cases = Case.objects.all()  # Return all cases if no query is provided
    
    return render(request, 'home.html', {'cases': cases, 'query': query})