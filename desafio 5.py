s = input("Digite uma string: ")

string_invertida = ""

for i in range(len(s) - 1, -1, -1): 
    string_invertida += s[i] 

print("String original:", s)
print("String invertida:", string_invertida)
