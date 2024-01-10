from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display= ['user','email','picture']
 


       



admin.site.register(UserProfile,UserProfileAdmin)



#mansoor1234
## pass :arman12345678

##test11

##pass: sara12345678