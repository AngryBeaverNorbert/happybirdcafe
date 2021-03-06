from django.shortcuts import render, get_object_or_404, redirect
from .models import YourFeeder
from .forms import YourFeederForm

# Create your views here.


def feeders_type(request):
    your_feeders_types = YourFeeder.objects.all()
    return render(request, 'your_feeders/feeders_type.html',
                  {'your_feeders_types': your_feeders_types})


def feeders_type_details(request, your_feeder_id):
    your_feeders_types = get_object_or_404(YourFeeder, id=your_feeder_id)
    your_feeders_type_detail = get_object_or_404(YourFeeder, id=your_feeder_id)
    return render(request, 'your_feeders/feeders_type_detail.html',
                  {'your_feeders_types': your_feeders_types,
                   'your_feeders_type_detail': your_feeders_type_detail})


def new_feeder(request):
    # your_feeders_types = get_object_or_404(YourFeeder, id=your_feeder_id)
    # your_feeders_type_detail = get_object_or_404(YourFeeder, id=your_feeder_id)
    if request.method == "POST":
        form = YourFeederForm(request.POST)
        if form.is_valid():
            feeder = form.save()
            # post.author = request.user
            feeder.save()
            return redirect('your_feeders:feeders_type_details', your_feeder_id=feeder.id)
        # return render(request, 'your_feeders/feeders_type_detail.html',
        #               {'your_feeders_types': your_feeders_types,
        #                'your_feeders_type_detail': your_feeders_type_detail}
        #               )
    else:
        form = YourFeederForm()
    return render(request, 'your_feeders/new_feeder.html', {'form': form})
