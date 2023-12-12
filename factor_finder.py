# Determin the factors of a number and then return the pth element of the list sorted ascending. 
# if there is not pth element return 0. Example: n=20, p=3, the factors of 20 in ascending order are {1,2,4,5,10,20}. 
# Using 1-based indexing , if p =3, then 4 is returned. if p>6, 0 would be returned. 

# Function description: 
#     Complete the function pthFactor ,
#     pthFactor has the following parameters: long int n: the integer whose factors are to be found 
#     long int p: the index of the factor to be returned. 

# Returns: 
#     long int : the value of the pth integer factor of n or if there is no factor at that index, then 0 is returned
    
# Constraints: 
#     1<=n<= 10^15 
#     1<= p <= 10 ^ 9 

def factors(n):
    factor_list = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factor_list.append(i)
            if i != n // i:
                factor_list.append(n // i)
    return factor_list

def pthFactor(n, p):
    factor_list = factors(n)
    factor_list.sort()
    if p <= len(factor_list):
        return factor_list[p - 1]
    else:
        return 0

# Example usage
n = 20
p = 3
result = pthFactor(n, p)
print(result)  # Output: 4
