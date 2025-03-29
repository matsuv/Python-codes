import random
import faker
import csv
from datetime import datetime, timedelta

# Inicializa o gerador de dados falsos
fake = faker.Faker('pt_BR')

# Função para gerar um telefone no formato brasileiro, garantindo unicidade
def gerar_telefone_brasileiro(existentes):
    while True:
        ddd = random.randint(11, 99)  # DDDs variam de 11 a 99
        numero = random.randint(900000000, 999999999)  # Formato 9XXXX-XXXX
        telefone = f"({ddd}) {str(numero)[:5]}-{str(numero)[5:]}"
        if telefone not in existentes:
            return telefone

# Função para gerar uma data aleatória em 2024
def gerar_data_aleatoria():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Gerando um conjunto fixo de 100 clientes únicos
clientes = {}
while len(clientes) < 100:
    telefone = gerar_telefone_brasileiro(clientes)
    clientes[telefone] = fake.name()

# Gerando múltiplas visitas para cada cliente
data = []
for phone, name in clientes.items():
    num_visits = random.randint(2, 20)  # Cada cliente pode ter de 1 a 10 visitas
    for _ in range(num_visits):
        visit_date = gerar_data_aleatoria().strftime('%Y-%m-%d')
        data.append([name, phone, visit_date])

# Criando o arquivo CSV
with open("visitas_estabelecimento.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Telefone", "Data de Ida ao Estabelecimento"])
    writer.writerows(data)

print("Arquivo 'visitas_estabelecimento.csv' gerado com sucesso!")
