# Karma Simulator

Simulador de karma para un juego RPG utilizado para practicar

## Como funciona?

Este simulador presenta al jugador una situacion con multiples decisiones con las cuales se alterara el valor del karma del jugador y acumulandolo en un total.

El flujo general es:

1. Se genera una situación aleatoria con opciones.
2. El jugador elige una decisión.
3. El karma se actualiza según la elección.
4. Se muestra el karma actual y un mensaje personalizado.
5. El jugador puede continuar enfrentando nuevas situaciones.


## Caracteristicas
- Diseño modular con funciones separadas
- Escalable: fácil de agregar nuevas situaciones y decisiones
- Bucle interactivo para múltiples rondas
- Preparado para documentación y publicación en GitHub

## Instalación y uso
1. Clona el repositorio:

   ```bash
   git clone https://github.com/YAMS947NZ/Aprendizaje-.git
   cd Aprendizaje

2. Ejecuta el simulador:
   python main.py

## Estructura del proyecto
karma-simulator/
├── karma.py        # Funciones del simulador
├── main.py         # Bucle principal
├── .gitignore      # Archivos ignorados por Git
└── README.md       # Documentación del proyecto

## Futuras mejoras
- Integrar interfaz gráfica (Tkinter o PyGame)
- Guardar progreso del jugador
- Añadir mas situaciones
- Dar opciones para decidir mas complejas
- Crear situaciones con que requiran tomar mas de una decisión

##  Contribuciones
¡Las contribuciones son bienvenidas! Puedes abrir un issue o enviar un pull request con mejoras, nuevas situaciones o refactorizaciones.

## Autor
Desarrollado por YAMS947NZ como parte de su aprendizaje en programación y desarrollo de proyectos modulares en Python.
