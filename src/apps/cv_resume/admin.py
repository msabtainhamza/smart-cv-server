from django.contrib import admin
from .models import (Language, PersonalLanguage, PersonalInfo, WorkExperience
, Skill, CVSkill, CVResume, Certification, Education,ProfilePhoto)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number']
    search_fields = ['full_name', 'email']
    list_filter = ['full_name', 'email']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(PersonalLanguage)
class PersonalLanguageAdmin(admin.ModelAdmin):
    list_display = ['personal_info', 'language']


# WORK EXPERIENCE

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'responsibilities']

    # EDUCATION


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



# CERTIFICATION

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

# SKILL


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CVSkill)
class CVSkillAdmin(admin.ModelAdmin):
    list_display = ['skill']
    search_fields = ['skill']

@admin.register(ProfilePhoto)
class CVSkillAdmin(admin.ModelAdmin):
    list_display = ['profile_pic']
    search_fields = ['profile_pic']

# CV RESUME
@admin.register(CVResume)
class CVResumeAdmin(admin.ModelAdmin):
    list_display = ['personal_info','id']
    search_fields = ['personal_info','id']
