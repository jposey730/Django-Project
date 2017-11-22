from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from quote.models import Day

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Day.objects.all().order_by("-date"),
                                           template_name="quote/quote.html"))]

