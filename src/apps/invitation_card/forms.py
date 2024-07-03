from urllib import request

from django import forms
from django.core.exceptions import ValidationError

from .models import (HostDetails, Invitation, EventDetails, MessageDetails)


class HostDetailForm(forms.ModelForm):
    class Meta:
        model = HostDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HostDetailForm, self).__init__(*args, **kwargs)

        self.fields['hostname'] = forms.CharField(label='Name', widget=forms.TextInput(

            attrs={'class': 'form-control', 'placeholder': 'Enter Host Name', 'required': True}
        ))

        self.fields['host_email'] = forms.EmailField(label='Email', widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Host Email', 'type': 'email'}
        ))

        self.fields['host_phone_number'] = forms.CharField(label='Phone Number', widget=forms.NumberInput(
            attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter Host Phone Number'}
        ))
        self.fields['host_address'] = forms.CharField(label='Address', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Host Address'}
        ))


class EventDetailForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventDetailForm, self).__init__()
        self.fields['event_type'] = forms.CharField(label='Event Type', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Event Type'}

        ))
        self.fields['event_date'] = forms.DateField(label='Event Date', widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ))
        self.fields['event_time'] = forms.TimeField(label='Event Time', widget=forms.TimeInput(
            attrs={'class': 'form-control', 'type': 'time'}
        ))
        self.fields['event_location'] = forms.CharField(label='Event Location', widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Event Location'}
        ))


class MessageDetailForm(forms.ModelForm):
    class Meta:
        model = MessageDetails
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MessageDetailForm, self).__init__(*args, **kwargs)
        self.fields['message'] = forms.CharField(label='Message', widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Enter Message'}
        ))


class CombinedForm(forms.Form):
    host_detail_form = HostDetailForm()
    event_detail_form = EventDetailForm()
    message_detail_form = MessageDetailForm()

    def save(self, request, *args, **kwargs):
        host_detail, create = HostDetails.objects.get_or_create(
            hostname=self.data['hostname'],
            host_email=self.data['host_email'],
            host_phone_number=self.data['host_phone_number'],
            host_address=self.data['host_address'],

        )

        event_detail, create = EventDetails.objects.get_or_create(
            event_type=self.data['event_type'],
            event_date=self.data['event_date'],
            event_time=self.data['event_time'],
            event_location=self.data['event_location'],

        )
        message_detail, create = MessageDetails.objects.get_or_create(
            message=self.data['message']
        )

        invitation_card, create = Invitation.objects.get_or_create(
            user=request.user,
            event=event_detail,
            host=host_detail,
            message=message_detail
        )

        return invitation_card
