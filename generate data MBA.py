import random
import faker
import csv
from datetime import datetime, timedelta

# Gerador de dados falsos
fake = faker.Faker()

# Função para gerar uma data aleatória dentro do intervalo
def generate_random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Definindo intervalo de datas
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Gerando um conjunto fixo de 100 nomes e associando a um telefone único
unique_customers = {fake.phone_number(): fake.name() for _ in range(100)}

# Gerando o arquivo com visitas, garantindo que nomes e telefones sejam únicos e se repitam
data = []
for phone, name in unique_customers.items():
    # Quantidade aleatória de visitas para cada nome/telefone entre 1 e 10
    num_visits = random.randint(1, 10)
    
    for _ in range(num_visits):
        visit_date = generate_random_date(start_date, end_date).strftime('%Y-%m-%d')
        data.append([name, phone, visit_date])

# Criando o arquivo CSV
with open('visitas_estabelecimento.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome', 'Telefone', 'Data de Ida ao Estabelecimento'])
    writer.writerows(data)

print("Arquivo CSV 'visitas_estabelecimento.csv' gerado com sucesso!")