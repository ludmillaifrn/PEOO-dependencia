class Cavalo :
    " " " modela um cavalo """
    def __init__(self , nome , raca , cor , idade , peso ) :
        self.nome = nome 
        self.raca = raca 
        self.cor = cor 
        self. idade = idade 
        self. peso = peso 

    def andar (self):
        print ( "{} está parado")

    def correr (self): 
        print ( "{} está correndo ")

    def deitar (self):
       print ("{} está deitado ")

