test=[1,2,3,4,5,6,7,8,9]

def findMissingNumber(array,n):
    sum1= n*(n+1)/2
    sum2= sum(array)
    result = int(sum1) - int(sum2)
    return result

print(findMissingNumber(test,10))