
def check(list1,list2):
    equals =[]
    not_equals = []
    for i in list1:
        if i in list2:
            equals.append(i)
        else:
            not_equals.append(i)
        
    print (f"Iguais: {equals}")
    print(f"Unicos: {not_equals}")
def main():
    list1 = [7, 2, 5, 4]
    list2 = [4, 6, 8, 2] 


    check(list1,list2)
    
main()