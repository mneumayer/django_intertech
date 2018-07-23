from django.shortcuts import render, get_object_or_404
from .models import Instrument, Bom
from .forms import InstrumentForm
from django.shortcuts import redirect
from django.utils import timezone


def index(request):
    # Generate counts of Instruments
    num_instruments = Instrument.objects.all().count()
    # Render the HTML template index.html with the data in the context variable
    instruments = Instrument.objects.all()
    # all objects in the Instrument database
    num_boms = Bom.objects.all().count()
    boms = Bom.objects.all()

    return render(request, 'index.html', {'num_instruments': num_instruments, 'instruments': instruments, 'num_boms': num_boms, 'boms': boms})


def instrument_detail(request, pk):
    post = get_object_or_404(Instrument, pk=pk)
    number = pk
    return render(request, 'instrument_detail.html', {'post': post}, number)


def instrument_edit(request, pk):
    instrument = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = InstrumentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('instrument_detail', pk=post.pk)
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, 'instrument_edit.html', {'form': form})


def instrument_new(request):
    if request.method == "POST":
        form = InstrumentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('instrument_detail', pk=post.pk)
    else:
        form = InstrumentForm()
    return render(request, 'instrument_edit.html', {'form': form})



def bom_detail(request, pk):
    post = get_object_or_404(bom, pk=pk)
    number = pk
    return render(request, 'bom_detail.html', {'post': post}, number)


def bom_edit(request, pk):
    bom = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = BomForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('bom_detail', pk=post.pk)
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, 'bom_edit.html', {'form': form})


def bom_new(request):
    if request.method == "POST":
        form = BomForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('bom_detail', pk=post.pk)
    else:
        form = InstrumentForm()
    return render(request, 'bom_edit.html', {'form': form})
