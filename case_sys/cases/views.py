from django.shortcuts import render
from .models import Case
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    query = request.GET.get('query', '')
    
    if query:
        cases_list = Case.objects.filter(
            Q(case_name__icontains=query) |
            Q(case_description__icontains=query) |
            Q(case_status__icontains=query) |
            Q(case_priority__icontains=query) |
            Q(case_assignee__icontains=query)
        )
    else:
        cases_list = Case.objects.all()  # Retrieve all cases if no query is provided

    paginator = Paginator(cases_list, 10)  # Show 10 cases per page
    page_number = request.GET.get('page')  # Get current page number from query params
    cases = paginator.get_page(page_number)  # Get cases for the current page

    return render(request, 'home.html', {'cases': cases, 'query': query})

#view case function
def case_view(request):
    return render(request, 'case_view.html')