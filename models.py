from __future__ import unicode_literals
#from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


GAME_STATUS_CHOICES=(
    ('F','First player to move'),
    ('S','Second player to move'),
    ('W','First player wins'),
    ('L','Second player wins'),
    ('D','Draw')
)

class GameQuerySet(models.QuerySet):
    def games_for_user(self,user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )
    def active(self,user):
        return self.filter(
            Q(status='F')|Q(status='S')
        )


#@python_2_unicode_compatible
class Game(models.Model):
    first_player=models.ForeignKey(User,on_delete=models.CASCADE,related_name="games_first_user")
    second_player=models.ForeignKey(User,on_delete=models.CASCADE,related_name="games_second_user")
    starttime=models.DateTimeField(auto_now_add=True)
    lastactive=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,default='F',choices=GAME_STATUS_CHOICES)
    objects= GameQuerySet.as_manager()    #wrting custom manager for our class

    def __str__(self):
        return "{0} vs {1}".format(self.first_player,self.second_player)

class Move(models.Model):
    x=models.IntegerField()
    y=models.IntegerField()
    comment=models.CharField(max_length=300, blank=True)
    by_first_player=models.BooleanField()
    game=models.ForeignKey(Game,on_delete=models.CASCADE)