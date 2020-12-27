from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from .models import Note2
from django.db.models import Q

# Create your views here.

@login_required
def homePageView(request):
        
    return render(request, 'pages/home.html')

def noteView(request):
    items = []

    for note in Note.objects.filter(Q(private = False)):
            items.append(note.content + ' -added by %s' % note.owner)
            
    return render(request, 'pages/index.html', {'items' : items})

def note2View(request):
    items2 = []

    for note2 in Note2.objects.filter(Q(private = False)):
            items2.append(note2.content + ' -added by %s' % note2.owner)
            
    return render(request, 'pages/indexcopy.html', {'items' : items2})

def addView(request):
    priv = False
    if request.POST.get('private') == 'on':
            priv=True

    note = Note(owner = request.user, content = request.POST.get('content', '').strip(), private = priv)	
    note.save()

    return redirect('/index')

def add2View(request):
    priv = False
    if request.POST.get('private') == 'on':
            priv=True


    # query = ('INSERT INTO flawedapp_notes2 (content, private, owner_id) VALUES (\'%s\', v)')

    note = Note2(owner = request.user, content = request.POST.get('content', '').strip(), private = priv)	
    note.save()

    return redirect('/indexcopy')


def searchView(request):
    query = ('SELECT * FROM flawedapp_note WHERE owner_id=(SELECT id FROM auth_user WHERE username=\'%s\')' % request.POST.get('q'))
    notes = Note.objects.raw(query)

    items = []

    for note in notes:
        items.append(note)

    return render(request, 'pages/home.html', {'items' : items})


def userView(request):
    usernameQuery = request.GET.get('query', '0')

    print(usernameQuery)

    query = ('SELECT * FROM flawedapp_note WHERE owner_id=(SELECT id FROM auth_user WHERE username=\'%s\')' % usernameQuery)
    print(query)
    notes = Note.objects.raw(query)

    items = []

    for note in notes:
        print(note.content)
        items.append(note.content)

    return render(request, 'pages/userpage.html', {'items' : items})
    

def unsafequery(request):
    return redirect('/userview/?query=%s' % request.POST.get('query'))