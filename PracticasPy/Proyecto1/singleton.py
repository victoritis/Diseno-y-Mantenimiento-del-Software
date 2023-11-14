class Cliente():
    pass

instancia = None
def get_instancia():
    global instancia
    if instancia is None: 
        instancia = Cliente()
    return instancia

print (get_instancia())
print (get_instancia())
print (get_instancia())

print(Cliente())
print(Cliente())