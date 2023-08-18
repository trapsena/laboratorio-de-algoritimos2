
def invert(list1):
    reverse=[]
    
    for i in range(len(list1)-1,-1,-1):
        reverse.append(list1[i])
        
    print (list1)
    print(reverse)
def main():
    list1=[4,5,6]
    list1=invert(list1)
    
main()