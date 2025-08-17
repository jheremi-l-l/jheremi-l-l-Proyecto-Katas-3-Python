# Crea la clase UsuarioBanco
# Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
# Código a seguir:
# Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
# Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
# Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
# Implementar agregar_dinero para aumentar el saldo del usuario.


# Clase Usuario Banco
class UsuarioBanco:

    # Método Constructor
    def __init__(self, nombre, saldo, cuenta_corriente):

        # Atributos
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    # Método Retirar Dinero
    def retirar_dinero(self, cantidad):
        
        # Controlamos excepciones
        if cantidad <= 0:
            raise ValueError("⚠️ La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError(f"❌ Saldo insuficiente. {self.nombre} tiene solo {self.saldo}€.")
        
        # Retiramos el dinero
        self.saldo -= cantidad
        print(f"💸 {self.nombre} ha retirado {cantidad}€. Saldo actual: {self.saldo}€.")

    def transferir_dinero(self, otro_usuario, cantidad):
        # Controlamos excepciones o errores
        if not isinstance(otro_usuario, UsuarioBanco):
            raise TypeError("⚠️ El destinatario debe ser un UsuarioBanco.")
        if cantidad <= 0:
            raise ValueError("⚠️ La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError(f"❌ No se puede transferir {cantidad}€. Saldo insuficiente.")

        # Retiramos el dinero de nuestro saldo
        self.saldo -= cantidad
        # Sumamos dinero a otro usuario
        otro_usuario.saldo += cantidad 
        print(f"🔁 {self.nombre} ha transferido {cantidad}€ a {otro_usuario.nombre}.")

    # Método para agragar dinero
    def agregar_dinero(self, cantidad):
        # Control de excepcion
        if cantidad <= 0:
            raise ValueError("⚠️ La cantidad a agregar debe ser mayor que cero.")
        
        # Ingresamos dinero
        self.saldo += cantidad
        print(f"💰 {self.nombre} ha agregado {cantidad}€. Saldo actual: {self.saldo}€.")

    # Método información del usuario
    def info_usuario(self):
        tipo = "Cuenta Corriente" if self.cuenta_corriente else "Cuenta de Ahorros"
        return (
            f"👤 Usuario: {self.nombre}\n"
            f"🏦 Tipo de cuenta: {tipo}\n"
            f"💳 Saldo disponible: {self.saldo}€"
        )

# Instanciamos

# Caso de uso:


#a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)


# Mostrar info inicial
print(alicia.info_usuario())
print(bob.info_usuario())

#b. Agregar 20 unidades al saldo de Bob.

bob.agregar_dinero(20)

#c. Transferir 80 unidades de Bob a Alicia.

bob.transferir_dinero(alicia,80)
# bob.transferir_dinero(alicia, 10)

#d. Retirar 50 unidades del saldo de Alicia.

alicia.retirar_dinero(50)


# Mostrar info inicial
print(alicia.info_usuario())
print(bob.info_usuario())
