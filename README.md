# SwapBellCLI

**Versión 0.2 · EYIlabs**

Aplicación de terminal escrita en Python para consultar las equivalencias de bornes al sustituir un telefonillo de portero automático convencional. Es válida únicamente para sistemas **4+n**.

Selecciona la marca del telefonillo instalado y la del que vas a instalar. SwapBellCLI muestra una tabla con la correspondencia entre los bornes de ambos equipos.

## Marcas disponibles

Tegui, Fermax, Golmar, Alcad, Auta, Guinaz, Fringe, Bticino, Farfisa y Comelit.

Las diez marcas están disponibles en ambos menús.

## Requisitos

- Python 3, sin dependencias externas.
- Git para descargar el repositorio con los comandos siguientes.
- Una terminal. En iPhone puedes utilizar iSH; en Android, Termux.

## Instalación y ejecución

### En un ordenador

Con Git y Python 3 instalados, ejecuta:

```sh
git clone https://github.com/joseancalvo/SwapBellCLI.git
cd SwapBellCLI
python3 equivalenciasportero.py
```

### En Android con Termux

Instala Termux desde [F-Droid](https://f-droid.org/es/) y abre la aplicación.

Actualiza los paquetes e instala Git y Python:

```sh
pkg update
pkg upgrade
pkg install git python
```

Descarga el repositorio y ejecuta el programa:

```sh
git clone https://github.com/joseancalvo/SwapBellCLI.git
cd SwapBellCLI
python3 equivalenciasportero.py
```

### En iPhone con iSH

Instala iSH desde la App Store y abre la aplicación.

Actualiza los paquetes e instala Git y Python:

```sh
apk update
apk upgrade
apk add git python3
```

Descarga el repositorio y ejecuta el programa:

```sh
git clone https://github.com/joseancalvo/SwapBellCLI.git
cd SwapBellCLI
python3 equivalenciasportero.py
```

## Uso

1. Indica si el telefonillo es `viejo` o `nuevo`. La respuesta admite mayúsculas y espacios al principio o al final. Si escribes `nuevo`, el programa te pide que revises las conexiones y termina.
2. Si escribes `viejo`, selecciona la marca del telefonillo instalado introduciendo un número del 1 al 10.
3. Selecciona la marca del telefonillo que vas a instalar, también del 1 al 10.
4. Consulta la tabla de equivalencias. Cada fila relaciona un borne del telefonillo instalado con el correspondiente en el nuevo.

Si una respuesta no es válida, el programa muestra un aviso y vuelve a pedirla. Los menús aceptan únicamente números enteros dentro del rango indicado.

Por ejemplo, al seleccionar Tegui como marca instalada y Fermax como marca nueva:

```text
Correspondencia de bornes
Instalado: Tegui | Nuevo: Fermax
-----------------+--------------
1                → 4
2                → 3
3                → 1
4                → 2
5                → 6
```

Antes de realizar la sustitución, revisa el tipo de llamada y las masas, tal como recuerda el programa.

## Novedades de la versión 0.2

- Validación de respuestas y opciones de los menús.
- Diez marcas disponibles tanto para el telefonillo instalado como para el nuevo.
- Código organizado en funciones, con un catálogo común de marcas y bornes.
- Tabla de correspondencias entre bornes.
- Nueva cabecera con un telefonillo descolgado en ASCII y la firma EYIlabs.
