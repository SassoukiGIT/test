from turtle import*
forme=['rectangle','cercle','triangle',]
couleur['yellow','green','red','purple','blue']
bgcolor('grey')
pensize(10)
choix=numinput('forme','0 rectangle','n 1cercle','n 2tringle','n 3étoile')
#rectangle
if choix==0:
    for i in range(4):
        color(couleur[i])
        forward(300)
        left(90)
#cercle
elif choix==1:
    circle(200)
#triangle
elif choix==2:
    for i in range(3):
        color(couleur[i])
        forward(300)
        left(120)
elif choix==3:        
    for i in range(5):
        color(couleur[i])
        forward(300)
        left(144)
                          
