# AsignacionPacientes22.03.25
Este código implementa un sistema de gestión de pacientes en un entorno hospitalario con prioridad de atención. Voy a explicar cómo funciona:
El código tiene tres clases principales:

Paciente: Almacena información básica del paciente como nombre, edad, DPI (documento de identificación), tipo de sangre, enfermedad y nivel de prioridad.
Enfermedad: Define enfermedades con un nombre, descripción y un valor numérico de prioridad (1-10).
SistemaAsignacion: Gestiona las colas de atención según la prioridad asignada a cada paciente:

Cola CRÍTICA: Para casos urgentes
Cola ALTA: Para casos importantes pero no críticos
Cola BAJA: Para casos que pueden esperar

El flujo de la aplicación es el siguiente:

Se crean enfermedades con distintos niveles de gravedad
Se registran pacientes con sus datos personales
Se les asigna una enfermedad y una prioridad (BAJA, ALTA, CRÍTICA)
El sistema coloca a cada paciente en la cola correspondiente
Los pacientes son atendidos según prioridad (primero los críticos, luego los de alta prioridad y finalmente los de baja)

En la ejecución, se crean 4 pacientes con diferentes condiciones y prioridades:

John Santeliz con gripe (prioridad BAJA)
Shirley Hernandez con fractura de fémur (prioridad ALTA)
Charly Muñez con apendicitis (prioridad CRÍTICA)
Lucy Gomez con resfriado común (prioridad BAJA)

El sistema atiende a 3 pacientes, siguiendo el orden de prioridad, y luego muestra el estado final de las colas.
