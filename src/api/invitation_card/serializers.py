from rest_framework import serializers
from src.apps.invitation_card.models import (
    Invitation, HostDetails, EventDetails, MessageDetails
)


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostDetails
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageDetails
        fields = '__all__'


class InvitationSerializer(serializers.ModelSerializer):
    host = HostSerializer()
    event = EventSerializer()
    message = MessageSerializer()

    class Meta:
        model = Invitation
        fields = '__all__'

    def create(self, validated_data):
        # GET DATA
        host = validated_data.pop('host')
        event = validated_data.pop('event')
        message = validated_data.pop('message')
        user = validated_data.pop('user')

        # POST DATA

        host, _ = HostDetails.objects.get_or_create(**host)
        event, _ = EventDetails.objects.get_or_create(**event)
        message, _ = MessageDetails.objects.get_or_create(**message)
        invitation,_ = Invitation.objects.get_or_create(user = user,host=host , event=event, message=message)

        invitation = Invitation.objects.create(
            user=user,
            host=host,
            event=event,
            message=message

        )

        return invitation

    def update(self, instance, validated_data):
        host_data = validated_data.pop('host')
        event_data = validated_data.pop('event')
        message_data = validated_data.pop('message')

        host_serializer = self.fields['host']
        event_serializer = self.fields['event']
        message_serializer = self.fields['message']

        # Update nested fields
        host_instance = host_serializer.update(instance.host, host_data)
        event_instance = event_serializer.update(instance.event, event_data)
        message_instance = message_serializer.update(instance.message, message_data)

        # Update remaining fields
        instance.host = host_instance
        instance.event = event_instance
        instance.message = message_instance
        instance.save()

        return instance


    def delete(self, instance):
        instance.delete()


    def get_cv_resumes(self, user_id):
        invitation = Invitation.objects.filter(user_id=user_id)
        serialized_data = self.__class__(invitation, many=True).data
        return serialized_data





class DownloadInvitationCardSerializer(serializers.Serializer):
    cv_resume_id = serializers.IntegerField(required=True)
    template_id = serializers.IntegerField(required=True)
