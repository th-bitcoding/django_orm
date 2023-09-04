from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from rest_framework.views import APIView
import io, csv, pandas as pd
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def create_members(request):
    group_name = Group.objects.get(group_name="B")
    club_member= Members(group = group_name,club = "B2",club_members = "b_B2_Sapna")
    club_member.save()
    return HttpResponse('success')

class CsvData(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = CsvAddApiviewSerializer(data=request.data)
        if serializer.is_valid():
            csv = serializer.validated_data['csv_file']
            readcsv = pd.read_csv(csv)
            lst=[]
            lst2=[]

            for key, row in readcsv.iterrows():
                lst.append({'group':row['group'],'club':row['club'],'club_members':row['club_members']})
                
            data = Members.objects.all()
            for i in data:
                lst2.append({'group':i.group,'club':i.club,'club_members':i.club_members})

            for item in lst:
                if item not in lst2:
                    Members.objects.update_or_create(group=item['group'],club=item['club'],club_members=item['club_members'])
            
            records_to_delete = Members.objects.exclude(
                group__in=[item['group'] for item in lst],
                club__in=[item['club'] for item in lst],
                club_members__in=[item['club_members'] for item in lst]
            )
            records_to_delete.delete()
  
            return Response({"status": "success"},
                        status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


