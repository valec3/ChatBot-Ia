# Ejemplo de uso del ChatBot

Este proyecto intenta simular un chatbot con múltiples modos de operación, incluyendo un modo de juego (TicTacToe), un modo de calculadora, y un modo normal para respuestas generales.

## Requisitos

- Python 3.x
- Librerías: `json`, `random`, `enum`
- Archivos JSON: `db.json`, `user_info.json`

## Estructura del Proyecto

- `app/`: Contiene el archivo principal `app.py` que maneja la lógica del chatbot.
- `calculator.py`: Implementa la funcionalidad de la calculadora.
- `clasificador.py`: Contiene la clase `Clasicador` para clasificar las entradas del usuario.
- `tictactoe.py`: Implementa la lógica del juego TicTacToe.
- `db.json`: Archivo JSON que contiene respuestas predefinidas para el chatbot.
- `user_info.json`: Archivo JSON para almacenar información del usuario.

## Modos de Operación

1. **Modo Normal**: Responde a preguntas generales basadas en el contenido de `
db.json`.
2. **Modo Calculadora**: Realiza operaciones matemáticas básicas.
3. **Modo TicTacToe**: Permite al usuario jugar una partida de TicTacToe contra la computadora.

## Cómo Ejecutar

1. Clona el repositorio.
2. Asegúrate de tener Python 3.x instalado.
3. Navega al directorio del proyecto y ejecuta `app.py`:

   ```bash
   cd app
   python app.py
   ```

4. Sigue las instrucciones en pantalla para interactuar con el chatbot.

## Ejemplo de Interacción

```
════════════════════════════════════════════════════════════════════════════════
Asistente ($normal): ¡Hola! Soy tu asistente. ¿En qué puedo ayudarte hoy?
Tú: hola que tal
════════════════════════════════════════════════════════════════════════════════
Asistente (normal): ¡Hola! ¿Cómo estás hoy?
Tú: calcula esto 4+5
════════════════════════════════════════════════════════════════════════════════
Asistente (matemáticas): El resultado es: 9
Tú: juguemos tic tac toe
════════════════════════════════════════════════════════════════════════════════
Asistente (normal): No entiendo tu mensaje. ¿Puedes reformularlo?
Tú: juguemos tictactoe
════════════════════════════════════════════════════════════════════════════════
Asistente (tictactoe): ¡Comencemos una partida de Tres en Raya!
|   |   |   |
|   |   |   |
|   |   |   |
Elige una posición del 0 al 8 para hacer tu movimiento.
Tú: 5
════════════════════════════════════════════════════════════════════════════════
Asistente (tictactoe): Tu movimiento:
|   |   | O |
|   |   | X |
Tú: 5
════════════════════════════════════════════════════════════════════════════════
Asistente (tictactoe): Tu movimiento:
|   |   | O |
|   |   | X |
|   |   |   |
Tú: 5
════════════════════════════════════════════════════════════════════════════════
Asistente (tictactoe): Tu movimiento:
|   |   | O |
|   |   | X |
|   |   |   |
Turno de la computadora.
Tú: 5
════════════════════════════════════════════════════════════════════════════════
Asistente (tictactoe): Tu movimiento:
|   |   | O |
|   |   | X |
|   |   |   |
Turno de la computadora.
Tú: que haces
════════════════════════════════════════════════════════════════════════════════
Asistente (normal): ¡Hola! ¿Cómo estás hoy?
Tú: salir
Asistente: ¡Hasta luego!
```
