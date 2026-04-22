*Este proyecto ha sido creado como parte del currículo de 42 por beamarti.*

# get_next_line

## Descripción

**get_next_line** es un proyecto cuyo objetivo es implementar una función en C capaz de leer una línea completa desde un descriptor de archivo, devolviéndola en cada llamada sucesiva, hasta llegar al final del archivo.

La función permite leer tanto desde archivos como desde la entrada estándar, gestionando correctamente la memoria y conservando el estado entre llamadas. Este proyecto es clave para comprender la lectura incremental, el uso de buffers, las variables estáticas y la correcta gestión de memoria dinámica en C.


## Instrucciones

### Compilación

El proyecto no genera una librería independiente, sino que se compila junto con los archivos que la utilicen.

Ejemplo de compilación:

```bash
gcc -Wall -Werror -Wextra get_next_line.c get_next_line_utils.c main.c
```

Para definir el tamaño del buffer en tiempo de compilación:

```bash
gcc -Wall -Werror -Wextra -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c main.c
```

### Uso

Ejemplo básico de uso:

```c
#include "get_next_line.h"

int main(void)
{
    int fd;
    char *line;

    fd = open("archivo.txt", O_RDONLY);
    while ((line = get_next_line(fd)) != NULL)
    {
        printf("%s", line);
        free(line);
    }
    close(fd);
    return (0);
}
```

## Funcionamiento general

* Cada llamada a `get_next_line` devuelve la siguiente línea del archivo.
* La lectura se realiza usando un buffer de tamaño `BUFFER_SIZE`.
* La función conserva la información no utilizada para la siguiente llamada.
* Al llegar al final del archivo, devuelve `NULL`.

Una línea se define como una secuencia de caracteres que termina con un `\n` o con el final del archivo.


## Elección del algoritmo y estructura de datos

### Algoritmo

El algoritmo se basa en un ciclo de lectura incremental:

1. Se lee desde el descriptor de archivo en bloques de tamaño `BUFFER_SIZE`.
2. El contenido leído se concatena a un buffer estático.
3. Se comprueba si el buffer contiene un salto de línea (`\n`).
4. Si existe, se extrae la línea completa y se guarda el resto para la siguiente llamada.
5. Si no existe, se continúa leyendo hasta encontrarlo o llegar al EOF.

Este enfoque permite leer archivos de cualquier tamaño sin cargarlos completamente en memoria.

### Variable estática

Se utiliza una **variable estática** para conservar el contenido sobrante entre llamadas a la función. Esta decisión es fundamental para cumplir el requisito del proyecto y permite mantener el estado sin usar variables globales.

### Gestión de memoria

* Toda la memoria reservada dinámicamente es liberada correctamente.
* Cada línea devuelta debe ser liberada por el usuario.
* Se evitan fugas de memoria incluso en casos de error o fin de archivo.

### Estructuras de datos

No se utilizan estructuras complejas. El proyecto se apoya en:

* Strings dinámicos (`char *`)
* Variables estáticas

Esto mantiene el código simple, eficiente y fácil de depurar.


## Archivos del proyecto

* `get_next_line.c` : lógica principal de la función
* `get_next_line_utils.c` : funciones auxiliares (string length, join, search, etc.)
* `get_next_line.h` : prototipos y definición de `BUFFER_SIZE`


## Recursos

### Documentación y referencias

* Manual de `read`: `man 2 read`
* Manual de gestión de memoria: `man malloc`, `man free`

### Uso de Inteligencia Artificial

Se ha utilizado inteligencia artificial como apoyo puntual para:

* Comprender el funcionamiento de la función `read`.
* Analizar el uso de variables estáticas.
* Revisar explicaciones teóricas sobre gestión de memoria y buffers.

La implementación, decisiones técnicas y validación final del código han sido realizadas por la autora del proyecto.

## Notas finales

Este proyecto refuerza conceptos fundamentales del lenguaje C y es especialmente relevante para proyectos posteriores del currículo de 42 donde se requiere lectura de archivos o comunicación por streams.
