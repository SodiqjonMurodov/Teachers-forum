from django.forms import ModelForm
from forum.models import *


class AddPost(ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'
        exclude = ['date']