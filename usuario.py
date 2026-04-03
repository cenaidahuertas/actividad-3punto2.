class Usuario:
    def __init__(
            self,
            id_usuario, 
            nombre, 
            apellido,
            email,
            contrasena,
            rol: str) -> None:
        
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self._contrasena = contrasena
        self.rol = rol

# ──id ────────────────────────────────

@property
def id_usuario(self):
    return self._id_usuario

@id_usuario.setter
def id_usuario(self, nuevo_id):
    if isinstance(nuevo_id, int) and nuevo_id > 0:
        self._id_usuario = nuevo_id
    else:
        raise ValueError("El ID de usuario debe ser un entero positivo.")
    
# ── nombre ────────────────────────────────
@property
def nombre(self):
    return self._nombre
@nombre.setter
def nombre(self, nuevo_nombre):
    if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
        self._nombre = nuevo_nombre.strip()
    else:
        raise ValueError("El nombre debe ser una cadena no vacía.")

# ── apellido ────────────────────────────────
@property
def apellido(self):
    return self._apellido

@apellido.setter
def apellido(self, nuevo_apellido):
    if isinstance(nuevo_apellido, str) and nuevo_apellido.strip():
        self._apellido = nuevo_apellido.strip()
    else:
        raise ValueError("El apellido debe ser una cadena no vacía.")

# ── email ────────────────────────────────
@property
def email(self):
    return self._email

@email.setter
def email(self, nuevo_email):
    if isinstance(nuevo_email, str) and "@" in nuevo_email:
        self._email = nuevo_email.strip()
    else:
        raise ValueError("El email debe ser una cadena válida que contenga '@'.")
    
# ── contraseña ────────────────────────────────
@property
def contrasena(self):
    return self._contrasena
@contrasena.setter
def contrasena(self, nueva_contrasena):
    if isinstance(nueva_contrasena, str) and len(nueva_contrasena) >= 6:
        self._contrasena = nueva_contrasena
    else:
        raise ValueError("La contraseña debe ser una cadena de al menos 6 caracteres.")

# ── rol ────────────────────────────────
@property
def rol(self):
    return self._rol
@rol.setter
def rol(self, nuevo_rol):
   if nuevo_rol in ["director", "encargado_catalogo", "visitante", "restaurador_jefe"]:
        self._rol = nuevo_rol
    else:
        raise ValueError("El rol debe ser 'director', 'encargado_catalogo', 'visitante' o 'restaurador_jefe'.")
    


# Autenticar usuario con email y contraseña ───────────────────────────────────

    def autenticar(self, email, contrasena):
        """Verifica si el email y contraseña coinciden con los del usuario."""
        return self.email == email and self._contrasena == contrasena
    
