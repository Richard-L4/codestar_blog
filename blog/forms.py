"""Forms for blog comments and custom signup form for user registration."""

from django import forms
from .models import Comment
from allauth.account.forms import SignupForm
from django.contrib.auth import password_validation


class CommentForm(forms.ModelForm):
    """
    Form for users to submit a comment.

    This form is linked to the Comment model and allows users
    to input their comment body.
    """

    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    """
    Custom signup form to override default labels and format password help text as a list.

    - Changes field labels for username, email, and passwords.
    - Formats password help texts using line breaks and dashes instead of <ul>/<li>.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the form, customize field labels, and generate formatted help texts."""
        super().__init__(*args, **kwargs)

        # Customize field labels
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email (optional)"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Password (again)"

        # Fetch password validators' help texts
        password_help_texts = password_validation.password_validators_help_texts()

        # Format help texts as a safe list (dash + line break)
        formatted_help_text = ""
        for text in password_help_texts:
            formatted_help_text += f"• {text}<br>"

        # Set the help text
        self.fields['password1'].help_text = formatted_help_text

        # Set a simple help text for password confirmation
        self.fields['password2'].help_text = "Enter the same password again to verify."
from django import forms
from allauth.account.forms import SignupForm
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Password 1 help text (manual bullet list with <p>)
        self.fields['password1'].help_text = (
            '<p>&bull; Your password must be at least 8 characters long.</p>'
            '<p>&bull; It must not be entirely numeric.</p>'
            '<p>&bull; It must not be a commonly used password.</p>'
            '<p>&bull; It must not be too similar to your personal information.</p>'
        )

        # Password 2 help text
        self.fields['password2'].help_text = (
            '<p>Please enter the same password again for verification.</p>'
        )
