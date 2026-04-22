*Este proyecto ha sido creado como parte del currículo de 42 por beamarti.*

# ft_printf

## Descripción

**ft_printf** es una reimplementación en C de la función estándar `printf` de la biblioteca estándar de C. El objetivo principal del proyecto es comprender en profundidad el manejo de funciones variádicas, el formateo de salida y la conversión de tipos.

Este proyecto permite imprimir diferentes tipos de datos (caracteres, strings, enteros, hexadecimales, punteros, etc.) siguiendo un formato definido por una cadena de formato, replicando el comportamiento básico de `printf`.


## Instrucciones

### Compilación

El proyecto genera una librería estática `libftprintf.a`.

Para compilarla, ejecutar:

```bash
make
```

Esto compilará todos los archivos fuente y creará la librería.

### Limpieza

```bash
make clean      # Elimina archivos objeto
make fclean     # Elimina archivos objeto y la librería
make re         # Recompila el proyecto desde cero
```

### Uso

Una vez compilada la librería, puede utilizarse enlazándola en cualquier proyecto C:

```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("Hola %s, número: %d\n", "42", 42);
    return (0);
}
```

Compilación del ejemplo:

```bash
cc -Wall -Werror -Wextra main.c libftprintf.a
```


## Características implementadas

* `%c` : imprime un carácter
* `%s` : imprime una cadena
* `%p` : imprime una dirección de memoria en hexadecimal
* `%d` / `%i` : imprime un número entero con signo
* `%u` : imprime un entero sin signo
* `%x` / `%X` : imprime un número en hexadecimal (minúsculas / mayúsculas)
* `%%` : imprime el carácter `%`

La función devuelve el número total de caracteres impresos, igual que `printf`.


## Elección del algoritmo y estructura de datos

### Algoritmo

El algoritmo principal de `ft_printf` consiste en recorrer secuencialmente la cadena de formato carácter a carácter:

1. Si el carácter actual no es `%`, se escribe directamente en la salida estándar.
2. Si se encuentra `%`, se analiza el carácter siguiente para identificar el especificador de formato.
3. Según el especificador, se llama a la función correspondiente para manejar ese tipo de dato.
4. Cada función especializada se encarga de convertir el valor recibido a su representación en texto y escribirlo.

### Funciones variádicas

Se utiliza la biblioteca `<stdarg.h>` para manejar un número variable de argumentos mediante:

* `va_start`
* `va_arg`
* `va_end`

Esto permite extraer los argumentos según el tipo indicado por el especificador de formato.

### Estructura de datos

No se utilizan estructuras de datos complejas. El proyecto se apoya en:

* Tipos primitivos (`int`, `unsigned int`, `unsigned long`, `char *`)
* Strings en C

Esta decisión reduce la complejidad y facilita el control total de la memoria, uno de los objetivos clave del proyecto.


## Recursos

### Documentación y referencias

* Manual de `printf`: `man 3 printf`
* Manual de funciones variádicas: `man stdarg`

### Uso de Inteligencia Artificial

Se ha utilizado inteligencia artificial como apoyo puntual para:

* Aclarar conceptos teóricos sobre funciones variádicas.
* Comprender el manejo de conversiones numéricas (decimal y hexadecimal).
* Revisar explicaciones y mejorar la claridad del diseño del código.

La lógica, implementación y validación final del código han sido realizadas por la autora del proyecto.


## Notas finales

Este proyecto forma parte del aprendizaje progresivo del lenguaje C dentro del currículo de 42 y sienta las bases para proyectos posteriores.
