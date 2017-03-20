from django.contrib import admin
from .models import ImageModel
from .models import Registration
from .models import Matchlist

# Register your models here.

admin.site.register(ImageModel)

admin.site.register(Registration)

admin.site.register(Matchlist)
