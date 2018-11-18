from django.contrib import admin
from .models import Game,Move
from django.contrib.auth.models import User
# Register your models here.
#from django.contrib.auth.admin import UserAdmin

#admin.site.register(Game)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display=('id','first_player','second_player','status')
    list_editable=('status',)
   
admin.site.register(Move)
