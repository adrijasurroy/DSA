# For an array of n strings product and a word to search, design a system that, when each character of the searched word is typed, 
# suggests at most three product names from the product array. 
# The suggested products should share a common prefix with the searched word. 
# If more than three products exist with a common prefix, report the three product names that appear first in the lexicographical order. 
# Return the suggested products which will be a list of lists after each character of the searched word is typed. 
# Note: 
#     A string x is considered lexicographically smaller than  another string y if x will occur before y in the english dictionary.  
# Example: 
#     Suppose n = 5, products = ["carpet", "car", "cat", "camera", "crate"], and search = "camera". 
#     The answer is [["camera", "car", "carpet"],["camera","car","carpet"],["camera"],["camera"],["camera"],["camera"]. 
# Function Description: 
#     Complete the function getProductSuggestions in the editor. 
#     getProductSuggestions has the following parameters: 
#         string product[n]: the list of products, 
#         string search: a string
# Returns: 
#     string[n][]: for each prefix of the string , return a maximum of three lexicographically smallest words with a common prefix.
# Constraints:
# 1<= n<=1000 
# 1<= length of products[i]<=500 
# 1 <= sum(length of products[i]) <= 5 * 10^5 
# all the strings of products are unique 
# products[i] consists of lowercase english letters only 
# 1<= length of search <= 1000 
# The searched text consists of lowercase english letters only

def getProductSuggestions(products, search):
    products.sort()  # Sort products lexicographically
    suggestions = []
    prefix = ""
    
    for char in search:
        prefix += char
        matching_products = []
        count = 0
        
        for product in products:
            if product.startswith(prefix):
                matching_products.append(product)
                count += 1
                if count == 3:
                    break
        
        suggestions.append(matching_products)
    
    return suggestions

# Example usage
products = ["carpet", "car", "cat", "camera", "crate"]
search = "camera"
result = getProductSuggestions(products, search)
print(result)
