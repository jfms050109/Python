ids_clientes=[1,2,3,4,5,6]

def add_cliente():
    ids_clientes.append(ids_clientes[len(ids_clientes)-1]+1)

print(ids_clientes[:])
add_cliente()
print(ids_clientes)
