from rest_framework import serializers
from dataclasses import field, fields

from .models import *



#GetSkills
class skillserializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


#GetCandidateDetails
class CDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = CandidateDetail
        fields = '__all__'


#Education
class EDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


#Proffisonal
class PDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'


#JobDetails
class JDetailserializers(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = '__all__'


#applyjobs
class ApplyJserializers(serializers.ModelSerializer):
    class Meta:
        model = ApplyJobs
        fields = '__all__'


#SaveCandidate
class SaveCserializers(serializers.ModelSerializer):
    class Meta:
        model = SaveCandidate
        fields = '__all__'


#PostResponse
class PostRserializers(serializers.ModelSerializer):
    class Meta:
        model = PostResponse
        fields = '__all__'


