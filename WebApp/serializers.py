from django.contrib.auth.models import User
from rest_framework import serializers
from WebApp.models import ProjectHire, ProjectDeveloper, Language, Roll, Developer


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language_name']


class ProjectHireSerializer1(serializers.ModelSerializer):
    project_language = serializers.StringRelatedField(
        many=True, read_only=True)  # LanguageSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = ProjectHire
        fields = ['user', 'project_name', 'project_start_date',
                  'project_end_date', 'project_language']


class ProjectDeveloperSerializer(serializers.ModelSerializer):
    project_name = serializers.ReadOnlyField(source='project_hire.project_name')
    role = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ProjectDeveloper
        #fields = '__all__'
        #fields  = ['id','project_hire','developer','star_date','end_date','role']
        fields = ['project_name', 'star_date', 'end_date', 'role']


class ProjectHireSerializer2(serializers.ModelSerializer):
    project_language = serializers.StringRelatedField(
        many=True, read_only=True)  # LanguageSerializer(many=True)
    # developer_record = serializers.StringRelatedField(many=True,read_only=True)   # Working Properly
    #user = serializers.ReadOnlyField(source='user.first_name')
    developer_record = ProjectDeveloperSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectHire
        #fields = ['id','user','project_name','project_country','project_start_date','project_end_date','project_language','developer_record']
        fields = ['project_name', 'project_country', 'project_start_date',
                  'project_end_date', 'project_language', 'developer_record']


class UserSerializer(serializers.ModelSerializer):
    developer = ProjectDeveloperSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = '__all__'


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

from django.db.models import Q
class UserProjectDetailViewSerializer(serializers.ModelSerializer):
    langauge_ = serializers.SerializerMethodField()
    project_hire_ = serializers.SerializerMethodField()
    project_worked_ = serializers.SerializerMethodField()
    project_working = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'username', 'langauge_', 'project_hire_','project_worked_','project_working']

    def get_langauge_(self, obj):
        developer = Developer.objects.filter(developer_name__id=obj.id).first()
        if developer:
                return developer.developer_language.all().values_list('language_name', flat=True)
        return ''

    def get_project_hire_(self,obj):
        project = ProjectHire.objects.filter(user__id=obj.id)
        if project:
            return project.values_list('project_name', flat=True)
        return []
    
    def get_project_worked_(self,obj):
        project = ProjectDeveloper.objects.filter(~Q(end_date=None),developer__developer_name__id=obj.id)
        if project:
            # project_w_l = []
            # project_w_d = {}
            # project_w_d['proejct_name'] = project.project_hire.project_name
            # project_w_d['stat_date'] = project.star_date
            # project_w_d['end_date'] = project.end_date
            # project_w_l.append(project_w_d)
            return ProjectDeveloperSerializer(project,many=True).data
        return []
        
    def get_project_working(self,obj):
        project = ProjectDeveloper.objects.filter(Q(end_date=None),developer__developer_name__id=obj.id)
        if project:
            return ProjectDeveloperSerializer(project,many=True).data
        return []
      
      
      
      
      
      
      
      
      
      
      
        
    

    # def to_representation(self,instance):
    #     data = super(ProjectDeveloperSerializer2,self).to_representation(instance)

    #    # data['developer'] = instance.developer.developer_name.first_name
    #     lang = instance.developer.developer_language.all()
    #     lang_l = set()
    #     for l in lang:
    #         lang_l.add(l.language_name)
    #     print(list(lang_l))
    #     data['language'] = lang_l
    #     if instance.end_date !=None:
    #         project_work=[]
    #         project_w_d={}
    #         #print(instance.end_date)
    #         project_w_d['project_name'] =instance.project_hire.project_name
    #         project_w_d['start_date'] =instance.star_date
    #         project_w_d['end_date'] =instance.end_date
    #         project_work.append(project_w_d)
    #         #print(project_work)
    #         data['project_worked'] = project_work
    #         role = instance.role.all()
    #         role_l=[]
    #         for r in role:
    #             role_l.append(r.roll_name)
    #             #print(r.roll_name)
    #         #print(role_l)
    #         project_w_d['role'] = role_l

    #     else:
    #         project_working = []
    #         project_working_d ={}
    #         project_working_d['project_name'] =instance.project_hire.project_name
    #         project_working_d['start_date'] =instance.star_date
    #         project_working.append(project_working_d)

    #        # print("Project_working",project_working)
    #         data['project_working']=project_working
    #         role = instance.role.all()
    #         role_l=[]
    #         for r in role:
    #             role_l.append(r.roll_name)
    #             #print(r.roll_name)
    #         #print(role_l)
    #         project_working_d['role'] = role_l
    #     return data
