i=0
while True:
    i+=1
    b=2    
    while True:       
        if b==i:
            print (i)
            break
        elif i%b==0:           
            break
        b+=1
        if b>i:
            break