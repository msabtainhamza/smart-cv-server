from django.db import models
from smart_cv_server import settings

User = settings.AUTH_USER_MODEL

# PERSONAL INFORMATION
class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProfilePhoto(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    @property
    def profile_pic_url(self):
        if self.profile_pic:
            return '{}{}'.format(settings.MEDIA_URL, self.profile_pic)
        return None

class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100,blank=True,null=True)
    date_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language, through="PersonalLanguage")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'personal_info'
        ordering = ('-created_at',)

    def __str__(self):
        return self.full_name


class PersonalLanguage(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.personal_info.full_name


# WORK EXPERIENCE


class WorkExperience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    responsibilities = models.CharField(max_length=50)

    def __str__(self):
        return self.responsibilities


# SKILLS

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# EDUCATION

class Education(models.Model):
    name = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    graduation_year = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# CERTIFICATION AND AWARD

class Certification(models.Model):
    name = models.CharField(max_length=50)
    issuer_name = models.CharField(max_length=50)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# CVRESUME


class CVResume(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, through='CVSkill')
    prifile_picture = models.ForeignKey(ProfilePhoto,on_delete=models.CASCADE,null=True,blank=True)
    body = models.TextField(blank=True,null=True)



    def __str__(self):
        return self.personal_info.full_name


class CVSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    cv_resume = models.ForeignKey(CVResume, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill.name
