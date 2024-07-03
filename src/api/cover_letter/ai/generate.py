class CoverLetterGenAI:
    def generate_cover_letter_body(self, cover_letter):
        job_title = cover_letter.job_title
        company_name = cover_letter.company_name
        body_content = f"""
        I am writing to express my interest in the {job_title} position at {company_name},. 
        With a strong background .I am confident in my ability to contribute effectively to your team.
        I believe will be valuable in the {job_title} position.
        Thank you for considering my application. I am looking forward to the opportunity to discuss how my background, skills, and enthusiasms align with the needs of {company_name}.
        """
        return body_content
