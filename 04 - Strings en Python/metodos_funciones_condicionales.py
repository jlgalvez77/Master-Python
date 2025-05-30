print('Bienvenido Lopez'.islower())

print('VERANO'.isupper())

pelicula = 'El Libro De La Selva'
print(pelicula.istitle())

print('Hola Juan 123'.isalpha())  # False, contiene números
print('Juan'.isalpha())  # True, solo letras

print('598'.isnumeric())  # True, solo números
print('Hola123'.isalnum())  # True, letras y números

print('Hola Mundo'.isspace())  # False, contiene caracteres no espacios
print('   '.isspace())  # True, solo espacios