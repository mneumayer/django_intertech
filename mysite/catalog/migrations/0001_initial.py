# Generated by Django 2.0.7 on 2018-07-23 13:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.PositiveIntegerField(help_text='project number', verbose_name='project number')),
                ('customer', models.TextField(help_text='customer', max_length=60, verbose_name='customer')),
                ('quantity', models.PositiveIntegerField(help_text='quantity', verbose_name='quantity')),
                ('part_description', models.TextField(help_text='part description', max_length=30, verbose_name='part description')),
                ('pt_fs', models.TextField(help_text='pressure transducer full scale', max_length=30, verbose_name='pressure transducer full scale')),
                ('test_pressure', models.TextField(help_text='test pressure', max_length=30, verbose_name='test pressure')),
                ('bench_test_presure', models.TextField(help_text='bench test pressure', max_length=30, verbose_name='bench test pressure')),
                ('tt_fs', models.TextField(help_text='test transducer full scale', max_length=30, verbose_name='test transducer full scale')),
                ('tt_span', models.TextField(help_text='test transducer span', max_length=30, verbose_name='test transducer span')),
                ('reject_limit', models.TextField(help_text='reject limit', max_length=30, verbose_name='reject limit')),
                ('test_time', models.TextField(help_text='test time', max_length=60, verbose_name='test time')),
                ('program', models.TextField(help_text='program', max_length=60, verbose_name='program')),
                ('special_instructions', models.TextField(help_text='special instructions', max_length=200, verbose_name='special instructions')),
                ('imn', models.TextField(help_text='Instrument model number', max_length=30, verbose_name='Instrument model number')),
                ('gad', models.TextField(help_text='General assembly drawing', max_length=30, verbose_name='General assembly drawing')),
                ('ppl', models.TextField(help_text='Pneumatic parts list', max_length=30, verbose_name='Pneumatic parts list')),
                ('fha', models.TextField(help_text='Flow head assembly', max_length=30, verbose_name='Flow head assembly')),
                ('epl', models.TextField(help_text='Electrical parts list', max_length=30, verbose_name='Electrical parts list')),
                ('cba', models.TextField(help_text='Control board assembly', max_length=30, verbose_name='Control board assembly')),
                ('e', models.TextField(help_text='Enclosure', max_length=30, verbose_name='Customer Name')),
                ('sist', models.TextField(help_text='Slide-in strips, tapped', max_length=30, verbose_name='Slide-in strips, tapped')),
                ('mk', models.TextField(help_text='Mounting kit', max_length=30, verbose_name='Mounting kit')),
                ('pma', models.TextField(help_text='Panel mounting adapter', max_length=30, verbose_name='Panel mounting adapter')),
                ('rpsp', models.TextField(help_text='Rear panel sub-plate', max_length=30, verbose_name='Rear panel sub-plate')),
                ('rpmd', models.TextField(help_text='Rear panel machining detail', max_length=30, verbose_name='Rear panel machining detail')),
                ('rppasd', models.TextField(help_text='Rear panel paint and silkscreen detail', max_length=30, verbose_name='Rear panel paint and silkscreen detail')),
                ('fpmd', models.TextField(help_text='Front panel machining detail', max_length=30, verbose_name='Front panel machining detail')),
                ('fppasd', models.TextField(help_text='Front panel paint and silkscreen detail', max_length=30, verbose_name='Front panel paint and silkscreen detail')),
                ('instrument_created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Released_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.TextField(help_text='Instrument number', max_length=30, verbose_name='Instrument number')),
                ('imn', models.TextField(help_text='Instrument model number', max_length=30, verbose_name='Instrument model number')),
                ('gad', models.TextField(help_text='General assembly drawing', max_length=30, verbose_name='General assembly drawing')),
                ('ppl', models.TextField(help_text='Pneumatic parts list', max_length=30, verbose_name='Pneumatic parts list')),
                ('fha', models.TextField(help_text='Flow head assembly', max_length=30, verbose_name='Flow head assembly')),
                ('epl', models.TextField(help_text='Electrical parts list', max_length=30, verbose_name='Electrical parts list')),
                ('cba', models.TextField(help_text='Control board assembly', max_length=30, verbose_name='Control board assembly')),
                ('e', models.TextField(help_text='Enclosure', max_length=30, verbose_name='Customer Name')),
                ('sist', models.TextField(help_text='Slide-in strips, tapped', max_length=30, verbose_name='Slide-in strips, tapped')),
                ('mk', models.TextField(help_text='Mounting kit', max_length=30, verbose_name='Mounting kit')),
                ('pma', models.TextField(help_text='Panel mounting adapter', max_length=30, verbose_name='Panel mounting adapter')),
                ('rpsp', models.TextField(help_text='Rear panel sub-plate', max_length=30, verbose_name='Rear panel sub-plate')),
                ('rpmd', models.TextField(help_text='Rear panel machining detail', max_length=30, verbose_name='Rear panel machining detail')),
                ('rppasd', models.TextField(help_text='Rear panel paint and silkscreen detail', max_length=30, verbose_name='Rear panel paint and silkscreen detail')),
                ('fpmd', models.TextField(help_text='Front panel machining detail', max_length=30, verbose_name='Front panel machining detail')),
                ('fppasd', models.TextField(help_text='Front panel paint and silkscreen detail', max_length=30, verbose_name='Front panel paint and silkscreen detail')),
                ('instrument_created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='bom',
            name='inn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Instrument'),
        ),
    ]
