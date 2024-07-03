from django.contrib import admin
from .models import (Invitation, HostDetails, EventDetails, MessageDetails)


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('event', 'host','id')
    search_fields = ('event', 'host')


@admin.register(HostDetails)
class HostDetailsAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'host_phone_number')
    search_fields = ['hostname']


@admin.register(EventDetails)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'event_date', 'event_time', 'event_location')
    search_fields = ('event_type', 'event_date', 'event_time', 'event_location')


@admin.register(MessageDetails)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ['message']
    search_fields = ['message']
