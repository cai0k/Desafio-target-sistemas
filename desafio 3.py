import json

with open('dados.json', 'r') as file:
    data = json.load(file)

sem_nulos = [entry for entry in data if entry["valor"] != 0]

with open('arquivo_limpo.json', 'w') as file:
    json.dump(sem_nulos, file, indent=4)

with open('arquivo_limpo.json', 'r') as file:
    data = json.load(file)

maior_valor = max(data, key=lambda x: x["valor"])

menor_valor = min(data, key=lambda x: x["valor"])

valores = [entry["valor"] for entry in data]

media = sum(valores) / len(valores)

dias_acima_da_media = sum(1 for entry in data if entry["valor"] > media)


print("\nMaior valor: ", maior_valor["valor"])
print("Dia do maior valor: ", maior_valor["dia"])

print("\nMenor valor: ", menor_valor["valor"])
print("Dia do menor valor: ", menor_valor["dia"])

print("\nNúmero de dias com faturamento acima da média:", dias_acima_da_media)