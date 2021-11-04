from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    print(search)
    output_for_search ={
        'search': search,
    }
    return render(request, 'list_app/new_search.html', output_for_search)