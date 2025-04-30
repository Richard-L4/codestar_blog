from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    View to display the 'About Me' page and
    handle collaboration form submissions.

    GET:
        - Retrieves the most recently updated About instance.
        - Displays an empty collaboration form.

    POST:
        - Validates and saves the collaboration request form.
        - Displays a success message on successful submission.

    Context:
        about (About): The most recent About object for display.
        collaborate_form (CollaborateForm):
        The collaboration request form (either empty or with submitted data).
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received!
                I endeavour to respond within 2 working days."
            )

    # Get the most recent About object based on update date
    about = About.objects.all().order_by('-updated_on').first()

    # Always return a fresh empty form in the context (even after POST)
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
