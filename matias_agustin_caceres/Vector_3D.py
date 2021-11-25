class Vector_R3:
    
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def suma(self, vector_a_sumar):
        self.x = self.x + vector_a_sumar.x
        self.y = self.y + vector_a_sumar.y
        self.z = self.z + vector_a_sumar.z
    
    def resta (self, vector_a_restar):
        self.x = self.x - vector_a_restar.x
        self.y = self.y - vector_a_restar.y
        self.z = self.z - vector_a_restar.z
    
    def multiplicacion (self, vector_a_multiplicar):
        self.x = self.x * vector_a_multiplicar.x
        self.y = self.y * vector_a_multiplicar.y
        self.z = self.z * vector_a_multiplicar.z

    def division (self, vector_a_dividir):
        self.x = self.x / vector_a_dividir.x
        self.y = self.y / vector_a_dividir.y
        self.z = self.z / vector_a_dividir.z 