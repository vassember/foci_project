from app.models import Meccs,Csapat,Eredmeny
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Sum
# Create your views here.

def index(request):
	m = Meccs.objects.all()
	er = Eredmeny.objects.all()
	cs=Csapat.objects.all()
	szum = Eredmeny.objects.values('csapat__name').annotate(dsum=Sum('pont')).order_by('-dsum')
	return render_to_response('index.html', {'szum':szum,'er':er,'m':m,'cs':cs},
		context_instance=RequestContext(request))	
	
