from django.db import models
from django.utils.translation import gettext_lazy as _

class PaymentType(models.TextChoices):
  CARD = 'card', _('Card')
  CASH = 'cash', _('Cash')

class PaymentStatus(models.TextChoices):
  CANCELLED = 'cancelled', _('Cancelled')
  INPROGRESS = 'inprogress', _('Progress')
  PAID = 'paid', ('Paid')