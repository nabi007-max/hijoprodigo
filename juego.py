class HijoProdigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dinero = 100
        self.dignidad = 50
        self.hambre = 0
        self.arrepentimiento = 0

    def gastar_todo(self):
        self.dinero = 0
        self.dignidad -= 20
        self.hambre += 50

    def invertir(self):
        self.dinero += 20
        print(f"Has invertido sabiamente. Dinero: {self.dinero}")

    def ahorrar(self):
        self.dinero += 20
        print(f"Has ahorrado. Dinero: {self.dinero}")

    def reflexionar(self):
        if self.hambre > 40:
            self.arrepentimiento += 10

jugador = HijoProdigo(input("Ingrese su nombre: "))

print(f"\n{jugador.nombre} ha recibido su herencia")
print(f"Dinero inicial: {jugador.dinero}")

# 🔁 BUCLE PRINCIPAL DEL JUEGO
while jugador.dinero > 0:
    print("\nSigues viviendo lejos de casa:…")
    print("Elige una opción:")
    print("1. Gastar todo")
    print("2. Invertir")
    print("3. Ahorrar")

    opcion = input("Opción: ")

    if opcion == "1":
        jugador.gastar_todo()
    elif opcion == "2":
        jugador.invertir()
    elif opcion == "3":
        jugador.ahorrar()
    else:
        print("Opción inválida")

    jugador.reflexionar()

print("\nEl dinero se acabó")
print("Nivel de arrepentimiento:", jugador.arrepentimiento)
