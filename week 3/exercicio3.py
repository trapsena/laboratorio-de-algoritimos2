def bank(money):
    hund = 0
    fifty = 0 
    twenty = 0
    ten = 0
    if money % 10 == 0:
        while money >= 100:
            money -= 100
            hund += 1
        while money >= 50:
            money -= 50
            fifty += 1
        while money >= 20:
            money -= 20
            twenty += 1
        while money >= 10:
            money -= 10
            ten += 1
            
        print(f"Notas de 100:{hund} ")
        print()
        print(f"Notas de 50:{fifty} ")
        print()
        print(f"Notas de 20:{twenty} ")
        print()
        print(f"Notas de 10:{ten} ")
    else:
        print("Error: amount not suitable for the system")
    
   
def main():
    money=int(input("Digite quanto deseja retirar: "))
    money=bank(money)
main()