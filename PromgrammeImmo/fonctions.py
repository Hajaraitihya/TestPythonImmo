from PromgrammeImmo.models import Appartement, Programme,Caracteristique
from django.db.models import Q
from django.db.models import F
from django.db.models import CharField, Value, When, Case
from django.db import models 
from django.db.models.functions import Concat




def getProgramsActif():
    queryset=Appartement.objects.filter(Id_programme__actif=True).values()
    return queryset
def getAppartprix():
    queryset=Appartement.objects.filter(Q(prix__lte=180000) , Q(prix__gte=100000)).values()
    return queryset
def getProgrammesPiscine():
    queryset=Appartement.objects.filter(caracteristiques__description="piscine").values_list('Id_programme','').distinct()
    return queryset
def getApparts(code=""):
    if code=="PERE NOEL":
        queryset=Appartement.objects.annotate(prix_bas=(F('prix')-(F('prix')*5)/100)).annotate(libelle_programme=Concat(F('Id_programme__name'), models.Value('Promo Special '), output_field=CharField())).values()
        return queryset
    else:
        return Appartement.objects.all().values()
def getseasonToday():
    doy = datetime.date.today().timetuple().tm_yday
    # "day of year" ranges for the northern hemisphere
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    # winter = everything else

    if doy in spring:
        season = 'spring'
    elif doy in summer:
        season = 'summer'
    elif doy in fall:
        season = 'fall'
    else:
        season = 'winter'
    return season

def getAppartsParOrdre():
    if getseasonToday()=='winter':
        queryset=Appartement.objects.annotate(ski=Case(When(caracteristiques__description="proche station ski",then=Value(1)),default=Value(2),output_field=models.IntegerField())).order_by('ski','-prix','-surface').values()
        return queryset
    elif getseasonToday()=='summer':
        queryset=Appartement.objects.annotate(piscine=Case(When(caracteristiques__description="piscine",then=Value(1)),default=Value(2),output_field=models.IntegerField())).order_by('piscine','-prix','-surface').values()
        return queryset
    else:
        queryset=Appartement.objects.all().order_by('-prix','-surface').values()
        return queryset
    