# POO y Algoritmos en Python

## Objetivos

- Entender como funciona la POOi

- Entender como medir la eficiencia temporral y espacial de nuestros algoritmos

- Entender como y porque graficar

- Aprender a resolver problemas de busqueda, ordenacion y optimizacion

## Tipos de datos

### Abstractos

En python todo es un objeto y todo tiene un tipo.

- Representacion de datos y formas de interactuar con ellos.

Formas de interactuar con un objeto

- Creacion, manipulacion, destruccioni

Ventajas

- Descomposicion, abstraccion, encapsulacion

Ahora que sabemos que todo en Python es un objeto y es un tipo de dato,

### Instancias

Mientras que la clase es un molde, a los objetos creados se les conoce como instancias

Cuando se crea una instancia, se ejecuta el metodo __init__

Todos los metodos de una clase reciben implicitamente como primer parametro self

Los atributos de clase nos permiten:

- Representar datos

- Procedimientos para interactuar con los mismos metodos

- Mecanismos para esconder la representacion interna

Se accede a los atributos con la notacion de punto

Se pueden tener atributos privados

### Decomposicion

Partir un problema en problemas mas pequenios

Las clases permiten crear mayores abstracciones en forma de componentes

Cada clase se encarga de una parte del problema y el programa se vuelve mas facil de mantener

### Abstraccion

Enfocarnos en la informacion relevante

Separar la informacion central de los detalles secundarios

Podemos utilizar variables y metodos (privados o publicos)

### Encapsulacion

Permite agrupar datos y su comportamiento

Controla el acceso a dichos datos

Previene modificaciones no autorizadas

### Herencia

Permite modelar una jerarquia de clases

Permite compartir comportameinto comun en la jerarquia

Al padre se le conoce como superclase y al huijo como subclase

### Polimorfismo

La habilidad de tomar varias formas

En Python, nos permite cambiar el comportamient de una superclase para adaptarlo a la subclase

## Intro a la complejidad algoritmica

Por que comparamos la eficiencia de un algoritmo

Complejidad temporal vs Complejidad espacial

### Crecimiento asintotico

No importan variaciones pequenias, el crecimiento asintotico es cuando el input se acerca mas al infinito

El enfoque se ecentra en lo que pasa conforme el tamanio del problema se acerca al infinito

Siempre podemos pensar en los mejores de los casos, promedio y peor de los casos, nuestro algoritmo debe estar preparado para el peor de los casos.

Big O notation, solo importa el input de mayor tamanio

## Clases de complejidad algoritmica

O(1) Constante - Nuestro tiempo de algoritmo no cambia, sin importar su input

O(n) Lineal - El tiempo de algoritmo crece conforme el valor del input crece

O(log n) Logaritmica - Nuestra funcion va a crecer de forma logaritmica conforme al input, primero va a crecer mucho y luego va a estabilizarse 

O(n log n) Log lineal - Va a crecer de forma logaritmica pero tambien con una constante

O(n ** 2) Polineal

O(2 ** n) Exponencial

## Busqueda Lineal

Busca en todos los elementos de manera secuencial

## Busqueda Binaria

Divide y conquista

El problema se divide en 2 en cada iteracion

## Ordenamiento de burbuja

Este ordenamiento es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si estan en el orden incorrecto. Este procedimiento se repite hasta que no se requieren mas intercambios, lo que indica que la lista se encuentra ordenada,

## Ordenamiento por insercion

Este algoritmo es uno de los mas comunes que estudian los CP's. Es intuitivo y facil de implementar, pero es ineficiente para listas de gran tamanio. Una de las caracteristicas del ordenamiento por inercion es que ordena en "su lugar". Es decir, no requiere memoria adicional para realizar el ordenamiento ya que simplemente modifican valores en memoria.

## Ordenamiento por mezcla

Es un algoritmo de divide y conquista. Primero divide una lista en partes iguales hasta que quedan sublistas de 1 o 0 elementos. Luego las recombinan en forma ordenada.
