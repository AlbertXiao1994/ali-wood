from django.shortcuts import render
 
def home(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/home.html', context)

def data(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/data.html', context)

def edit(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/edit.html', context)

def rank(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/rank.html', context)

def history(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/history.html', context)