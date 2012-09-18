# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from concepts.models import Player

def displayBattlefield(request):
  return render(request, "displayBattlefield.html", {'players':Player.objects.all()})
  #return HttpResponse("die in a fire")
