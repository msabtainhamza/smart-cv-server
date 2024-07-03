from rest_framework import serializers

from src.apps.cover_letter.models import CoverLetter


class CoverLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoverLetter
        fields = '__all__'
        read_only_fields = ['user']





