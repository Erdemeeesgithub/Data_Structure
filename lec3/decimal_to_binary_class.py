# Suppose n is a positive integer, n >= 0 .
# Convert n to its binary representation without using any library function.

def recursive_decimal_to_binary_str(n):
    
    if n < 2:               
        return str(n)
    return recursive_decimal_to_binary_str(n // 2) + str(n % 2)
    # binary = ''
    # if n % 2 == 0:
    #     binary = binary + "0" 
    # else:
    #     binary = binary + "1" 
    # n = n//2
    # recursive_decimal_to_binary_str(n, binary)






def main():
    print(recursive_decimal_to_binary_str(6)) #110
    print(recursive_decimal_to_binary_str(13)) #1101
    print(recursive_decimal_to_binary_str(126)) #1111110
    print(recursive_decimal_to_binary_str(509)) #111111101
    
	
if __name__ == '__main__':
    main()
