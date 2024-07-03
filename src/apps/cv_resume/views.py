import os.path

import requests
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import Template
from django.views.generic import TemplateView

from smart_cv_server.settings import BASE_DIR, model
from src.apps.cv_resume.forms import CVResumeForm
from src.apps.cv_resume.models import Certification, CVResume, CVSkill, WorkExperience, Education, PersonalInfo


class PersonalInfoView(TemplateView):
    template_name = 'cv_resume.html'

    def get_context_data(self):
        context = super(PersonalInfoView, self).get_context_data()
        context['form'] = CVResumeForm

        return context

    def post(self, request, *args, **kwargs):
        form = CVResumeForm(request.POST)
        if form.is_valid():
            # Save the form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            date_of_birth = form.cleaned_data['date_of_birth']
            nationality = form.cleaned_data['nationality']
            education_name = form.cleaned_data['education_name']
            field_of_study = form.cleaned_data['field_of_study']
            institute = form.cleaned_data['institute']
            location = form.cleaned_data['location']
            graduation_year = form.cleaned_data['graduation_year']
            company = form.cleaned_data['company']
            position = form.cleaned_data['position']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            responsibilities = form.cleaned_data['responsibilities']
            certification_name = form.cleaned_data['certification_name']
            issuer_name = form.cleaned_data['issuer_name']
            certification_date = form.cleaned_data['certification_date']
            skills = form.cleaned_data['skills']
            user = request.user
            # Save PersonalInfo
            personal_info, create = PersonalInfo.objects.get_or_create(
                user=user,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                address=address,
                date_of_birth=date_of_birth,
                nationality=nationality
            )

            # Save Education
            education, create = Education.objects.get_or_create(
                name=education_name,
                field_of_study=field_of_study,
                institute=institute,
                location=location,
                graduation_year=graduation_year
            )

            # Save WorkExperience
            work_experience, create = WorkExperience.objects.get_or_create(
                company=company,
                position=position,
                start_date=start_date,
                end_date=end_date,
                responsibilities=responsibilities
            )

            # Save Certification
            certification, create = Certification.objects.get_or_create(
                name=certification_name,
                issuer_name=issuer_name,
                date=certification_date
            )

            # Save CVResume
            cv_resume, create = CVResume.objects.get_or_create(
                personal_info=personal_info,
                education=education,
                workExperience=work_experience,
                certification=certification
            )

            # Save Skills
            for skill in skills:
                cv_skill = CVSkill.objects.create(skill=skill, cv_resume=cv_resume)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            return HttpResponseRedirect('Not Submitted')


from django.views.generic import TemplateView


class CVResumeView(TemplateView):
    def get_template_names(self):

        template_type = self.kwargs.get('template_type', 'default')
        return [f'cv_resumes/{template_type}.html']

    def dispatch(self, request, *args, **kwargs):
        self.request = request  # Save the request object
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        _id = self.kwargs['id']
        template_type = self.kwargs['template_type']
        cv_resume = get_object_or_404(CVResume, id=_id)
        body = model.generate(gen_for='cv', type=template_type, object=cv_resume)
        cv_resume.body = body
        context = super().get_context_data(**kwargs)

        profile_ = cv_resume.prifile_picture.profile_pic.url if cv_resume.prifile_picture else None
        profile_pic_url = self.request.build_absolute_uri(profile_) if profile_ else None
        context['cv_resume'] = cv_resume
        context['profile_pic_url'] = profile_pic_url

        style_file = os.path.join(BASE_DIR, 'static', 'css', 'required', f'{template_type}.css')
        context['style_file'] = style_file

        return context