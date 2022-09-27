from django.shortcuts import render, get_object_or_404
from django_admin_geomap import geomap_context
# Create your views here.
from .models import Kpps, Reports
from django.db.models import Avg


def showmap(request):
    posts = Kpps.objects.all()
    geomap = geomap_context(
        Kpps.objects.all(),
        map_zoom=6,
        map_longitude='64.430557',
        map_latitude='50.148239',
        map_height="1000px")
    context = {'posts': posts}
    # appenddicts = geomap | context  # Соединяем два дикта - контекст меток на карте и контекст значений
    appenddicts = {**geomap, **context}
    return render(request, 'views/block.html', appenddicts)


def showkpp(request, pk):
    report = Reports.objects.filter(kpp=pk)
    lastreports = Reports.objects.filter(kpp=pk).order_by('-id')[:3:1]
    avgttw = Reports.objects.filter(kpp=pk).aggregate(ttw=Avg('ttw'))
    avgttw = avgttw['ttw']
    avgttw = round(avgttw, 1)
    carcount = Reports.objects.filter(kpp=pk).aggregate(cars=Avg('carcount'))
    carcount = carcount['cars']
    carcount = int(carcount)
    pcount = Reports.objects.filter(kpp=pk).aggregate(people=Avg('pcount'))
    pcount = pcount['people']
    pcount = int(pcount)
    post = get_object_or_404(Kpps, id=pk)
    context = (
        {
            'report': report,
            'lastreports': lastreports,
            'post': post,
            'avgttw': avgttw,
            'carcount': carcount,
            'pcount': pcount,
        }
    )
    return render(request, 'views/postblock.html', context)