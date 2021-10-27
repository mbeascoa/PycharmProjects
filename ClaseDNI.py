class DNI :
    letraDNI=""
    strNumeroDNI=""



    def calculoLetra(self , stringNumeroDNI):
        self.strNumeroDNI = stringNumeroDNI
        resultado=""
        codigo=""
        resto= 0
        resto = int(self.strNumeroDNI) % 23
        codigo = "TRWAGMYFPDXBNJZSQVHLCKET"
        resultado=  codigo[resto:resto + 1]
        return resultado