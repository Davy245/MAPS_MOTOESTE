from django.contrib import admin
from .models import *
from users.models import *

# Register your models here.

admin.site.register(MotoTaxi)
admin.site.register(Client)
admin.site.register(Motorcycle)
admin.site.register(Ride)
admin.site.register(Balance)
admin.site.register(Rating)

