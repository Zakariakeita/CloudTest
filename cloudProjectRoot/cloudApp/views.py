from datetime import datetime
from django.shortcuts import render,redirect
from cloudApp.models import *

# Create your views here.
def dashboard(request):
    context={}
    return render(request,"cloudApp/templates/index.html",context)

def inscription(request):
    partcipants=Participant.objects.all().order_by('dateInscription','nom','prenom')
    context={"participants":partcipants}
    return render(request,"cloudApp/templates/inscription.html",context)

def saveParticipant(request):
    if request.method == "POST":
        nom=request.POST["nom"].upper()
        prenom=request.POST["prenom"].title()
        numero=request.POST["numero"]
        email=request.POST["email"]

        participant= Participant(nom=nom, prenom=prenom, numero=numero,email=email, dateInscription=datetime.now())
        participant.save()
        return redirect('inscription')

def updateParticipant(request, id):
    if request.method == "POST":
        nom=request.POST["nom"].upper()
        prenom=request.POST["prenom"].title()
        numero=request.POST["numero"]
        email=request.POST["email"]
        Participant.objects.filter(id=id).update(nom=nom, prenom=prenom, numero=numero,email=email)
    return redirect('inscription')

def deleteParticipant(request, id):
    Participant.objects.filter(id=id).delete()
    return redirect('inscription')


