from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Balance(models.Model):
    balance = models.DecimalField(verbose_name='Saldo', max_digits=100, decimal_places=2)




class Common(models.Model):
    timeCreate = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    cpf = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, verbose_name='Senha')
    picture = models.ImageField(upload_to='uploads', verbose_name='Imagem')
    age = models.IntegerField(verbose_name='Idade')

    rate = models.IntegerField(verbose_name='Avaliação', blank=True, null=True)
    balance = models.OneToOneField(Balance, verbose_name='Saldo', on_delete=models.CASCADE, blank=True, null=True)
    history = models.ManyToManyField("Ride", blank=True, verbose_name="Historico")
    
    class Meta():
        abstract = True

    def __str__(self):
        return f'{self.user}'

class Motorcycle(models.Model):
    model = models.CharField(max_length=100, verbose_name='Modelo')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    color = models.CharField(max_length=100, verbose_name='Cor')
    year = models.IntegerField(verbose_name='Ano')
    picture = models.ImageField(upload_to='uploads')


class MotoTaxi(Common):
    cnh = models.IntegerField()
    status = models.BooleanField(default=False)
    motorcycle = models.OneToOneField(Motorcycle, on_delete=models.CASCADE, verbose_name='Nome')

    def CreateRate(self,tittle, text, rating, client):

        rate = Rating.objects.create(tittle = tittle, text = text, rating = rating, moto = self, client = client, owner = "Moto Taxi: " + self.name + " - " + str(self.cpf))
        rate.save()

class Client(Common):
    Favorite = models.ManyToManyField(MotoTaxi, verbose_name="Favoritos", blank=True)

    def AddFavorite(self,MotoTaxi):
        self.Favorite.add(MotoTaxi)

    def CreateRate(self,tittle, text, rating, moto):

        rate = Rating.objects.create(tittle = tittle, text = text, rating = rating, moto = moto, client = self, owner = "Cliente: " + self.name + " - " + str(self.cpf))
        rate.save()

    def CreateRide(self, value, distance, paymente, motoTax, start, end):
        ride = Ride.objects.create(value = value, distance = distance, paymente = paymente, motoTax = motoTax, cliente = self, start = start, end = end)
        ride.save()

        self.history.add(ride)
        motoTax.history.add(ride)


class Rating(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    text = models.TextField()
    rating = models.DecimalField(verbose_name='Nota', max_digits=100, decimal_places=2)
    moto = models.ForeignKey(MotoTaxi, verbose_name='Perfil', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Cliente")
    owner = models.CharField(max_length=150, verbose_name="Autor", blank=True)

class Ride(models.Model):
    value = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Valor')
    distance = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Distância')
    payment = models.CharField(verbose_name='Pagamento', max_length=100)
    motoTax = models.ForeignKey(MotoTaxi, on_delete=models.PROTECT,verbose_name="Moto Taxi")
    clinte = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Cliente")
    start = models.CharField(max_length=300, verbose_name="Começo")
    end = models.CharField(max_length=300, verbose_name="Chegada")