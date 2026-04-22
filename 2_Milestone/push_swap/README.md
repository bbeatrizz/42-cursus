*Este proyecto ha sido creado como parte del currículo de 42 por beamarti.*

# Push_Swap

## Descripción
Push_Swap es un proyecto del currículo de 42 cuyo objetivo es crear un programa que ordene una lista de enteros utilizando un conjunto limitado de operaciones sobre **dos pilas**. El objetivo es generar la **secuencia más corta posible de movimientos** para ordenar la pila en orden ascendente.  

El programa debe manejar:  
- Argumentos pasados individualmente (por ejemplo: `./a.out 3 2 1`)  
- Argumentos pasados como una **cadena con espacios** (por ejemplo: `./a.out "3 2 1"`)  
- Validación de entradas: sin duplicados y dentro del rango de enteros de 32 bits.  

Estrategias de ordenación implementadas:  
- **Sort Two**: intercambio simple si es necesario.  
- **Sort Three**: secuencia optimizada para 3 elementos.  
- **Sort Five**: mueve los elementos mínimos a una segunda pila, ordena los 3 restantes y vuelve a insertar los mínimos.  
- **Radix Sort**: utilizado para más de 5 elementos.  

El proyecto asegura la correcta gestión de memoria, incluyendo la liberación de nodos y los splits dinámicos para cadenas.

---

## Instrucciones

### Compilación
Compila el proyecto usando el Makefile incluido:

```bash
make
```

Esto generará la librería estática `pushswap.a`. Luego, compila el ejecutable a partir de la librería:

```bash
gcc -Wall -Werror -Wextra pushswap.a -o push_swap
```

### Ejecución
Ejecuta el programa pasando los números como argumentos:

```bash
./push_swap 3 2 1
./push_swap "3 2 1"
./push_swap 5 "4 3 1"
```

El programa imprimirá en la salida estándar la secuencia de operaciones necesarias para ordenar la pila (`sa`, `ra`, `pb`, `pa`, etc.).

---

## Recursos
Referencias clásicas sobre el tema:  
- Documentación de listas enlazadas en C  
- Artículos y tutoriales sobre **push_swap** y algoritmos de ordenación (Radix, inserción, swaps mínimos)  
- Foros y repositorios de 42 sobre buenas prácticas en push_swap  

### Uso de IA
Se utilizó IA para:  
- Planificar la estructura modular del proyecto  
- Optimizar validación de entrada  
- Explicar el flujo de operaciones para casos de prueba  

La lógica, implementación y validación final del código han sido realizadas por la autora del proyecto.
---

## Notas técnicas
- Todas las funciones de manipulación de pilas (`swap`, `push`, `rotate`, `revrotate`) siguen la lógica estándar de push_swap.  
- Se gestiona correctamente la memoria, liberando todas las pilas y splits dinámicos al finalizar.  
- El código está preparado para manejar cualquier combinación de argumentos en línea de comando, incluyendo cadenas con varios números separados por espacios.  

---