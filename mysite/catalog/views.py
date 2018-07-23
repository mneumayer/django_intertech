from django.shortcuts import render, get_object_or_404
from .models import Instrument, Bom
from .forms import InstrumentForm, BomForm
from django.shortcuts import redirect
from django.utils import timezone


# Main Page_____________________________________________________________________________________________________________


def index(request):
    # Generate counts of Instruments
    num_instruments = Instrument.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    instruments = Instrument.objects.all()
    # all objects in the Instrument database
    num_boms = Bom.objects.all().count()
    boms = Bom.objects.all()

    return render(request, 'index.html',
                  {'num_instruments': num_instruments, 'instruments': instruments, 'num_boms': num_boms, 'boms': boms})


# New Instrument________________________________________________________________________________________________________


def instrument_detail(request, pk):
    instrument_post = get_object_or_404(Instrument, pk=pk)
    number = pk
    return render(request, 'instrument_detail.html', {'instrument_post': instrument_post}, number)


def instrument_edit(request, pk):
    instrument = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        instrument_form = InstrumentForm(request.POST, instance=post)
        if instrument_form.is_valid():
            instrument_post = instrument_form.save(commit=False)
            instrument_post.published_date = timezone.now()
            instrument_post.save()
            return redirect('instrument_detail', pk=instrument_post.pk)
    else:
        instrument_form = InstrumentForm(instance=instrument)
    return render(request, 'instrument_edit.html', {'form': instrument_form})


def instrument_new(request):
    if request.method == "POST":
        instrument_form = InstrumentForm(request.POST)
        if instrument_form.is_valid():
            instrument_post = instrument_form.save(commit=False)
            instrument_post.published_date = timezone.now()
            instrument_post.save()
            return redirect('instrument_detail', pk=instrument_post.pk)
    else:
        instrument_form = InstrumentForm()
    return render(request, 'instrument_edit.html', {'instrument_form': instrument_form})


# New Bom_______________________________________________________________________________________________________________


def bom_detail(request, pk):
    bom_post = get_object_or_404(Bom, pk=pk)
    number = pk
    return render(request, 'bom_detail.html', {'bom_post': bom_post}, number)


def bom_edit(request, pk):
    bom = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        bom_form = BomForm(request.POST, instance=post)
        if bom_form.is_valid():
            bom_post = bom_form.save(commit=False)
            bom_post.published_date = timezone.now()
            bom_post.save()
            return redirect('bom_detail', pk=bom_post.pk)
    else:
        bom_form = BomForm(instance=bom)
    return render(request, 'bom_edit.html', {'form': bom_form})


def bom_new(request):
    if request.method == "POST":
        bom_form = BomForm(request.POST)
        if bom_form.is_valid():
            bom_post = bom_form.save(commit=False)
            bom_post.published_date = timezone.now()
            bom_post.save()
            return redirect('bom_detail', pk=bom_post.pk)
    else:
        bom_form = BomForm()
    return render(request, 'bom_edit.html', {'bom_form': bom_form})

# Save To Released table________________________________________________________________________________________________


