from django import forms
from .models import Person  # Corrected the import to match Python naming conventions

class PersonForm(forms.ModelForm):  # Corrected the class name to follow PascalCase naming convention
    class Meta:
        model = Person  # Corrected the model name to match Python naming conventions
        fields = ['name', 'age']