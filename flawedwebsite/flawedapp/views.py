from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from django.db.models import Q

# Create your views here.

@login_required
def homePageView(request):
		
	items = []
	for note in Note.objects.filter(Q(private = False) | Q(owner = request.user)):
			items.append(note.content + ' -added by %s' % note.owner)
	
	return render(request, 'pages/index.html', {'items' : items})

@login_required
def addView(request):
	priv = False
	if request.POST.get('private') == 'on':
			priv=True
	
	print(priv)

	note = Note(owner = request.user, content = request.POST.get('content', '').strip(), private = priv)	
	note.save()

	return redirect('/')

	#on, None