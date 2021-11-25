class Matriz_3x3:

    def __init__ (self, numero_1,  numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9,):
        self.matriz = [ [numero_1, numero_2, numero_3], [numero_4, numero_5, numero_6], [numero_7, numero_8, numero_9] ]


    def suma (self, matriz_a_sumar):

        for i in range(3):

            for j in range(3):

                self.matriz[i][j] = self.matriz[i][j] + matriz_a_sumar[i][j]


    def resta (self, matriz_a_resta):

        for i in range(3):

            for j in range(3):

                self.matriz[i][j] = self.matriz[i][j] + matriz_a_resta[i][j]
                      

    
