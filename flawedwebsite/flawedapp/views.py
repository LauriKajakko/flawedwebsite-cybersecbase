from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note

# Create your views here.

@login_required
def homePageView(request):
    	
	items = []
	for note in Note.objects.all():
    		items.append(note.content + ' -added by %s' % note.owner)
	
	return render(request, 'pages/index.html', {'items' : items})

@login_required
def addView(request):
    	
	note = Note(owner = request.user, content = request.POST.get('content', '').strip())
	note.save()

	return redirect('/')