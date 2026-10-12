from abc import ABC, abstractmethod

# ==========================================
# 1. CLASE ABSTRACTA: Usuario
# ==========================================
class Usuario(ABC):
    def __init__(self, id_usuario, nombre, correo, rol):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._correo = correo
        self._rol = rol
        self._estado_sesion = False

    # Método común para iniciar sesión
    def iniciarSesion(self, correo, rol):
        if self._correo == correo and self._rol == rol:
            self._estado_sesion = True
            print(f"✅ [INICIO DE SESIÓN] Bienvenido, {self._nombre} (Rol: {self._rol})")
            return True
        print("❌ [ERROR] Credenciales o rol incorrectos.")
        return False

    # Método común para cerrar sesión
    def cerrarSesion(self):
        self._estado_sesion = False
        print(f"🔒 [CIERRE DE SESIÓN] Sesión finalizada para {self._nombre}.")

    # Métodos abstractos o de consulta generales
    @abstractmethod
    def consultarHorario(self):
        pass


# ==========================================
# 2. SUBCLASE: Docente (Herencia de Usuario)
# ==========================================
class Docente(Usuario):
    def __init__(self, id_usuario, nombre, correo, cedula, especialidad):
        # Usamos super() para inicializar los atributos de la superclase
        super().__init__(id_usuario, nombre, correo, "Docente")
        self.__cedula = cedula
        self.__especialidad = especialidad
        self.__horarios_asignados = []

    # Implementación obligatoria del método abstracto
    def consultarHorario(self):
        print(f"📅 El docente {self._nombre} está consultando su horario de clases.")
        return self.__horarios_asignados

    def get_cedula(self):
        return self.__cedula


# ==========================================
# PRUEBA / DEMOSTRACIÓN DEL AVANCE
# ==========================================
if __name__ == "__main__":
    print("--- DEMOSTRACIÓN DE AVANCE: TIME CLASS ---\n")

    # 1. Intentar instanciar la clase abstracta directamente daría error (Abstracción en acción)
    # user = Usuario(1, "Test", "test@mail.com", "Admin") -> Esto fallaría por ser abstracta.

    # 2. Creamos un objeto de la subclase Docente
    profesor = Docente(
        id_usuario=101, 
        nombre="Ing. Carlos Mendoza", 
        correo="carlos.mendoza@timeclass.edu", 
        cedula="1309876543", 
        especialidad="Ingeniería de Software"
    )

    # 3. Probamos el inicio de sesión incorrecto
    profesor.iniciarSesion("carlos.mendoza@timeclass.edu", "Estudiante")

    print()

    # 4. Probamos el inicio de sesión correcto
    if profesor.iniciarSesion("carlos.mendoza@timeclass.edu", "Docente"):
        # 5. Consultamos el horario usando el método heredado/implementado
        profesor.consultarHorario()
        
        print()
        # 6. Cerramos sesión
        profesor.cerrarSesion()