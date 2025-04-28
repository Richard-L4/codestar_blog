from django import forms
from .models import Comment
from allauth.account.forms import SignupForm

# Blog comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email (optional)"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password (again)"

        # Replace password help texts with simple safe text
        self.fields['password1'].help_text = (
            "Your password must be at least 8 characters and not entirely numeric."
        )
        self.fields['password2'].help_text = "Enter the same password again to verify."


        
     
