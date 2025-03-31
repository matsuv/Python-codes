import random
import faker
import csv
from datetime import datetime, timedelta

# Inicializa o gerador de dados falsos no formato brasileiro
fake = faker.Faker('pt_BR')

# Função para gerar um telefone brasileiro único
def gerar_telefone_brasileiro():
    ddd = random.randint(11, 99)
    numero = random.randint(900000000, 999999999)
    return f"({ddd}) {str(numero)[:5]}-{str(numero)[5:]}"

# Definição de categorias de frequência
frequencias = {
    "mensal": 30,
    "quinzenal": 15,
    "semanal": 7,
    "esporádico": random.randint(40, 90)  # Clientes que vão raramente
}

# Criar 200 clientes únicos com diferentes frequências
clientes = []
for _ in range(500):
    nome = fake.name()
    telefone = gerar_telefone_brasileiro()
    frequencia = random.choice(list(frequencias.keys()))
    clientes.append((nome, telefone, frequencias[frequencia]))

# Gerar visitas para cada cliente ao longo de um ano (2024)
data_inicio = datetime(2024, 1, 1)
data_fim = datetime(2024, 12, 31)
dados_visitas = []

for nome, telefone, intervalo in clientes:
    data_visita = data_inicio + timedelta(days=random.randint(0, 30))  # Primeira visita aleatória em janeiro
    while data_visita <= data_fim:
        dados_visitas.append([nome, telefone, data_visita.strftime('%Y-%m-%d')])
        data_visita += timedelta(days=intervalo)  # Próxima visita conforme a frequência do cliente

# Ordenar os dados por nome e data
dados_visitas.sort(key=lambda x: (x[0], x[2]))

# Criar o arquivo CSV
with open("frequencia_clientes_cabeleireiro.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Telefone", "Data de Ida ao Estabelecimento"])
    writer.writerows(dados_visitas)

print("Arquivo 'frequencia_clientes_cabeleireiro.csv' gerado com sucesso!")
