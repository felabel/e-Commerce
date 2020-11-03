from django import forms
# making sure that there are no two users
from django.contrib.auth import get_user_model
User = get_user_model()
 
class ContactForm(forms.Form):
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control","id": "form_full_name",
                "placeholder": "your full name"
                })
                )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control","id": "form_full_name",
                "placeholder": "your email"
                })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": 'form-control',"placeholder": "your message", "rows":"5", "cols":"15"
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

# class LoginForm(forms.Form):
#     username = forms.CharField(label="username")
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             "input_type": "password"
#         }
#     ))
# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control","id": "form_full_name",
#                 "placeholder": "your email"
#                 })
#     )
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             "input_type": "password"
#         }
#     ))
#     password2 = forms.CharField(
#         label = 'confirm password',
#         widget=forms.PasswordInput(
#         attrs={
#             "input_type": "password"
#         }
#     ))

#     # code to avoid users with the same username and email
#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("username is already taken")
#         return(username)

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email  already exists")
#         return(email)

#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get("password")
#         password2 = self.cleaned_data.get("password2")
#         if password2 != password:
#             raise forms.ValidationError("passwords must match")
#             return data

    
