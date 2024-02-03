from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#id (primary key - automático) 
#nome, sobrenome telefone
# email, data de criação, descrição (texto)

#category (forein key), show(boolean), owner(forein key) 
class Category(models.Model):
    #Mudar o nome da categoria la no admin do django
    class Meta:
        verbose_name = "Categoria"
    
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name   

class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = "Contatos"
        
    #campo de texto comum
    first_name = models.CharField(max_length = 50)
    #campo de texto comum
    last_name = models.CharField(max_length=50,
                                blank=True)
    #campo de telefone em formato de texto comum
    phone = models.CharField(max_length=20)
    #campo de email
    email = models.EmailField(max_length=254,
                            blank=True)
    #data de criação do cadastro
    created_date = models.DateTimeField(default=timezone.now)
    #descrição do usuário cadastrado
    description = models.TextField(blank=True)
    #mostrar ou não um determinado campo
    show = models.BooleanField(default=True)
    #adiciona um campo de adição de imagem
    #cria a pasta pictures e salva o arquivo dentro com ano e mês de adição
    picture = models.ImageField(blank=True,
                                upload_to='pictures/%Y/%m')
    #Categoria com foreign key
    category = models.ForeignKey(Category,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True
                                )
    owner = models.ForeignKey(User,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True
                                )
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'