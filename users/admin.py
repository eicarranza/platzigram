
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    # list_display admin option, is a tuple of field names to display, 
    # as columns, on the change list page for the object
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user', )
    list_editable = ('phone_number', 'website', 'picture')

    # search_fields: habilita un campo de busqueda para encontrar
    # coincidencias con los campos indicados en los parentesis
    search_fields = (
        'user__email', 
        'user__first_name', 
        'user__last_name', 
        'phone_number'
    )

    # list_filter: muestra en el costado derecho, la columna
    # con las opciones de filtro que pueden ser usadas
    list_filter = [
        'created', 
        'modified',
        'user__is_active',
        'user__is_staff'
    ]

    # fieldsets agrupa los campos mostrados en la interfaz admin,
    # de acuerdo con el titulo que le pongamos, en este ejemplo
    # los campos user y picture estaran en la seccion fieldsets
    fieldsets = (
        ('Profile', {
            'fields': (
                'user', 'picture',
            )
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified')
            )
        })
    )

    # Muestra las variables del parentesis en pantalla, 
    # como no editables
    readonly_fields = ('created', 'modified', 'user')


class ProfileInLine(admin.StackedInline):
    """ 
        Create a profile admin interface with 
        user admin interface on the same page
     """
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    """ Adds profile admin to base user admin """
    inlines = (ProfileInLine, )
    list_display = (
        'username',
        'email', 
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)