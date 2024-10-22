def procurar_letra_a(string):
    letra = "a"
    contagem = string.lower().count(letra.lower())
    return (f"Quantidade de vezes que a letra 'a' aparece na string '{string}': {contagem}")

string = input("Insira a string: ")
resultado = procurar_letra_a(string)
print(resultado)