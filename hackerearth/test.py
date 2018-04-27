def presents(*args):
    
    N=[*args]
    
    R=reversed(N)
    
    A=[]
    
    for i in R:
        
        A.append(i)
        
        
    x=[a*b for a,b in zip(N,A)]
    
    print(sum(x))
    
    

if __name__=='__main__':

    presents(1,2,3)

    presents(4,5,6)
