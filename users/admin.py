
# Django
from django.contrib import admin

# Models
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