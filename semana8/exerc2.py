def listmagiclol(list,ratinglist):
    for i in range(9):
        print(f"{list[i]} = {ratinglist[i]}")
    
def foodrating(list,ratinglist):
        try:
            counter=0
            for i in range (9):
                rating = int(input(f"Digite uma avaliação de 1-10 para o item: {list[i]}"))
                assert rating > 0 and rating <= 10, "O Numero não é aceito na avaliação"
                counter=+ 1
                ratinglist.append(rating)
                
                
                    
            return ratinglist
        except ValueError:
            raise
            #print("Valor Invalido")
            #return foodrating(list,ratinglist)
        except BaseException as error:
            raise
            #print(f"Ocorreu um erro: {error}")
            #return foodrating(list,ratinglist)
def main():
    list= ["Maça","Banana","Abacaxi","Pera","Miojo","Bife","Batata","Carne Humana","Carne de Gato"]
    ratinglist=[]
    ratinglist=foodrating(list,ratinglist)
    listmagiclol(list,ratinglist)
main()