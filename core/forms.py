from django import forms
from .models import Ticket, Comment, Attachment
from django.contrib.auth.models import User

class TicketForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Ticket
        fields = ['project', 'title', 'status', 'assignees']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']
