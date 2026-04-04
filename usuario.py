"""
Módulo: usuario.py
Clase base para todos los usuarios del sistema del museo.
"""


class Usuario:
    def __init__(self, id_usuario, nombre, apellido, email, contrasena, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self._contrasena = contrasena
        self.rol = rol

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id > 0:
            self._id_usuario = nuevo_id
        else:
            raise ValueError("El ID de usuario debe ser un entero positivo.")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        if isinstance(nuevo_apellido, str) and nuevo_apellido.strip():
            self._apellido = nuevo_apellido.strip()
        else:
            raise ValueError("El apellido debe ser una cadena no vacía.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        if isinstance(nuevo_email, str) and "@" in nuevo_email:
            self._email = nuevo_email.strip()
        else:
            raise ValueError("El email debe contener '@'.")

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, nuevo_rol):
        roles_validos = ["director", "encargado_catalogo", "visitante", "restaurador_jefe"]
        if nuevo_rol in roles_validos:
            self._rol = nuevo_rol
        else:
            raise ValueError(f"El rol debe ser uno de: {roles_validos}")

    def autenticar(self, email, contrasena):
        """Verifica si el email y contraseña coinciden."""
        return self.email == email and self._contrasena == contrasena

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido} | Email: {self.email} | Rol: {self.rol}"
