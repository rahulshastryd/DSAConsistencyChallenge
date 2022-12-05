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
