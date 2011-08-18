from app.models import Meccs,Csapat
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
	mecssek=Meccs.objects.all()
	csapatok=Csapat.objects.all()
	return render_to_response('index.html', {'m': mecssek,'cs':csapatok},
		context_instance=RequestContext(request))


