from .models import add
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User,'student'.
    list_display = ('email','username','rollnumber','gender','backlogs','resume','phone','section','year','branch','admin',)
    list_filter = ('admin','staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('User info', {'fields': ('username','rollnumber','year','section','branch','backlogs','resume','gender','phone','datejoined')}),
        ('Permissions', {'fields': ('admin','active','staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','rollnumber','phone','gender','backlogs','resume','year','branch','section','datejoined','password','password1')}
        ),
    )
    search_fields = ('email','username','rollnumber','phone',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

class addAdmin(admin.ModelAdmin):
    list_display=['subject','deficulty','question','Option1','Option2','Option3','Option4','option']
admin.site.register(add,addAdmin)
