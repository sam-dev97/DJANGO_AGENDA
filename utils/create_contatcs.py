# Importa o módulo os para interagir com o sistema operacional.
import os

# Importa o módulo sys para configurar o caminho do sistema.
import sys

# Importa a classe datetime do módulo datetime para lidar com datas e horas.
from datetime import datetime

# Importa a classe Path do módulo pathlib para lidar com caminhos de arquivos e diretórios.
from pathlib import Path

# Importa a função choice do módulo random para escolher aleatoriamente um item de uma sequência.
from random import choice

# Importa o framework Django.
import django

# Importa as configurações do Django.
from django.conf import settings

# Obtém o diretório base do projeto Django, assumindo que este script está em um subdiretório.
DJANGO_BASE_DIR = Path(__file__).parent.parent

# Adiciona o diretório base ao caminho do sistema.
sys.path.append(str(DJANGO_BASE_DIR))

# Define o número de objetos a serem criados.
NUMBER_OF_OBJECTS = 1000

# Configura o módulo de configurações do Django para 'project.settings'.
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# Desativa o uso de fuso horário no Django.
settings.USE_TZ = False

# Inicializa o ambiente do Django.
django.setup()

# Verifica se o script está sendo executado como o programa principal.
if __name__ == '__main__':
    # Importa o módulo faker para gerar dados fictícios.
    import faker

    # Importa os modelos Category e Contact da aplicação contact.
    from contact.models import Category, Contact

    # Remove todos os registros da tabela Contact.
    Contact.objects.all().delete()

    # Remove todos os registros da tabela Category.
    Category.objects.all().delete()

    # Inicializa um objeto Faker para gerar dados fictícios em português brasileiro.
    fake = faker.Faker('pt_BR')

    # Lista de categorias predefinidas.
    categories = ['Amigos', 'Família', 'Conhecidos']

    # Cria objetos de modelo Category a partir da lista de categorias.
    django_categories = [Category(name=name) for name in categories]

    # Salva cada objeto de modelo Category no banco de dados.
    for category in django_categories:
        category.save()

    # Lista para armazenar objetos de modelo Contact gerados aleatoriamente.
    django_contacts = []

    # Loop para criar o número especificado de objetos de modelo Contact.
    for _ in range(NUMBER_OF_OBJECTS):
        # Gera um perfil fictício usando o objeto Faker.
        profile = fake.profile()

        # Extrai o endereço de e-mail do perfil gerado.
        email = profile['mail']

        # Divide o nome completo em primeiro e último nome.
        first_name, last_name = profile['name'].split(' ', 1)

        # Gera um número de telefone fictício.
        phone = fake.phone_number()

        # Gera uma data fictícia dentro do ano atual.
        created_date: datetime = fake.date_this_year()

        # Gera uma descrição fictícia com no máximo 100 caracteres.
        description = fake.text(max_nb_chars=100)

        # Escolhe aleatoriamente uma categoria da lista de categorias.
        category = choice(django_categories)

        # Cria um objeto de modelo Contact e o adiciona à lista.
        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    # Verifica se há pelo menos um objeto de modelo Contact na lista.
    if len(django_contacts) > 0:
        # Cria todos os objetos de modelo Contact na base de dados de uma vez.
        Contact.objects.bulk_create(django_contacts)