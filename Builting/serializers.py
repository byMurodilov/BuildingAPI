from rest_framework import serializers
from .models import Hudud, Qurilishtashkiloti, Qurilishbinosi

class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'

class QurilishtashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurilishtashkiloti
        fields = '__all__'

class QurilishbinosiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurilishbinosi
        fields = '__all__'
