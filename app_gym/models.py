from django.db import models

# ==========================================
# MODELO: MIEMBRO
# ==========================================
class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    membresia_activa = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='miembros_imagenes/', blank=True, null=True) # Campo para la imagen

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================

# MODELO: CLASE (Adorno por ahora)
# ==========================================
class Clase(models.Model):
    nombre_clase = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horario = models.CharField(max_length=50) # Ejemplo: "Lunes 10:00-11:00"
    duracion_minutos = models.IntegerField()
    cupo_maximo = models.IntegerField()
    nivel_dificultad = models.CharField(
        max_length=20,
        choices=[
            ('Principiante', 'Principiante'),
            ('Intermedio', 'Intermedio'),
            ('Avanzado', 'Avanzado'),
        ],
        default='Principiante'
    )
    # Relación de Muchos a Muchos con Miembro
    miembros_inscritos = models.ManyToManyField(Miembro, related_name='clases_inscritas', blank=True)

    def __str__(self):
        return self.nombre_clase

# ==========================================
# MODELO: EMPLEADO (Adorno por ahora)
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_contratacion = models.DateField(auto_now_add=True)
    puesto = models.CharField(max_length=100) # Ej: "Instructor", "Recepcionista", "Gerente"
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    # Relación de Uno a Muchos con Clase (un empleado puede impartir muchas clases)
    clases_impartidas = models.ForeignKey(
        Clase,
        on_delete=models.SET_NULL, # Si la clase se elimina, el empleado sigue existiendo pero no tendrá clase asignada
        related_name='instructores',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.puesto})"