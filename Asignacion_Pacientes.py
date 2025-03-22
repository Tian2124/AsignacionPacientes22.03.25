class Paciente:
    def __init__(self, nombre, edad, dpi, tipo_de_sangre):
        self.nombre = nombre
        self.edad = edad
        self.dpi = dpi
        self.tipo_de_sangre = tipo_de_sangre
        self.enfermedad = None
        self.prioridad = None

    def asignar_enfermedad(self, enfermedad):
        self.enfermedad = enfermedad

    def asignar_prioridad(self, prioridad):
        if prioridad not in ["BAJA", "ALTA", "CRITICA"]:
            raise ValueError("La prioridad debe ser BAJA, ALTA o CRITICA")
        self.prioridad = prioridad

    def __str__(self):
        return f"Paciente {self.nombre}: Edad {self.edad} años, DPI {self.dpi}, Tipo sangre {self.tipo_de_sangre} - Enfermedad: {self.enfermedad}, Prioridad: {self.prioridad}"


class Enfermedad:
    def __init__(self, nombre, descripcion, prioridad_atencion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad_atencion = prioridad_atencion  # Valor numérico de 1 a 10

    def __str__(self):
        return self.nombre


class SistemaAsignacion:
    def __init__(self):
        self.pacientes = []
        self.cola_baja = []
        self.cola_alta = []
        self.cola_critica = []

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)
        self.asignar_a_cola(paciente)

    def asignar_a_cola(self, paciente):
        if paciente.prioridad == "BAJA":
            self.cola_baja.append(paciente)
        elif paciente.prioridad == "ALTA":
            self.cola_alta.append(paciente)
        elif paciente.prioridad == "CRITICA":
            self.cola_critica.append(paciente)

    def siguiente_paciente(self):

        if self.cola_critica:
            return self.cola_critica.pop(0)
        elif self.cola_alta:
            return self.cola_alta.pop(0)
        elif self.cola_baja:
            return self.cola_baja.pop(0)
        else:
            return None

    def mostrar_estado_colas(self):
        print("\nESTADO ACTUAL DE LAS COLAS DE ATENCIÓN:")
        print(f"Cola CRÍTICA: {len(self.cola_critica)} pacientes")
        print(f"Cola ALTA: {len(self.cola_alta)} pacientes")
        print(f"Cola BAJA: {len(self.cola_baja)} pacientes")


if __name__ == "__main__":
    # Enfermedades
    gripe = Enfermedad("Gripe", "Infección respiratoria viral", 3)
    fractura = Enfermedad("Fractura de fémur", "Fractura en el hueso más largo de la pierna", 7)
    apendicitis = Enfermedad("Apendicitis", "Inflamación del apéndice que requiere cirugía", 9)
    resfriado = Enfermedad("Resfriado común", "Infección viral leve de las vías respiratorias", 2)

    # Pacientes
    p1 = Paciente("John Santeliz", 45, "1234567890123", "O+")
    p1.asignar_enfermedad(gripe)
    p1.asignar_prioridad("BAJA")

    p2 = Paciente("Shirley Hernandez", 67, "9876543210123", "A-")
    p2.asignar_enfermedad(fractura)
    p2.asignar_prioridad("ALTA")

    p3 = Paciente("Charly Muñez", 34, "5678901234567", "B+")
    p3.asignar_enfermedad(apendicitis)
    p3.asignar_prioridad("CRITICA")

    p4 = Paciente("Lucy Gomez", 28, "3456789012345", "AB+")
    p4.asignar_enfermedad(resfriado)
    p4.asignar_prioridad("BAJA")

    sistema = SistemaAsignacion()

    sistema.registrar_paciente(p1)
    sistema.registrar_paciente(p2)
    sistema.registrar_paciente(p3)
    sistema.registrar_paciente(p4)

    sistema.mostrar_estado_colas()

    print("\nATENCIÓN DE PACIENTES:")
    for _ in range(3):
        paciente = sistema.siguiente_paciente()
        if paciente:
            print(f"Atendiendo a: {paciente}")

    sistema.mostrar_estado_colas()