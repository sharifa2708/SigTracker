from . models import Sig, DevSig
from django.shortcuts import render
from django.http import Http404

from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class index(TemplateView):
    template_name = "index.html"

class dev_sig(TemplateView):
    template_name = "dev_sig.html"

class ml_sig(TemplateView):
    template_name = "ml_sig.html"

class cp_sig(TemplateView):
    template_name = "cp_sig.html"