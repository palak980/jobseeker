from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response





#GetSkills
class SkillsCreate(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = skillserializers
class SkillsList(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = skillserializers
class SkillsUpdate(generics.UpdateAPIView):
    queryset = Skills.objects.all()
    serializer_class = skillserializers

@api_view(['GET'])
def GetSkillsCreate(request):
    request.method == 'GET'
    snippets = Skills.objects.all()
    serializer = skillserializers(snippets, many=True)
    return Response(serializer.data)


#GetCandidateDetails
class CDetailCreate(generics.ListCreateAPIView):
    queryset = CandidateDetail.objects.all()
    serializer_class = CDetailserializers

@api_view(['GET'])
def GetCDetails(request):
    request.method == 'GET'
    snippets = CandidateDetail.objects.all()
    serializer = CDetailserializers(snippets, many=True)
    return Response(serializer.data)


#Education
class EDetailCreate(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EDetailserializers
class EDetailupdate(generics.RetrieveUpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EDetailserializers

@api_view(['GET'])
def GetEDetails(request):
    request.method == 'GET'
    snippets = Education.objects.all()
    serializer = EDetailserializers(snippets, many=True)
    return Response(serializer.data)


#Professional
class PDetailCreate(generics.ListCreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = PDetailserializers
class PDetailupdate(generics.UpdateAPIView):
    queryset = Professional.objects.all()
    serializer_class = PDetailserializers

@api_view(['GET'])
def GetPDetails(request):
    request.method == 'GET'
    snippets = Professional.objects.all()
    serializer = PDetailserializers(snippets, many=True)
    return Response(serializer.data)


#JobDetails
class JDetailCreate(generics.ListCreateAPIView):
    queryset = JobDetails.objects.all()
    serializer_class = JDetailserializers

@api_view(['GET'])

def GetJobDetails(request):
    request.method == 'GET'
    snippets = JobDetails.objects.all()
    serializer = JDetailserializers(snippets, many=True)
    return Response(serializer.data)


#JobSearch
class JobSearch(generics.ListCreateAPIView):
    queryset = JobDetails.objects.all()
    serializer_class = JDetailserializers
    filter_backends = [SearchFilter]
    search_fields = ['Location','JobProfile']


#applyjobs
class ApplyJCreate(generics.ListCreateAPIView):
    queryset = ApplyJobs.objects.all()
    serializer_class = ApplyJserializers


#SaveCandidate
class SaveCCreate(generics.ListCreateAPIView):
    queryset = SaveCandidate.objects.all()
    serializer_class = SaveCserializers


#GetResponse
class PostRCreate(generics.ListCreateAPIView):
    queryset = PostResponse.objects.all()
    serializer_class = PostRserializers

@api_view(['GET'])
def GetResponse(request):
    request.method == 'GET'
    snippets = PostResponse.objects.all()
    serializer = PostRserializers(snippets, many=True)
    return Response(serializer.data)



