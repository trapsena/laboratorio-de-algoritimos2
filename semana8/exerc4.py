def listmagiclol(list,finder):
    print(f"O indice{finder} na lista corresponde ao: {list[finder]}")
    
def find_element(list):
    
        try:
            finder = int(input(f"Coloque um numero indice para ser localizado na lista: \n"))
            if finder < 0 or finder > len(list):
                raise IndexError("O numero escolhido não está na lista ")
                     
            return finder
        except ValueError:
             print("Valor Invalido")
             return find_element(list)
        except BaseException as error:
             print(f"Ocorreu um erro: {error}")
             return find_element(list)
def main():
    list= [1,2,3,4,5,6,7,8,9]
    finder=find_element(list)
    listmagiclol(list,finder)
main()