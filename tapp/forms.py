from django import  forms
from .models import add
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','username','phone','rollnumber''backlogs','resume','gender','year','branch','section')

    def clean_password1(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
class  StudentRegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password1(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords don't match")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.active=True
        user.staff=False
        if commit:
            user.save()
        return user

class TeacherRegisterForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
       model = User
       fields = ('email','username','gender','phone',)

    def clean_password1(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords don't match")
        return password

    def clean_email(self):
       email = self.cleaned_data.get('email')
       qs = User.objects.filter(email=email)
       if qs.exists():
           raise forms.ValidationError("email is taken")
       return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(TeacherRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.active=True
        user.staff=True
        if commit:
            user.save()
        return user


class addForm(forms.ModelForm):
    class Meta:
        model=add
        fields=('subject','deficulty','question','Option1','Option2','Option3','Option4','option')

    def clean_add(self, *args, **kwargs):
        #run the standard clean method first
        inputdata = self.cleaned_data.get('add')
        print('validating form')


        return inputdata
