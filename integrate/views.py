from django.views import generic
from django.http import HttpResponse

import json

from .integrate import *

# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'index.html'


def IntegrateView(request):
	function = request.POST.get('input')
	llimit = request.POST.get('min')
	ulimit = request.POST.get('max')
	solution = integrate(function, llimit, ulimit)

	return HttpResponse(solution)
