# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
import json


# Create your views here.
def citas(request):
    return render(request, 'citas/cita.html', {})
	
	
def nueva_cita(request):

	categoria = request.GET.get("categoria")
	
	r = requests.get("http://quotes.rest/qod.json?category="+categoria)
	d = json.loads(r.content)
	
	
	
	author = d["contents"]["quotes"][0]["author"]
	quote = d["contents"]["quotes"][0]["quote"]
	copyright = d["contents"]["copyright"]
	
	
	
	
	#author=str(d)#
	#quote="el conocimiento es poder"#
	#copyright="sufrutamadre"#
	context = {'author': author,'quote':quote,'copyright':copyright,}
	return render(request, 'citas/cita.html', context)