from django.contrib import admin

from .models import User, Photo, Party, PartyPhoto, Message, Willingness

admin.site.register(Photo)
admin.site.register(Party)
admin.site.register(PartyPhoto)
admin.site.register(Message)
admin.site.register(Willingness)
