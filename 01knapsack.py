def knapsack(wt,val,W,N):
    dp={}
    def solve(n,cap):
        if n==0 or cap==0:
            return 0
        elif (n,cap) in dp:
            return dp[(n,cap)]
        else:
            cwt=wt[n-1]
            cv=val[n-1]
            if cwt <= cap:
                c1= cv+solve(n-1,cap-cwt)
                c2= solve(n-1,cap)
                c=max(c1,c2)
            else:
                c=solve(n-1,cap)
            dp[(n,cap)]=c
            return c
        
    return solve(N,W)

N=int(input("Enter number of items: "))
W=int(input("Enter max capacity of knapsack: "))
wt=list(map(int,input("Enter weights of items (space separated)").split()))
val=list(map(int,input("Enter values of items (space separated)").split()))

res=knapsack(wt,val,W,N)
print("The maximum value that can be achieved is:",res)