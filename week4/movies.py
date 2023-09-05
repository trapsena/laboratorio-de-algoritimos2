
def classes():
    movie= {}
    
    movie["Dragon Ball Z: A Arvore do Poder"] = {"vilao":"Tarles","lançamento":1990}
    movie["Dragon Ball Z: O Poder Invencível"] = {"vilao":"Broly","lançamento":1993}
    movie["Dragon Ball Z: Uma Vingança Para Freeza"] = {"vilao":"Cooler","lançamento":1991}
    movie["Dragon Ball Z: O Retorno de Coola"] = {"vilao":"Metal Cooler","lançamento":1992}
    movie["Dragon Ball Super : Super Hero"] = {"vilao":"Cell Max","lançamento":2022}
    
    for movie, info in movie.items():
        print(f"Filme: {movie}")
        print(f"Vilão: {info['vilao']}")
        print(f"Ano de Lançamento: {info['lançamento']}\n")
    
def main():
    classes()
main()