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
            # existing_data = Members.objects.all()
            # existing_records = {(entry.group, entry.club): entry for entry in existing_data}

            # lst=[]
            Members.objects.all().delete()
            for _, row in readcsv.iterrows():
                group = row['group']
                club = row['club']
                club_members = row['club_members']
                # lst.append(club_members)
                
                Members.objects.create(group=group, club=club, club_members=club_members)

                # Get all existing records that match the criteria
                # existing_records = Members.objects.filter(group=group, club=club,club_members=club_members)

                # if existing_records.exists():
                #     # Update each existing record
                #     for existing_record in existing_records:
                #         existing_record.club_members = club_members

                #         existing_record.save()
                # else:
                #     Members.objects.filter(group=group,club=club).exclude(club_members__in =lst)
                #     # Create a new record if no matching records exist
                #     Members.objects.create(group=group, club=club, club_members=club_members)
                # print('****',lst)

            #     if (group, club) in existing_records:
            #         existing_record = existing_records[(group, club)]
            #         existing_record.club_members = club_members
            #         existing_record.save()
            #     else:
            #         existing_record = Members(
            #             group=group,
            #             club=club,
            #             club_members=club_members,
            #         )
                    
            #         existing_record.save()
            # print('***',existing_record.club_members)
            return Response({"status": "success"},
                        status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
