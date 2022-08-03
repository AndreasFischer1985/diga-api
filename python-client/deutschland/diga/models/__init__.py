# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.diga.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.diga.model.digadetails import Digadetails
from deutschland.diga.model.digadetails_meta import DigadetailsMeta
from deutschland.diga.model.digalist import Digalist
from deutschland.diga.model.digalist_data_inner import DigalistDataInner
from deutschland.diga.model.digalist_included_inner import DigalistIncludedInner
from deutschland.diga.model.digalist_meta import DigalistMeta
from deutschland.diga.model.digaprescription import Digaprescription
from deutschland.diga.model.digaprescription_data_inner import DigaprescriptionDataInner
from deutschland.diga.model.digaprescription_meta import DigaprescriptionMeta
