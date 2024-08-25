from django.contrib import admin
from .models import Users,AdminT,Channel,CV,Skill,UserEducation,UserPersonalInfo,WorkExperience,LanguageCv

# Register your models here.
admin.site.register(Users)
admin.site.register(AdminT)
admin.site.register(Channel)
admin.site.register(CV)
admin.site.register(Skill)
admin.site.register(UserEducation)
admin.site.register(UserPersonalInfo)
admin.site.register(WorkExperience)
admin.site.register(LanguageCv)