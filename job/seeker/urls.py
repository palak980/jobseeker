from django.urls import URLPattern, path
from .views  import *
from seeker import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[



    #GetSkill
    path('Skills/',views.SkillsCreate.as_view(),  name='skill_post'),
    path('Skillslist/',views.SkillsList.as_view(),  name='skill_list'),
    path('Skillupdate/<int:pk>',views.SkillsUpdate.as_view(),  name='skill_update'),
    path('GetSkillsDetail/', views.GetSkillsCreate),

    #GetCandidateDetails
    path('CandidateDetail/',views.CDetailCreate.as_view(),  name='candidatedetail'),
    path('GetPersonalDetail/', views.GetCDetails),

    #Education
    path('EducationDetail/',views.EDetailCreate.as_view(),  name='candidatedetail'),
    path('EducationDetailUpdate/<int:pk>',views.EDetailupdate.as_view(),  name='EducationDetail_update'),
    path('GetEducationalDetail/', views.GetEDetails),

    #Professional
    path('ProfessionalDetail/',views.PDetailCreate.as_view(),  name='candidateProfessionaldetail'),
    path('ProfessionalDetailUpdate/<int:pk>',views.PDetailupdate.as_view(),  name='candidateProfessionaldetailUpdate'),
    path('GetProfessionalDetail/', views.GetPDetails),


    #JobDetails
    path('JobsDetail/',views.JDetailCreate.as_view(),  name='Jobdetail'),
    path('GetJobsDetail/', views.GetJobDetails),


    #SearchJobs
    path('JobSearch/',views.JobSearch.as_view(),  name='JobSearch'),

    #applyjobs
    path('ApplyJobs/',views.ApplyJCreate.as_view(),  name='ApplyJobs'),

    #SaveCandidate
    path('SaveCandidate/',views.SaveCCreate.as_view(),  name='SaveCandidate'),

    #GetResponse
    path('PostResponse/',views.PostRCreate.as_view(),  name='PostResponse'),
    path('GetResponse/', views.GetResponse),

]