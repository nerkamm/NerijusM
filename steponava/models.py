from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Budas(models.Model):
    """Modelis aprašo medžioklės būdą"""
    name = models.CharField('Medžiojimo būdas', max_length=10, help_text='Įveskite medžiojimo būdą (pvz. tykojant)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Būdas'
        verbose_name_plural = 'Būdai'


class Lapas(models.Model):
    """Modelis aprašo medžioklės lapą"""
    numeris = models.CharField('Numeris', max_length=10)
    vadovas = models.ForeignKey('Vadovas', on_delete=models.SET_NULL, null=True)
    zverys = models.TextField('Aprašymas', max_length=200, help_text='Leidžiami medžioti žvėrys')
    budas = models.ForeignKey('Budas', on_delete=models.SET_NULL, null=True, help_text='Parinkite medžiojimo būdą')

    def __str__(self):
        return self.numeris

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('lapas-detail', args=[str(self.numeris)])

    class Meta:
        verbose_name = 'Lapas'
        verbose_name_plural = 'Lapai'


class LapasInstance(models.Model):
    """Modelis, aprašantis medžioklės lapo būseną"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID')
    lapas = models.ForeignKey('Lapas', on_delete=models.SET_NULL, null=True)
    issued = models.DateField('Išduotas', null=True, blank=True)
    due_valid = models.DateField('Galioja iki', null=True, blank=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('n', 'Naujas'),
        ('i', 'Išduotas'),
        ('p', 'Panaudotas'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='n',
        help_text='Statusas',
    )

    @property
    def is_overdue(self):
        if self.due_valid and date.today() > self.due_valid:
            return True
        return False

    def __str__(self):
        return f'{self.id} ({self.lapas})'

    class Meta:
        verbose_name = 'Išduotas lapas'
        verbose_name_plural = 'Išduoti lapai'


class Vadovas(models.Model):
    """Modelis, aprašantis medžiotoją"""
    first_name = models.CharField('Vardas', max_length=100)
    last_name = models.CharField('Pavardė', max_length=100)
    bilietas = models.CharField('Medžiotojo bilieto numeris', max_length=10)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Vadovas'
        verbose_name_plural = 'Vadovai'

    def __str__(self):
        """Pavardės ir vardo formatavimas eilutėje"""
        return f'{self.last_name} {self.first_name}'


class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="img/NoImageIco.jpg", upload_to="profile_pics")

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'

    def __str__(self):
        return f"{self.user.username} profilis"