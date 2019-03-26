"""aliwood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import view

urlpatterns = [
    url(r'^$', view.home, name='home'),
    url(r'^data/$', view.data, name='data'),
    url(r'^data/upload', view.upload, name='upload'),
    url(r'^data/detail', view.detail, name='detail'),
    url(r'^edit/style_templat', view.styleTemplat, name='styleTemplat'),
    url(r'^edit/case_simulate/case', view.caseSimulateCases, name='caseSimulateCases'),
    url(r'^edit/case_simulate', view.caseSimulate, name='caseSimulate'),
    url(r'^edit/gen_video', view.genVideo, name='genVideo'),
    url(r'^edit/custom_params', view.customParam, name='customParam'),
    url(r'^rank/gen_rank', view.genRank, name='genRank'),
    url(r'^rank/rank_result', view.rankResult, name='rankResult'),
    url(r'^history/', view.history, name='history'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)