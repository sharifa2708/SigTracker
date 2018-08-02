from django.contrib import admin
from . models import Sig
from . models import DevSig
from . models import MlSig
from . models import CpSig

admin.site.register(Sig)
admin.site.register(DevSig)
admin.site.register(MlSig)
admin.site.register(CpSig)