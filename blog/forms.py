from django import forms
from .models import Comment
from allauth.account.forms import SignupForm

# Blog comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Custom signup form
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Optional: Customize field labels (if you want to)
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email (optional)"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password (again)"

        # Optional: Remove allauth's default <ul><li> help texts if needed
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
