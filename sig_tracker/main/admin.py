from django.contrib import admin
from . models import Sig
<<<<<<< HEAD
from . models import Topics

admin.site.register(Sig)
admin.site.register(Topics)
=======
from . models import DevSig
from . models import MlSig
from . models import CpSig

admin.site.register(Sig)
admin.site.register(DevSig)
admin.site.register(MlSig)
admin.site.register(CpSig)
>>>>>>> 531244f4fc50a5f7af58a82ab52f9b5d7eb22c68
