from django.forms import ModelForm
from .models import Room


# create room form
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
