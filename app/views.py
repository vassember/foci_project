from app.models import Meccs,Csapat,Eredmeny
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
	er=Eredmeny.objects.all()
	return render_to_response('index.html', {'er':er},
		context_instance=RequestContext(request))


