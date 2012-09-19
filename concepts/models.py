from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    picurl = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    permanents = models.ManyToManyField(Card,through='BitOfCardboard')
    def __unicode__(self):
        return self.name
    
class BitOfCardboard(models.Model):
    player = models.ForeignKey(Player)
    card = models.ForeignKey(Card)
    quatity = models.IntegerField(default=1)
    def __unicode__(self):
        return self.player.name + "'s " + self.card.name + "(s)"
