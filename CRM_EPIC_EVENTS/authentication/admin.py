from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Team, Statut
#from .serializers import UserSerializer


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'team')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2','first_name', 'last_name', 'email', 'phone', 'is_staff', 'team'),
        }),
    )
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'team')
    list_filter = ('is_staff', 'team')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'team')
    


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Team)
admin.site.register(Statut)



