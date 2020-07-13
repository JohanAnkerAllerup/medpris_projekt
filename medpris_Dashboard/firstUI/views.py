from django.shortcuts import render

# Create your views here.
def indexPage(request):
    context= {'a': 'a'}
    return(render(request, 'index.html', context))