# POO y Algoritmos en Python

## Objetivos

- Entender como funciona POO

- Entender como medir la eficiencia temporral y espacial de nuestros algoritmos

- Entender como y porque graficar

- Aprender a resolver problemas de busqueda, ordenacion y optimizacion con python

## [POO](https://en.wikipedia.org/wiki/Object-oriented_programming)

La Programacion Orientada a Objetos nos permite modelar cosas reales y concretas
del mundo y sus relaciones con otros objectos.

## Tipos de datos

### Abstractos

- En python todo es un objeto y todo tiene un tipo ```type(data)```. Esto significa
que todo lo que hagamos dentro de nuestro programa tiene una representacion en
memoria, el hecho de que cada objeto tenga un tipo, significa que podemos
encapsular sus datos y comportamientos.

  - Representacion de datos y formas de interactuar con ellos.

- Formas de interactuar con un objeto

  - Creacion

  - Manipulacion

  - Destruccion

Ventajas

- Descomposicion: Podemos decontruir el objeto lo mas que queramos

- Abstraccion

- Encapsulacion: Podemos esconder ciertos datos y manejarlos internamente

Desventajas

- ??????

```python
class <class_name>(<super_class>):
  def __init__(self, <param>):
    <expression>

  def <methods>():
```

```python
class Persona:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def cheer(self, other_person):
    return f'Hola, {other_person.name, me llamo self.name} tengo self.age anios'

person1 = Person('Rafael', 30)
person2 = Person('YouTube', 15)

person.cheer(person2)
```

### Instancias

- Mientras que la clase es un molde, 
a los objetos creados se les conoce como instancias

- Cuando se crea una instancia, se ejecuta el metodo ```__init__```

- Todos los metodos de una clase reciben implicitamente como
primer parametro ```self```

- Los atributos de clase nos permiten:

  - Representar datos

  - Procedimientos para interactuar con los mismos metodos

  - Mecanismos para esconder la representacion interna

- Se accede a los atributos con la notacion de punto

- Se pueden tener atributos privados. En python por convencion se usa ```_```

Ejemplo de instancias: [instaces.py](./oop_instaces.py)

### Decomposicion

- Partir un problema en problemas mas pequenios

- Las clases permiten crear mayores abstracciones en forma de componentes

- Cada clase se encarga de una parte del problema y el programa se
vuelve mas facil de mantener

Ejemplo de decomposition: [decomposition.py](./oop_decomposition.py)

### Abstraccion

- Enfocarnos en la informacion relevante

- Separar la informacion central de los detalles secundarios

- Podemos utilizar variables y metodos (privados o publicos)

Ejemplo de abstraccion: [abstraction.py](./oop_abstraction.py)

### Encapsulacion

- Permite agrupar datos y su comportamiento

- Controla el acceso a dichos datos

- Previene modificaciones no autorizadas

Ejemplo de encapsulacion: [encapsulation.py](./oop_encapsulation.py)

### Herencia

- Permite modelar una jerarquia de clases

- Permite compartir comportameinto comun en la jerarquia

- Al padre se le conoce como superclase y al huijo como subclase

Ejemplo de herencia: [herently.py](./oop_herently.py)

### Polimorfismo

- La habilidad de tomar varias formas

En Python, nos permite cambiar el comportamient de una superclase para adaptarlo a la subclase

Ejemplo de polimorfismo: [polymorphism.py](./oop_polymorphism.py)

## Intro a la Complejidad Algoritmica

- Por que comparamos la eficiencia de un algoritmo?

- Complejidad temporal vs Complejidad espacial

- Podemos definirla como T(n)

Aproximaciones

- Cronometrar el tiempo en el que corre un algoritmo

- Contar los pasos con una medida abstracta de operacion

- Contar los pasos conforme nos aproximamos al infinito

### Crecimiento asintotico

- No importan variaciones pequenias, el crecimiento asintotico es cuando el input se acerca mas al infinito

- El enfoque se ecentra en lo que pasa conforme el tamanio del problema se acerca al infinito

- Siempre podemos pensar en los mejores de los casos, promedio y peor de los casos,
nuestro algoritmo debe estar preparado para el peor de los casos.

- Big O notation, solo importa el input de mayor tamanio

```py
# Ley de la suma

# O(n) + O(n) => O(n + n) => O(2n) => O(n)
# El algoritmo crece de forma lineal, la funcion crece con respecto a n de manera lineal
# (no importan los terminos especificos)

def f(n):
  for i in range(n):
    print(i)

  for i in range (n):
    print (i)


# O(n) + O(n * n) => O(n + n^2) => O(n^2) 
# El algoritmo crece de forma cuadratica, porque importa el termino mas grande, no importa el coeficiente,
# mientras mas nos acercamos a infinito

def f(n):
  for i in range(n):
    print(i)

  for i in range(n * n):
    print(i)



# Ley de la multiplicacion

# O(n) * O(n) => O(n * n) => O(n^2)
# Crecimiento cuadratico

def f(n):
  for i in range(n):
    for j in range(n):
      print(i,j)


# Recursividad multiple
# O(n^2)

def fibonacci(n):
  if == n or n == 1:
    return 1
  return fibonacci(n-1)+fibonacci(n-n)
```

## Clases de complejidad algoritmica

- **O(1) Constante**:  Nuestro tiempo de algoritmo no cambia, sin importar su input.

- **O(n) Lineal**: El tiempo de algoritmo crece conforme el valor del input crece.

- **O(log n) Logaritmica**: Nuestra funcion va a crecer de forma logaritmica conforme al input,
primero va a crecer mucho y luego va a estabilizarse 

- **O(n log n) Log lineal**: Va a crecer de forma logaritmica pero tambien con una constante

- **O(n^2)**: Polineal

- **O(2^n)**: Exponencial

## [Busqueda Lineal](./lineal_search.py)

- Busca en todos los elementos de manera secuencial

- Cual es el peor caso? Cantidad de elementos

## [Busqueda Binaria](./binary_search.py)

- Divide y conquista

- El problema se divide en 2 en cada iteracion

- Cual es el peor caso? 

## Ordenamiento de burbuja

Este ordenamiento es un algoritmo que recorre repetidamente una lista que necesita ordenarse.
Compara elementos adyacentes y los intercambia si estan en el orden incorrecto.
Este procedimiento se repite hasta que no se requieren mas intercambios, lo que indica que la
lista se encuentra ordenada,

## Ordenamiento por insercion

Este algoritmo es uno de los mas comunes que estudian los CPU's. Es intuitivo y facil de
implementar, pero es ineficiente para listas de gran tamanio. Una de las caracteristicas
del ordenamiento por inercion es que ordena en "su lugar". Es decir, no requiere
memoria adicional para realizar el ordenamiento ya que simplemente modifican valores en memoria.

## Ordenamiento por mezcla

Es un algoritmo de divide y conquista. Primero divide una lista en partes
iguales hasta que quedan sublistas de 1 o 0 elementos. Luego las recombinan en forma ordenada.

## Porque graficar

- Reconocimiento de patrones

- Prediccion de una serie

- Simplifica la interptretacion y las conclusiones acerca los datos

## Introduccion a la optimizacion

- El concepto de optimizacion permite resolver muchos problemas de manera computacional

- Una funcion objetivo que debemoz maximizar o minimizar

- Una serie de limitantes que debemos respetar

## [El problema del morral](https://en.wikipedia.org/wiki/Knapsack_problem)



https://www.bigocheatsheet.com/
https://bigocheatsheet.io/

