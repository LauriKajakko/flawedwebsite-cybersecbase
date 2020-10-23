from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note

# Create your views here.

@login_required
def homePageView(request):
    return render(request, 'pages/index.html')
