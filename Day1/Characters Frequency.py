Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.

Input Format
First Parameter - string str1

Output Format
Return the array.

Example 1:
Input:
    arfardarb
Output:
    3 3 1 1 1
Explanation:
    a is repeated 3 times, followed by r which is repeated 3 times. f, d and b occurs only 1 time.    
Constraints
1 <= n <= 105
String contains lowercase letters
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Ans:
def solve(str1):
    op={}
    ans=[]
    for i in str1:
        if i in op:
            op[i]+=1
        else:
            op[i]=1
    for key,value in op.items():
        ans.append(value);
    return ans
