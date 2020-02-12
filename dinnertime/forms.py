from django.forms import ModelForm
from .models import MainDish, SideDish


class MainDishForm(ModelForm):
    class Meta:
        model = MainDish
        fields = ['main_course']


class SideDishForm(ModelForm):
    class Meta:
        model = SideDish
        fields = ['side_dish']
