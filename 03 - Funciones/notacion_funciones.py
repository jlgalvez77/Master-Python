def multiplicado_palabras(texto, cantidad):
    return texto * cantidad

resultado = multiplicado_palabras('Hammer', 10)
print(resultado)

def miltiplicador_notacion(texto: str, cantidad: int)-> str:
    return texto * cantidad

resultado_notacion = miltiplicador_notacion('Jose', 10)
print(resultado_notacion)