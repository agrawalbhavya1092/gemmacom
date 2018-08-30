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




class MyView(LoginRequiredMixin,GroupRequiredMixin,CalendarMixin, DetailView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        calendar = self.object
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

        local_timezone = timezone.get_current_timezone()
        period = period_class(event_list, date, tzinfo=local_timezone)

        context.update({
            'date': date,
            'period': period,
            'calendar': calendar,
            'weekday_names': weekday_names,
            'here': quote(self.request.get_full_path()),
        })
        return context