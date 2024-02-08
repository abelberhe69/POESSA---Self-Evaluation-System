from django import forms
from .models import *

class የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_form(forms.ModelForm):
    class Meta:
        model = የ6ወር_ስኮርካርድ_እቅድ_ቅፅ_model
        fields = '__all__'
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_form(forms.ModelForm):
    class Meta:
        model = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_1_model
        fields = '__all__'
    
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_form(forms.ModelForm):
    class Meta:
        model = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_2_model
        fields = '__all__'
    
class የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_form(forms.ModelForm):
    class Meta:
        model = የ6ወር_የባህሪ_መመዘኛ_ቅፅ_3_model
        fields = '__all__'
    
class የድርጊት_መርሃ_ግብር_ቅፅ_form(forms.ModelForm):
    class Meta:
        model = የድርጊት_መርሃ_ግብር_ቅፅ_model
        fields = '__all__'