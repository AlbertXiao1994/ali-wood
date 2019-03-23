from django.shortcuts import render
from django.core.paginator import Paginator
 
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

def genRank(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/rank/genRank.html', context)

def rankResult(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/rank/rankResult.html', context)

def history(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/history.html', context)