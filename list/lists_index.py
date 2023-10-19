clients=['joao','felipe','olivia','alipio']
string=''
listaex=['','','']
def screch(lista,elemento):
    if type(lista)==type(listaex) or type(lista)==type(string):
        return lista.index(elemento)


print(screch(clients,'felipe'))