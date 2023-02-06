from django.db import models
import abc

# Create your models here.
class Balance(models.Model):
    balance = models.DecimalField(verbose_name='Saldo', max_digits=100, decimal_places=2)
    


class Profile(models.Model, abc.ABC):
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.IntegerField()
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100, verbose_name='Senha')
    picture = models.ImageField(upload_to='uploads', verbose_name='Imagem')
    age = models.IntegerField(verbose_name='Idade')
    rating = models.IntegerField(verbose_name='Avaliação')
    balance = models.OneToOneField(Balance, verbose_name='Saldo', on_delete=models.CASCADE)


class Motorcycle(models.Model):
    model = models.CharField(max_length=100, verbose_name='Modelo')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    color = models.CharField(max_length=100, verbose_name='Cor')
    year = models.DateField(verbose_name='Ano')
    picture = models.ImageField(upload_to='uploads')

class MotoTaxi(Profile, models.Model):
    cnh = models.IntegerField()
    status = models.BooleanField(default=False)
    motorcycle = models.OneToOneField(Motorcycle, on_delete=models.CASCADE, verbose_name='Nome')


class Rating(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    text = models.TextField()
    rating = models.DecimalField(verbose_name='Nota', max_digits=100, decimal_places=2)
    profile = models.ForeignKey(Profile, verbose_name='Perfil')


class Ride(models.Model):
    value = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Valor')
    distance = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Distância')
    payment = models.CharField(verbose_name='Pagamento')
