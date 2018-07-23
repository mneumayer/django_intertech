from django import forms
from .models import Instrument, Bom


class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        fields = ('inn',)
        # fields = ('inn','imn','gad','ppl','fha','epl','cba','e','sist','mk','pma','rpsp','rpmd','rppasd','fpmd','fppasd',)


class BomForm(forms.ModelForm):

    class Meta:
        model = Bom
        fields = ('project_number', 'instrument')
        # fields = ('project_number', 'customer', 'quanity', 'part_description', 'pt_fs', 'test_pressure',
        #'bench_test_pressure','tt_fs', 'tt_span', 'reject_limit', 'test_time', 'program', 'special_instructions',
        #