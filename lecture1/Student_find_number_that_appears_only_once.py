def find(lissy):
    digit1 = ''
    digit2 = ''
    last_digit = len(lissy) - 1
    for i in range(0, last_digit): 
        for j in range(0, last_digit): 
             if i != j:
                 digit1 = lissy[i]
                 digit2 = lissy[j]
                 if digit1 == digit2: 
                     return digit1     
     
             else: 
                 return "nothing matches" 
        
    return -1

def main():
    l1 = [7,1,5,3,6,4,7,1,5,6,4]
    l2 = [7,6,4,3,2,1,1,2,3,4,5,6,7]
    print(find(l1)) # expect: 3
    print(find(l2)) # expect: 5

if __name__ == '__main__':
    main()
