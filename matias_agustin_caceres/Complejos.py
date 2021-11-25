class Compejo:
    
    
    def __init__ (self, parte_real, parte_imaginaria):
        self.parte_real = parte_real
        self.parte_imaginaria = parte_imaginaria

    
    def suma(self, numero_a_sumar):
        self.parte_real = self.parte_real + numero_a_sumar.parte_real
        self.parte_imaginaria = self.parte_imaginaria + numero_a_sumar.parte_imaginaria
    
    def resta(self, numero_a_restar):
        self.parte_real = self.parte_real - numero_a_restar.parte_real
        self.parte_imaginaria = self.parte_imaginaria - numero_a_restar.parte_imaginaria
    
    def multiplicacion (self, numero_a_multiplicar):
        factor_i_al_cuadrado = -1
        parte_a = self.parte_real * numero_a_multiplicar.parte_real
        parte_b = self.parte_real * numero_a_multiplicar.parte_imaginaria
        parte_c = self.parte_imaginaria * numero_a_multiplicar.parte_real
        parte_d = ((self.parte_imaginaria * numero_a_multiplicar.parte_imaginaria) * factor_i_al_cuadrado)
        self.parte_real = parte_a + parte_d
        self.parte_imaginaria = parte_c + parte_b

    def division (self, numero_a_dividir):
        factor_i_al_cuadrado = -1
        parte_a = self.parte_real / numero_a_dividir.parte_real
        parte_b = self.parte_real / numero_a_dividir.parte_imaginaria
        parte_c = self.parte_imaginaria / numero_a_dividir.parte_real
        parte_d = ((self.parte_imaginaria / numero_a_dividir.parte_imaginaria) * factor_i_al_cuadrado)
        self.parte_real = parte_a + parte_d
        self.parte_imaginaria = parte_c + parte_b   