from pathlib import Path

import pandas as pd


class Model:
    def generate(self, gen_for=None,type=None,object=None):



        if gen_for=="cover_letter":

            job_title = object.job_title
            company_name = object.company_name
            body_content = f"""
            I am writing to express my interest in the {job_title} position at {company_name},. 
            With a strong background .I am confident in my ability to contribute effectively to your team.
            I believe will be valuable in the {job_title} position.
            Thank you for considering my application. I am looking forward to the opportunity to discuss how my background, skills, and enthusiasms align with the needs of {company_name}.
            """
            return body_content

        elif gen_for =="cv":
            # Accessing related objects through the ManyToMany fields
            skill_list = ", ".join([skill.name for skill in object.skills.all()])
            language_list = ", ".join([language.name for language in object.personal_info.languages.all()])
            certification_name = object.certification.name if object.certification else ""
            # Define the body content using placeholders for dynamic values
            body_content = f"""
            <p>I am a dedicated and driven professional. 
            Throughout my education at {object.education.institute}, I developed a solid foundation in 
            {object.education.field_of_study}, which has been further strengthened by my hands-on experience 
            at {object.work_experience.company}.</p>

            <p>My role as {object.work_experience.position} involved responsibilities such as 
            {object.work_experience.responsibilities}. This experience has equipped me with essential skills 
            like {skill_list}, making me proficient in various aspects of the field.</p>

            <p>I am fluent in {language_list}, which allows me to communicate effectively in diverse environments. 
            My strong analytical and problem-solving skills, coupled with my ability to adapt to new challenges, 
            make me an asset to any team.</p>

            <p>I am committed to continuous learning and professional development, evidenced by my certifications 
            in {certification_name}. I am excited about the opportunity to contribute to a dynamic organization.</p>
            """
            return body_content

    def gen_code(self,template, template_type):
        BASE_DIR = Path(__file__).resolve().parent.parent
        df = pd.read_csv(BASE_DIR/'gen.csv')
        print("READ>>>>>>>>>>>>>>>>>>....................................")
        code = df[(df['Template'] == template) & (df['Type'] == template_type)]['Code'].values
        print("CODE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(code)

        if len(code) > 0:
            return code[0]
        else:
            return None
