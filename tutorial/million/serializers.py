from rest_framework import serializers
from million.models import *
class Sex_Serialiazer(serializers.ModelSerializer):
    class Meta:
        model=Sex
        fields=('sex_name',)
