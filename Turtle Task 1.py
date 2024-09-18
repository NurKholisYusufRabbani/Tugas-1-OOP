import turtle

# Definisikan class untuk TurtleKuraKura
class TurtleKuraKura:
    # Constructor untuk mengatur turtle dan ukuran
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color("red")
        self.t.speed(4)

    # Method untuk menggerakkan kura-kura dalam bentuk persegi sebagai contoh
    def gerak(self, size):
        for _ in range(3):
            self.t.forward(size)
            self.t.left(120)

    # Method untuk menutup jendela turtle
    def selesai(self):
        turtle.done()

# Membuat objek dari class TurtleKuraKura
kura = TurtleKuraKura()

# Menggerakkan kura-kura
kura.gerak(200)
kura.selesai()
