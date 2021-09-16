from django import forms

from meetings.models import Room


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'floor_num', 'room_num']

    name = forms.CharField(max_length=200)
    floor_num = forms.IntegerField()
    room_num = forms.IntegerField()

    def clean(self):
        cleaned_data = super(RoomForm, self).clean()
        name = cleaned_data.get('name')
        floor_num = cleaned_data.get('floor_num')
        room_num = cleaned_data.get('room_num')
        if not name and not floor_num and not room_num:
            raise forms.ValidationError('You have to write something!')