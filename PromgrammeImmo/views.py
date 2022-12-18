from django.shortcuts import render

# Create your views here.

from PromgrammeImmo.models import Programme, Appartement, Caracteristique
from PromgrammeImmo.serializers import ProgrammeSerializer, AppartementSerializer, CaracteristiqueSerializer
from rest_framework import viewsets
from django.db.models import Q

class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer

class AppartementViewSet(viewsets.ModelViewSet):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer
    lookup_field = 'description'
class CaracteristiqueViewSet(viewsets.ModelViewSet):
    queryset = Caracteristique.objects.all()
    serializer_class = CaracteristiqueSerializer
def getAppartProgActif():
    queryset=Appartement.objects.filter(Programme__actif=True)

def getAppartprix():
    queryset=Appartement.objects.filter(Q(prix__lte=180000) , Q(prix__gte=100000)).values()

def getProgrammesPiscine():
    queryset=Appartement.objects.filter(caracrirestique_description="piscine").values_list('Id_programme').Desctinct()
def getApparts(code=""):
    if code=="PERE NOEL":
        queryset=Appartement.objects.annotate(prix_bas=(F('prix')+(F('prix')*5)/100)).annotate(libilleprogramme=F('Id_programme')+'PROMO SPECIALE')
def getseasonToday():
    doy = datetime.today().timetuple().tm_yday
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
        queryset=Appartement.objects.annotate(ski=Case(when(caracrirestique_description="proche de                   ski",Then=True),Default=False)).order_by('ski','-prix','-surface').values()
    elif getseasonToday()=='summer':
        queryset=Appartement.objects.annotate(piscine=Case(when(caracrirestique_description="piscine",Then=True),Default=False)).order_by('piscine','-prix','-surface').values()
    else:
        queryset=Appartement.objects.all().order_by('piscine','-prix','-surface').values()
        
        
    
                                        

