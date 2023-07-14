#from cProfile import Profile
from urllib import response
from django.db import models
#from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.core.validators import FileExtensionValidator



#GetSkills
class Skills(models.Model):

    Non_Tech_Skill = models.TextField(max_length=100,default='') 
    Tech_Skill = models.TextField(max_length=100,default='') 
    Description = models.TextField(max_length=100,default='')
    Non_Tech_Skill = models.TextField(max_length=100,default='') 
    Description = models.TextField(max_length=100,default='')
    Experience = models.IntegerField()

    class Meta:
        verbose_name_plural = "Skills"

#GetCandidateDetails
class CandidateDetail(models.Model):
    name=models.TextField(max_length=255)
    date_of_birth = models.DateField()
    Genderchoice=([('Male','Male'),('Female','Femail')])
    Gender=models.TextField(choices=Genderchoice,max_length=20,blank=True)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')   
    #phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    phone_number = models.IntegerField(blank=True)
    Email=models.EmailField()
    Address=models.CharField(max_length=255)
    PinCode=models.IntegerField()
    City=models.TextField(max_length=255)
    catagoryChoice=([('OBc','OBc'),('general','general'),('SC/ST','SC/ST')])
    catagory=models.TextField(choices=catagoryChoice,max_length=20,blank=True)
    Languages=models.CharField(max_length=255)
    workPermit=models.CharField(max_length=255)

    def __str__(self):
        #return self.title
        return self.name


#Education
class Education(models.Model):
    HighSchool=models.CharField(max_length=255)
    HighSchoolPassout=models.IntegerField()
    Intermediate=models.CharField(max_length=255)
    IntermediatePassout=models.IntegerField()
    Degree_or_Diploma=models.CharField(max_length=255)
    Course=models.TextField(max_length=255)
    Branch=models.TextField(max_length=255)
    Passout=models.IntegerField(validators=[MinValueValidator(2019), MaxValueValidator(2023)])
    Projects=models.CharField(max_length=255)


    def __str__(self):
        #return self.title
        return self.Degree_or_Diploma


#professional
class Professional(models.Model):
    CurrentIndustry=models.CharField(max_length=255,blank=True)
    CurrentDepartment=models.CharField(max_length=255,blank=True)
    CurrentRoleCatagory=models.CharField(max_length=255,blank=True)
    CurrentJobRole=models.CharField(max_length=255,blank=True)
    Experience=models.IntegerField(blank=True)
    CurrentCTC=models.IntegerField(blank=True)
    Profile=models.CharField(max_length=255)
    Languages=models.CharField(max_length=255)
    Certification=models.FileField(upload_to='uploads/documents/',null=True,blank=True,validators=[FileExtensionValidator( ['pdf','.doc','docx'])])
    CertificationLink=models.URLField(max_length=5000,blank=True)
    PaperPublished=models.CharField(max_length=255,blank=True)
    PaperPublishedLink=models.URLField(max_length=5000,blank=True)
    PreferredJobRole=models.CharField(max_length=255)
    PreferredCTC=models.CharField(max_length=255)
    PreferredShift=models.CharField(max_length=255)


    def __str__(self):
        #return self.title
        return self.Profile


#JobDetails
class JobDetails(models.Model):
    CompanyName=models.CharField(max_length=255)
    JobProfile=models.CharField(max_length=255)
    Experience=models.IntegerField()
    Oppening=models.IntegerField()
    KeySkills=models.CharField(max_length=255)
    Qualification=models.CharField(max_length=255)
    Salary=models.IntegerField()
    JobDescription=models.CharField(max_length=255)
    Location=models.CharField(max_length=255)
    LastDate=models.DateField()
    IndustryType=models.CharField(max_length=255)
    EmployementType=models.CharField(max_length=255)


    def __str__(self):
        #return self.title
        return self.JobProfile


#Apply Jobs
class ApplyJobs(models.Model):
    apply1=models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    apply2=models.ForeignKey(Education,on_delete=models.CASCADE)
    apply3=models.ForeignKey(Professional,on_delete=models.CASCADE)
    apply4=models.ForeignKey(JobDetails,on_delete=models.CASCADE)


#SaveCandidate
class SaveCandidate(models.Model):
    Save1=models.ForeignKey(CandidateDetail,on_delete=models.CASCADE)
    Save2=models.ForeignKey(Education,on_delete=models.CASCADE)
    Save3=models.ForeignKey(Professional,on_delete=models.CASCADE)


#PostResponse
class PostResponse(models.Model):
    choice=([('applied','applied'),('application viewed','application viewed'),('resume viewed','resume viewed')])
    Response=models.TextField(choices=choice,max_length=20,blank=True)

#candidte login
class register(models.Model):
	name=models.CharField(max_length=50)
	email= models.EmailField()
	pass1=models.CharField(max_length=8)
	contact=models.IntegerField(null=True)
	workstatus=models.CharField(max_length=20,null=False)
	resume= models.FileField(upload_to='documents')
	def __str__(self):
		return self.name



