devedores=['minduin','fernando','ana']

print (devedores)

pagou=input("quem pagou?\n")
if  pagou in devedores:
    devedores.remove(pagou)
print(devedores)