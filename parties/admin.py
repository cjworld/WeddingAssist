from django.contrib import admin

from .models import User, Photo, Party, PartyPhoto, Message, ParticipationWillingness

admin.site.register(Photo)
admin.site.register(Party)
admin.site.register(PartyPhoto)
admin.site.register(Message)
admin.site.register(ParticipationWillingness)
