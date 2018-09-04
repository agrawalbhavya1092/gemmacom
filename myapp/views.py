from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from .mixins import GroupRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from schedule.views import *

# Create your views here.
@login_required(login_url='/login/')
def home(request):
	# from django.utils import translation
	# user_language = 'en'
	# translation.activate(user_language)
	# request.session[translation.LANGUAGE_SESSION_KEY] = user_language
	title = _('Welcome to my site')

	return render(request,"index.html",{'title':title})


def load_prevnext_calendar(request,*args,**kwargs):
    calendar = kwargs.get('calendar_slug')
    calendar = Calendar.objects.get(name = calendar)
    print("calendar..........................",calendar)
    period_class = kwargs['period']
    try:
        date = coerce_date_dict(request.GET)
    except ValueError:
        raise Http404
    if date:
        try:
            date = datetime.datetime(**date)
        except ValueError:
            raise Http404
    else:
        date = timezone.now()
    event_list = GET_EVENTS_FUNC(request, calendar)
    my_event_list = GET_MY_EVENTS_FUNC(request, calendar)
    local_timezone = timezone.get_current_timezone()
    period = period_class(event_list, date, tzinfo=local_timezone)
    my_period = period_class(my_event_list, date, tzinfo=local_timezone)

    context.update({
        'date': date,
        'period': period,
        'my_period': my_period,
        'calendar': calendar,
        'weekday_names': weekday_names,
        'here': quote(request.get_full_path()),
    })
    return render(request,'calendar.html',context)

class LoadCalendar(LoginRequiredMixin,GroupRequiredMixin,CalendarMixin, TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super(LoadCalendar, self).get_context_data(**kwargs)
        calendar = self.kwargs.get('calendar_slug')
        calendar = Calendar.objects.get(name = calendar)
        # print("calendar..........................",calendar)
        period_class = self.kwargs['period']
        try:
            date = coerce_date_dict(self.request.GET)
        except ValueError:
            raise Http404
        if date:
            try:
                date = datetime.datetime(**date)
            except ValueError:
                raise Http404
        else:
            date = timezone.now()
        event_list = GET_EVENTS_FUNC(self.request, calendar)
        my_event_list = GET_MY_EVENTS_FUNC(self.request, calendar)
        local_timezone = timezone.get_current_timezone()
        period = period_class(event_list, date, tzinfo=local_timezone)
        my_period = period_class(my_event_list, date, tzinfo=local_timezone)

        context.update({
            'date': date,
            'period': period,
            'my_period': my_period,
            'calendar': calendar,
            'weekday_names': weekday_names,
            'here': quote(self.request.get_full_path()),
        })
        return context

class MyView(LoginRequiredMixin,GroupRequiredMixin,CalendarMixin, DetailView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        calendar = self.object
        print("calendar..........................",calendar)
        period_class = self.kwargs['period']
        try:
            date = coerce_date_dict(self.request.GET)
        except ValueError:
            raise Http404
        if date:
            try:
                date = datetime.datetime(**date)
            except ValueError:
                raise Http404
        else:
            date = timezone.now()
        event_list = GET_EVENTS_FUNC(self.request, calendar)
        my_event_list = GET_MY_EVENTS_FUNC(self.request, calendar)
        local_timezone = timezone.get_current_timezone()
        period = period_class(event_list, date, tzinfo=local_timezone)
        my_period = period_class(my_event_list, date, tzinfo=local_timezone)

        context.update({
            'date': date,
            'period': period,
            'my_period': my_period,
            'calendar': calendar,
            'weekday_names': weekday_names,
            'here': quote(self.request.get_full_path()),
        })
        return context