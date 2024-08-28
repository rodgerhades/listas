#listas

frutas = []

while True:
    fruta = input("escolha sua fruta ou fim ")
    if fruta.lower() == "fim":
        break
    frutas.append(fruta)
    
print("lista de frutas: ")
for fruta in frutas:
    print(fruta)
    