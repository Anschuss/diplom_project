from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View

from .models import TenderDoc


class StatusDetailMixin(SingleObjectMixin):
    STATUS_TENDER = {
        "completed": "Завершон",
        "in_developing": "В разработке",
    }
