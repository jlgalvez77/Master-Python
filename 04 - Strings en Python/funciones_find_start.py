print('Hola Python')
buscador = 'Este texto es para buscar caracteres, utilizando el caracter como parametro'

print(buscador.find('E'))
print(buscador.find('texto'))
print(buscador.find('Hammer'))
print(buscador.find('e'))

print(buscador.find('E', 3))


print(buscador.index('E'))
# print(buscador.index('Hammer'))  # Esto lanzará un error si no se encuentra

print(buscador.startswith('Este'))
print(buscador.startswith('texto'))

print(buscador.endswith('parametro'))