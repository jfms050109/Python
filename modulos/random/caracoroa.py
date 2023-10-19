import random
while True:
    moeda=['cara','coroa']    
    resp=input('cara ou coroa?\n')
    if(resp.lower()=='exit'):break
    print(moeda[random.randrange(0,2)])