from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Poll, Poll_choice, User_poll_choice, Article, Article_Image, Event, Event_register, Document

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confurmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("name", "surname", "second_name", "avatar", "date_of_birth", "phone","pubnet", "university",
                  "course", "reg_address", "cur_address", "organizations", "hobby", "is_active", "is_admin",)

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "name", "surname", "second_name", "avatar", "date_of_birth", "phone", "pubnet", "university",
                    "course", "reg_address", "cur_address", "organizations", "hobby", "is_admin",)
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {'fields' : ("email", "password",)}),
        ("Personal info", {'fields' : ("name", "surname", "second_name", "avatar", "date_of_birth", "phone","pubnet", "university",
                                       "course", "reg_address", "cur_address", "organizations", "hobby",)}),
        ("Permissions", {'fields' : ("is_admin",)})
    )

    add_fieldsets = (
        (None, {
            'classes' : ("wide",),
            'fields' : ("email", "password1", "password2"),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.register(Poll)
admin.site.register(Poll_choice)
admin.site.register(User_poll_choice)

admin.site.register(Article)
admin.site.register(Article_Image)

admin.site.register(Event)
admin.site.register(Event_register)

admin.site.register(Document)

admin.site.unregister(Group)

# Register your models here.
