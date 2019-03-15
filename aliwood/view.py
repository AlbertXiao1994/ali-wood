from django.shortcuts import render
 
def home(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'aliwood/home.html', context)