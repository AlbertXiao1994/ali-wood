from django.shortcuts import render
 
def home(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/home.html', context)

def data(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/data.html', context)

def edit(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/edit.html', context)

def rank(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/rank.html', context)

def history(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/history.html', context)