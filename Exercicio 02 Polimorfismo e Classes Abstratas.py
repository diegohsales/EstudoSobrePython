"""
Crie uma hierarquia de classes conforme o diagrama. Os atributos em comum devem ficar na classe Animal e cada 
tipo de animal deve emitir um som diferente.

No programa principal, crie objetos dos 3 tipos de animais e execute o método que emite o som de cada um.
Implemente a seguir uma classe Veterinario que contenha o método examinar() cujo parâmetro de entrada é um animal.
O veterinário deve examinar cada um dos animais. Quando o animal for examinado ele também deve emitir o som do 
animal.
"""

#Veja um exemplo de programa principal
dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato


