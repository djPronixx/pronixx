from django.shortcuts import render
from django.http import  HttpResponse
from .models import cover , show , home_info , features_gallay, pakage, artist_wall 

# Create your views here.

def home(request):
    
    header = cover.objects.all()
    shows = show.objects.all()
    info = home_info.objects.all()
    gallary = features_gallay.objects.all()
    offer = pakage.objects.all()
    artistwall = artist_wall.objects.all()    

    jPara = {'header':header,'shows':shows , 'info': info , 'gallary':gallary , 'offer':offer , 'wall': artistwall }
   
    return render(request, 'home.html' , jPara)

def gallary(request):
    info = home_info.objects.all()
    header = cover.objects.all()
    gallary = features_gallay.objects.all()
    jgal = {'header':header, 'gallary':gallary ,'info': info}
    
    return render(request, 'gallary.html', jgal )

def events(request):
    info = home_info.objects.all()
    header = cover.objects.all()
    shows = show.objects.all()
    htm = {'header':header,'shows':shows  ,'info': info}
    
    return render(request, 'events.html', htm )



def contacts(request):
    info = home_info.objects.all()
    header = cover.objects.all()
    htm1 = {'header':header,  'info': info}
    
    
    return render(request, 'contact.html', htm1 )





