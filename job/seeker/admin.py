from django.contrib import admin
from  . import models

# Register your models here.



#GetSkills
class SkillsetAdmin(admin.ModelAdmin):
    list_display= ('Tech_Skill', 'Description','Non_Tech_Skill','Description','Experience')
admin.site.register(models.Skills,SkillsetAdmin)

#GetCandidateDetails
class CDetail(admin.ModelAdmin):
    list_display= ('name','date_of_birth','Gender','phone_number','Email','Address','PinCode','City','catagory','Languages','workPermit')
admin.site.register(models.CandidateDetail,CDetail)

#Education
class EDetail(admin.ModelAdmin):
    list_display= ('HighSchool','HighSchoolPassout','Intermediate','IntermediatePassout','Degree_or_Diploma','Course','Branch','Passout','Projects')
admin.site.register(models.Education,EDetail)

#Professional
class PDetail(admin.ModelAdmin):
    list_display= ('CurrentIndustry','CurrentDepartment','CurrentRoleCatagory','CurrentJobRole','Experience','CurrentCTC','Profile','Languages','Certification','CertificationLink','PaperPublished','PaperPublishedLink','PreferredJobRole','PreferredCTC','PreferredShift')
admin.site.register(models.Professional,PDetail)


#JobDetails
class JDetail(admin.ModelAdmin):
    list_display= ('CompanyName','JobProfile','Experience','Oppening','KeySkills','Qualification','Salary','JobDescription','Location','LastDate','IndustryType','EmployementType')
admin.site.register(models.JobDetails,JDetail)


#applyJobs
class ApplyJ(admin.ModelAdmin):
    list_display= ('apply1','apply2','apply3')
admin.site.register(models.ApplyJobs,ApplyJ)


#saveCandidate
class SaveC(admin.ModelAdmin):
    list_display= ('Save1','Save2','Save3')
admin.site.register(models.SaveCandidate,SaveC)


#PostResponse
class PostR(admin.ModelAdmin):
    list_display= ()
admin.site.register(models.PostResponse,PostR)



