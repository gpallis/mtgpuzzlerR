# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from concepts.models import Player

def displayBattlefield(request):
  player = Player.objects.get(name="Dave")
  return render(request, "displayBattlefield.html", {
    'player':player,
    'handWidth':player.permanents.count()*175 + 10,
  })
  #return HttpResponse("die in a fire")
