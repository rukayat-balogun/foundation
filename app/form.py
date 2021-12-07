from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django import forms

class applicantSignUpForm(UserCreationForm):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Surname"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("First Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_lenght=50)), label=("Email Address"))
    phone_number = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=15)), label=("Phone Number"))


    def _init_(self, *args, **kwargs):
        super(UserCreationForm, self)._init_(*args, **kwargs)

        for fieldname in [ 'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check and raise error if other user already exists with given email
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return email
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

    


    @transaction.atomic
    def save(self):
        user= super().save(commit=False)
        user.is_applicant = True
        user.save()
        #applicant = PersonalDetails.objects.create(user=user)
        phone_number = self.cleaned_data.get('phone_number')
        newapplicant = PersonalDetails.objects.create(user=user, phone_number=phone_number)
        newapplicant.save()
        return user


class subAdminSignUpForm(UserCreationForm):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Username"), error_messages={ 'invalid': ("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("Surname"))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=("First Name"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password (again)"))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_lenght=50)), label=("Email Address"))
    phone_number = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=15)), label=("Phone Number"))


    def _init_(self, *args, **kwargs):
        super(UserCreationForm, self)._init_(*args, **kwargs)

        for fieldname in [ 'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try another one."))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # check and raise error if other user already exists with given email
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this email")
        return email
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user= super().save(commit=False)
        user.is_subadmin = True
        user.active = False
        user.save()
        phone_number = self.cleaned_data.get('phone_number')
        subAdmin = PersonalDetails.objects.create(user=user, phone_number=phone_number)
        subAdmin.save()