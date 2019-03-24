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

def styleTemplat(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/edit/style-template.html', context)

def caseSimulate(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/edit/case-simulate.html', context)

def caseSimulateCases(request):
  context          = {}
  context['path'] = request.path
  return render(request, 'aliwood/pages/edit/case.html', context)

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