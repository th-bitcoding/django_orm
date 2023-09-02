from rest_framework import serializers
from .models import * 

class MembersSerializers(serializers.ModelSerializer):
    class Meta:
        models = Members
        fields = ['id','group','club','club_members']


class CsvAddApiviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvFile
        fields = ['id','csv_file']