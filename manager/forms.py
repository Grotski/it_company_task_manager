from django import forms
from django.contrib.auth import get_user_model

# from django.forms.widgets import BootstrapDateTimePickerInput

from manager.models import Task


class TaskForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Task
        fields = "__all__"


# class TaskCreationForm(forms.ModelForm):
#     deadline = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=BootstrapDateTimePickerInput())
#
#     class Meta:
#         model = Task
#         fields = "__all__"
#         fields = ["name", "description", "deadline", "priority", "task_type", "assignees", ]
#         exclude = ["is_completed", ]
#         widgets = {
#             "name": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Enter task name"
#                 }
#             ),
#             "description": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Enter task description",
#                     "id": "exampleFormControlTextarea1",
#                 }
#             ),
#             "priority": forms.Select(
#                 attrs={
#                     "class": "form-control",
#                     "id": "exampleFormControlSelect1",
#                 }
#             ),
#             # "deadline": BootstrapDateTimePickerInput(),
#             "task_type": forms.CheckboxSelectMultiple(
#                 attrs={
#                     "id": "customCheck1",
#                 }
#             ),
#             "assignees": forms.SelectMultiple(
#                 attrs={
#                     "class": "form-control",
#                     "id": "exampleFormControlSelect1",
#                 }
#             )
#         }


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "search . . ",
                "id": "icon-search",
                "type": "text",
            }
        ),
        required=False,
        label=""
    )