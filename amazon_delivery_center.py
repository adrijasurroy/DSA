#Amazon has multiple delivery centers and delivery warehouses all over the world! The world is represented by a number line from -10^9 to 10^9. There are n delivery centers, the ith one at location center[i]. A location x is called a suitable location for a warehouse if it is possible to bring all the products to that point by travelling a distance of no more than d. At any one time, products can be brought from one delivery center and placed at point x. Given the positions of n delivery centers, calculate the number of suitable locations in the world. That is, calculate the number of points x on the number line (-10^9 <= x<=10^9) where the travel distance required to bring all the products to that point is less than or equal to d.
#Note: The distance between point x and center[i] is x-center[i], their absolute distance.

#Example:
#Given n=3, center = [-2, 1, 0], d=8
#The various locations along with the distance traveled to bring all treasures at that point are:
#- Locate the warehouse at x = -3: First bring products from center[0] = -2 covering a distance of |-3 - (-2)| = 1 to reach the center and |-3-(-2)|=1 to return. Similarly we bring products from centers 1 and 2 to point -3 for total distance of 1+1+4+4+3+3 =16 which is >d. This is not a suitable location.
#-Locate warehouse at x=0, total distance traveled is 2*|0-(-2)| + 2*|0-1| + 2*|0-0| = 6 <= d. This is a suitable location.
#-Locate the warehouse at x=-1, total distance traveled is 2*|-1-(-2)| + 2*|-1-1| + 2*|-1-0| = 8 <=d. This is a suitable location.
#-Locate the warehouse at x=1, total distance traveled is 2*|1-(-2)| + 2*|1-1| + 2*|1-0| = 8 <= d. This is a suitable location.
#Thus the only suitable locations are {-1, 0, 1}. Return 3.

#Function Description:
#Complete the function suitableLocations
#suitableLocations has the following parameters:
#int center[n]: the positions of delivery centers
#long d: the maximum total travel distance for a suitable location

#Returns:
#int : the number of suitable locations.

#Constraints:
#1<=n<=10^5
#-10^9<=center[i]<=10^9
#0<=d<=10^15

def count_suitable_locations(center, d):
    center.sort()
    n = len(center)
    count=0
    print(center)
    for i in range(n-1):
        cent = [j for j in range(center[i],center[i+1]+1)]
        print(cent)
        count += count_recursive(center, d, 0, len(cent)-1)
    return count


def count_recursive(center, d, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2
    mid_location = center[mid]

    count_left = count_recursive(center, d, left, mid - 1)
    count_right = count_recursive(center, d, mid + 1, right)

    count = count_left + count_right

    for i in range(left, right + 1):
        count += min(abs(mid_location - center[i]), d)

    return count


# Example usage
center = [2, 0, 3, -4]
d = 22
result = count_suitable_locations(center, d)
print(result)