from django.db import models
from django.db.models import TextField
from django.utils import timezone


# Create your models here.


class Instrument(models.Model):
    inn = models.TextField('Instrument number', max_length=30, help_text='Instrument number')
    imn = models.TextField('Instrument model number', max_length=30, help_text='Instrument model number')
    gad = models.TextField('General assembly drawing', max_length=30, help_text='General assembly drawing')
    ppl = models.TextField('Pneumatic parts list', max_length=30, help_text='Pneumatic parts list')
    fha = models.TextField('Flow head assembly', max_length=30, help_text='Flow head assembly')
    epl = models.TextField('Electrical parts list', max_length=30, help_text='Electrical parts list')
    cba = models.TextField('Control board assembly', max_length=30, help_text='Control board assembly')
    e = models.TextField('Customer Name', max_length=30, help_text='Enclosure')
    sist = models.TextField('Slide-in strips, tapped', max_length=30, help_text='Slide-in strips, tapped')
    mk = models.TextField('Mounting kit', max_length=30, help_text='Mounting kit')
    pma = models.TextField('Panel mounting adapter', max_length=30, help_text='Panel mounting adapter')
    rpsp = models.TextField('Rear panel sub-plate', max_length=30, help_text='Rear panel sub-plate')
    rpmd = models.TextField('Rear panel machining detail', max_length=30, help_text='Rear panel machining detail')
    rppasd = models.TextField('Rear panel paint and silkscreen detail', max_length=30,
                              help_text='Rear panel paint and silkscreen detail')
    fpmd = models.TextField('Front panel machining detail', max_length=30, help_text='Front panel machining detail')
    fppasd = models.TextField('Front panel paint and silkscreen detail', max_length=30,
                              help_text='Front panel paint and silkscreen detail')
    instrument_created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.inn


class Bom(models.Model):
    project_number = models.CharField(max_length=10)
    customer = models.TextField('customer', max_length=60, help_text='customer')
    quantity = models.CharField(max_length=3)
    part_description = models.TextField('part description', max_length=30, help_text='part description')
    pt_fs = models.TextField('pressure transducer full scale', max_length=30,
                             help_text='pressure transducer full scale')
    test_pressure = models.TextField('test pressure', max_length=30, help_text='test pressure')
    bench_test_pressure = models.TextField('bench test pressure', max_length=30, help_text='bench test pressure')
    tt_fs = models.TextField('test transducer full scale', max_length=30, help_text='test transducer full scale')
    tt_span = models.TextField('test transducer span', max_length=30, help_text='test transducer span')
    reject_limit = models.TextField('reject limit', max_length=30, help_text='reject limit')
    test_time = models.TextField('test time', max_length=60, help_text='test time')
    program = models.TextField('program', max_length=60, help_text='program')
    special_instructions = models.TextField('special instructions', max_length=200, help_text='special instructions')
    instrument = models.ForeignKey(Instrument, models.SET_NULL, blank=True, null=True)
    bom_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.project_number


class Released(models.Model):
    project_number = models.CharField(max_length=10)

