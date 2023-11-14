class NegativeNumberError(Exception):
     pass

def mathmagiclol(raiz):
    magic= raiz ** (1/2)

    print(f"A raiz de {raiz} é = {magic}")

def square_root():
    
        try:
            raiz = float(input(f"Digite um numero para ver a sua raiz quadrada:\n"))
            if raiz < 0:
                raise NegativeNumberError("Raiz quadrada de numeros negativos não é real")
                return square_root()
            
            return raiz
    
        except ValueError:
             print("Valor Invalido")
             raise
             return square_root()
        except BaseException as error:
             print(f"Ocorreu um erro: {error}")
             return square_root()
def main():
    raiz=square_root()
    mathmagiclol(raiz)
main()