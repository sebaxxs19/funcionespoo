import tkinter as tk
import random



# Lógica del Black Jack
def crear_mazo():
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos = ['♠', '♥', '♦', '♣']
    return [(v, s) for v in valores for s in palos]

def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    if carta[0] == 'A':
        return 11
    return int(carta[0])

def calcular_mano(mano):
    total = sum(valor_carta(c) for c in mano)
    ases = sum(1 for c in mano if c[0] == 'A')
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

# Interfaz gráfica
class BlackJack:
    def __init__(self, root):
        self.root = root
        self.root.title("Black Jack")
        self.dinero = 500
        self.mazo = crear_mazo()
        random.shuffle(self.mazo)
        self.init_gui()

    def init_gui(self):
        self.info = tk.Label(self.root, text=f'Dinero: ${self.dinero}', font=('Arial', 14))
        self.info.pack()

        self.apuesta_entry = tk.Entry(self.root)
        self.apuesta_entry.pack()
        self.apuesta_entry.insert(0, '100')

        self.mensaje = tk.Label(self.root, text='', font=('Arial', 12))
        self.mensaje.pack()

        self.jugador_lbl = tk.Label(self.root, text='Tus cartas:', font=('Arial', 12))
        self.jugador_lbl.pack()

        self.crupier_lbl = tk.Label(self.root, text='Cartas del crupier:', font=('Arial', 12))
        self.crupier_lbl.pack()

        self.btn_iniciar = tk.Button(self.root, text='Iniciar ronda', command=self.iniciar_ronda)
        self.btn_iniciar.pack()

        self.btn_pedir = tk.Button(self.root, text='Pedir carta', command=self.pedir_carta, state=tk.DISABLED)
        self.btn_pedir.pack()

        self.btn_plantarse = tk.Button(self.root, text='Plantarse', command=self.plantarse, state=tk.DISABLED)
        self.btn_plantarse.pack()

        self.btn_reiniciar = tk.Button(self.root, text='Reiniciar juego', command=self.reiniciar_juego, state=tk.DISABLED)
        self.btn_reiniciar.pack()

    def iniciar_ronda(self):
        try:
            self.apuesta = int(self.apuesta_entry.get())
            if self.apuesta <= 0 or self.apuesta > self.dinero:
                self.mostrar_mensaje('Apuesta inválida.', 'red')
                return
        except:
            self.mostrar_mensaje('Ingresa un número válido.', 'red')
            return

        if len(self.mazo) < 10:
            self.mazo = crear_mazo()
            random.shuffle(self.mazo)

        self.jugador = [self.mazo.pop(), self.mazo.pop()]
        self.crupier = [self.mazo.pop(), self.mazo.pop()]
        self.btn_pedir.config(state=tk.NORMAL)
        self.btn_plantarse.config(state=tk.NORMAL)
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_reiniciar.config(state=tk.DISABLED)
        self.mostrar_mensaje('', 'black')
        self.actualizar_gui()

    def pedir_carta(self):
        self.jugador.append(self.mazo.pop())
        if calcular_mano(self.jugador) > 21:
            self.mostrar_mensaje('Te pasaste. Pierdes.', 'red')
            self.dinero -= self.apuesta
            self.finalizar_ronda()
        self.actualizar_gui()

    def plantarse(self):
        while calcular_mano(self.crupier) < 17:
            self.crupier.append(self.mazo.pop())

        total_j = calcular_mano(self.jugador)
        total_c = calcular_mano(self.crupier)

        if total_c > 21 or total_j > total_c:
            self.mostrar_mensaje('¡Ganaste!', 'green')
            self.dinero += self.apuesta
        elif total_j == total_c:
            self.mostrar_mensaje('Empate.', 'blue')
        else:
            self.mostrar_mensaje('Perdiste.', 'red')
            self.dinero -= self.apuesta

        self.finalizar_ronda()

    def finalizar_ronda(self):
        self.btn_pedir.config(state=tk.DISABLED)
        self.btn_plantarse.config(state=tk.DISABLED)
        self.btn_iniciar.config(state=tk.NORMAL)
        self.actualizar_gui()
        if self.dinero <= 0:
            self.mostrar_mensaje('Te has quedado sin dinero.', 'red')
            self.btn_iniciar.config(state=tk.DISABLED)
            self.btn_reiniciar.config(state=tk.NORMAL)

    def reiniciar_juego(self):
        self.dinero = 500
        self.mazo = crear_mazo()
        random.shuffle(self.mazo)
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_reiniciar.config(state=tk.DISABLED)
        self.mostrar_mensaje('Juego reiniciado.', 'black')
        self.actualizar_gui()

    def actualizar_gui(self):
        self.info.config(text=f'Dinero: ${self.dinero}')
        self.jugador_lbl.config(text=f'Tus cartas: {" | ".join(f"{v}{s}" for v, s in self.jugador)} ({calcular_mano(self.jugador)})')

        if self.btn_iniciar['state'] == tk.DISABLED:
            crupier_mostrar = [f"{self.crupier[0][0]}{self.crupier[0][1]}", "??"]
        else:
            crupier_mostrar = [f"{v}{s}" for v, s in self.crupier]
        self.crupier_lbl.config(text=f'Crupier: {" | ".join(crupier_mostrar)}')

    def mostrar_mensaje(self, texto, color='black'):
        self.mensaje.config(text=texto, fg=color)

# Ejecutar
root = tk.Tk()
root.geometry("400x300+100+100")  # Ancho x Alto + Posición X + Posición Y
juego = BlackJack(root)
root.mainloop()