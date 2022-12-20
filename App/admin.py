from django.contrib import admin
from App.models import *
# Register your models here.

class MemberShip(admin.TabularInline):
    model = MembershipInProject
    extra = 0

class SearchEtudiant(admin.ModelAdmin):
    search_fields=['nom']

@admin.register(project)
class projetAdmin(admin.ModelAdmin):
    list_display=("nom_projet","duree_projet","etat","temps_alloue","createur","superviseur")
    fieldsets = (
        ('A propos',{'fields':('nom_projet',)}),
        ('Etat',{'fields':('etat',)}),
        ('Durée',{'fields':('duree_projet','temps_alloue')}),
        (None,{'fields':('createur','superviseur',)})
    )
    inlines = (MemberShip,)
    autocomplete_fields=["createur"]

admin.site.register(etudiant,SearchEtudiant)
# admin.site.register(project,projetAdmin)
admin.site.register(coach)

