# Instrucciones para agentes

Estas instrucciones se aplican a todo el repositorio.

## Proyecto

SwapBellCLI es una aplicación de terminal en Python 3 para consultar equivalencias
de bornes de telefonillos convencionales **4+n**. La interfaz y la documentación
están en español. Debe funcionar sin dependencias externas, también en Termux
(Android) e iSH (iPhone).

## Archivos principales

- `equivalenciasportero.py`: catálogo de marcas, entrada interactiva, tabla de
  equivalencias y punto de entrada `main()`.
- `README.md`: presentación, requisitos, instalación y uso.
- `e75a77e5-a7b7-46b5-8a57-aaa218894468.jpg`: portada del README; conserva su enlace
  relativo si se mueve o cambia de nombre.

## Criterios de edición

- Mantén el código sencillo y usa la biblioteca estándar. Evita introducir
  dependencias o herramientas de construcción sin una necesidad concreta.
- Conserva los nombres y mensajes en español y el estilo del código existente.
- Mantén la ejecución protegida por `if __name__ == "__main__":` para que importar
  el módulo no inicie preguntas interactivas.
- `MARCAS` es la fuente común de ambos menús. Su orden determina la numeración.
  Cada cadena contiene cinco bornes separados por guiones; sus posiciones
  establecen las correspondencias entre marcas. Conserva esa alineación.
- No inventes ni alteres equivalencias eléctricas por suposición. Cualquier cambio
  en esos datos debe apoyarse en documentación técnica o información explícita
  del usuario.
- Conserva la validación de respuestas y rangos, y el recordatorio sobre el tipo
  de llamada y las masas.
- Actualiza el README cuando cambien el uso, los requisitos o las marcas
  disponibles. Mantén coherente la versión si se modifica.
- Limita los cambios a la tarea solicitada y respeta los cambios previos del
  usuario. No incluyas archivos del sistema como `.DS_Store`.

## Ejecución y comprobaciones

Para ejecutar la aplicación:

```sh
python3 equivalenciasportero.py
```

Actualmente no hay una suite de pruebas ni configuración de herramientas de
calidad. Para cambios de comportamiento, comprueba los recorridos afectados.
Estos ejemplos permiten verificar el flujo normal y la validación de los menús:

```sh
printf '1\n2\n' | python3 equivalenciasportero.py
printf 'abc\n0\n11\n1\nabc\n0\n11\n2\n' | python3 equivalenciasportero.py
```

Ambos casos deben mostrar Tegui → Fermax con las parejas `1 → 4`, `2 → 3`,
`3 → 1`, `4 → 2` y `5 → 6`. El segundo debe rechazar las entradas no numéricas
y las opciones fuera de rango en ambos menús antes de aceptar las válidas.

Para cambios de documentación basta revisar el contenido, los enlaces locales
y `git diff --check`; no es necesario añadir pruebas automatizadas.
