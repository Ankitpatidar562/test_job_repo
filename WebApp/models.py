from django.db import models
from django_countries.fields import CountryField
# Create your models here.
from django.contrib.auth.models import User
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)
    is_soft_deleted =models.BooleanField(default=False)
    
    class Meta:
        abstract = True

    
class Language(models.Model):
    language_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.language_name}"
        
class ProjectHire(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_user')
    project_name = models.CharField(max_length=200)
    project_country = CountryField()
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    project_language = models.ManyToManyField(Language)
    reason = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        project_language = ",".join(str(p_l) for p_l in self.project_language.all())
        return f"{self.user.first_name} - {self.project_name}-{project_language}"

class Developer(BaseModel):
    developer_name = models.ForeignKey(User,on_delete=models.CASCADE) 
    developer_language = models.ManyToManyField(Language)  
    def __str__(self) -> str:
        return f"{self.developer_name.first_name}"

class Roll(models.Model):
    roll_name = models.CharField(max_length=200) 
    def __str__(self) -> str:
        return f"{self.roll_name}"

class ProjectDeveloper(BaseModel):
    project_hire = models.ForeignKey(ProjectHire,on_delete=models.CASCADE,related_name='developer_record')
    developer = models.ForeignKey(Developer,on_delete=models.CASCADE, related_name='developer')
    star_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    role = models.ManyToManyField(Roll,related_name='role_r_name')
    
    def __str__(self) -> str:
        role_list = ", ".join(str(role_name) for role_name in self.role.all() )
        return f"{self.developer.developer_name.first_name} - {self.star_date} -{self.end_date} -{role_list}"
    
        # roll_list = ", ".join(str(role_name) for role_name in self.role.all())
        # return "{}-{}".format(roll_list)
    
    