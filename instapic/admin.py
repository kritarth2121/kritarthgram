from django.contrib import admin
from .models import User,Photo,PhotoLikes,Followers,PhotoTag

admin.site.register(User)
admin.site.register(PhotoTag)

admin.site.register(PhotoLikes)

admin.site.register(Photo)
admin.site.register(Followers)



