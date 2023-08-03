# Claire is mentoring a group of students to participate in the upcoming Women’s Day Mathematics Challenge. In one of her classes, she plans to teach modulo arithmetic to the girls. She takes an array of numbers and asks the girls to perform the following operation: pick two adjacent positive numbers, ai and ai+1, and replace the two numbers with either (ai % ai+1) or (ai+1 % ai), where x % y denotes x modulo y. Thus, after each operation, the length of the array decreases by 1.
# Claire asks the firls to find the minimum length possible of the array which can be achieved by performing the above operation any number of times.

# Example:

# Consider, the length of the array to be n = 4., and the array of numbers to be arr=[1,1,2,3].

# The following sequence of operations can be performed(considering 1based indexing):

# 1. arr=[1,1,2,3]: Choose i = 3, thus arr[i] = 2 and arr[i + 1] = 3. We get the new value to be given by2 % 3 = 2 or 3 % 2 = 1. The reulting array can thus be [1,1,2] or [1,1,1,]. We consider the former one to minimize the array length.
# 2. arr = [1,1,2]: Choose i = 2, thus arr[i] = 1 and arr[i+ 1] = 2. We canget the new array as [1,1].
# 3. arr = [1,1]: Choose i =1 to get the array [0].

# Thus the minimum possible length for hte above array would be 1.\

def getmMinLength(arr):
    n = len(arr)
