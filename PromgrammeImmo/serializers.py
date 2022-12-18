from rest_framework_json_api import serializers
from PromgrammeImmo.models import Appartement, Programme,Caracteristique

class ProgrammeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programme
        fields = ('name', 'actif')
class CaracteristiqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caracteristique
        fields = ('description',)
        lookup_field = 'description'
class AppartementSerializer(serializers.HyperlinkedModelSerializer):
    caracteristiques = CaracteristiqueSerializer(many=True)
    class Meta:
        model = Appartement
        fields = ('prix', 'surface', 'nombre_piece','caracteristiques','Id_programme')
        
        
        





        

