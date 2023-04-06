from django.contrib import admin
from WebApp.models import ProjectHire,Language,Roll,ProjectDeveloper,Developer
# Register your models here.
import csv
from django.http import HttpResponse
admin.site.register(Language)

admin.site.register(Roll)

class ProjectDeveloperModelAdmin(admin.ModelAdmin):
   # list_display =['project_hire','developer','star_date','end_date',]@admin.action
    def export_to_csv(self, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mymodel.csv"'

        # Create the CSV writer
        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['ID', 'project_hire_Name', 'developer Name','Roll_List','star_date'])
        writer.writerow(["====================================================================="])

        # Write the data rows
        for obj in queryset:
            writer.writerow([obj.id,obj.project_hire, obj.developer,[role.roll_name for role in obj.role.all()], obj.star_date,obj.end_date])
        writer.writerow(["====================================================================="])

        # Return the response
        return response
   
    exclude = ['is_soft_deleted','is_complete']
    actions = [export_to_csv]
admin.site.register(ProjectDeveloper,ProjectDeveloperModelAdmin)


class ProjectHireModelAdmin(admin.ModelAdmin):
    exclude = ['is_soft_deleted','is_complete']  
admin.site.register(ProjectHire,ProjectHireModelAdmin)

class DeveloperModelAdmin(admin.ModelAdmin):
    exclude = ['is_soft_deleted','is_complete']
admin.site.register(Developer,DeveloperModelAdmin)

    

