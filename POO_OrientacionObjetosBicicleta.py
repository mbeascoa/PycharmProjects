class Bicicleta:
    color = ""       #son variables de clase que se pueden usar en cualquier
    tamanio = ""     #función dentro de la clase
    Vel_max=15
    velocidad=-1
    def __init__(self):
        self.velocidad = 0


    # este es un constructor, cuando se cree un objeto
    # de tipo bicicleta lo primero que hace es
    # ejecutar el constructor

    def subirmarcha (self):  	 #el self es necesario en el método
        self.velocidad = self.velocidad+1
    def bajarmarcha(self):
        self.velocidad = self.velocidad - 1
    def cambiarVelMax(self,maxVel):
        self.Vel_max = maxVel   # en esta línea se puede quitar el self
    def __str__(self):
            return "Velocidad Actual:" + str(self.velocidad) + ", Velocidad Máxima: " + str(self.Vel_max)

mibici = Bicicleta()
#mibici es una variable de instancia, hemos creado un objeto Bicicleta se lo
# hemos asignado a la variable de insancia

print(mibici.velocidad)
#ha entrado en el constructor y ha inicializado la velocidada cero 0
mibici.subirmarcha()
#entra en el método o función y sube la velocidad a uno, quedando en 1
mibici.subirmarcha()
#entra en el método o función y sube la velocidad a uno, quedando en 2
print(mibici.velocidad)
mibici.bajarmarcha()
#entra en el método o función y baja la velocidad a uno, quedando en 2
print(mibici.velocidad)
mibici.cambiarVelMax(25)
#entra en el método o función cambiar la velocidad máxima a 25
print(mibici.Vel_max)

print (mibici)
