class onepiece(object): #parent class
    def __init__(self,name,pos):
        self.name=name
        self.pos=pos
    def display(self):
        print("Name is:",format(self.name))
        print("position is:",format(self.pos))

class onepiecearcs(onepiece): #child class               #inheritance
    def __init__(self,name,pos,arcname,epi):
        self.arcname=arcname
        self.epi=epi

        onepiece.__init__(self,name,pos)
    def info(self):
        print("Name is:",format(self.name))
        print("position is:",format(self.pos))
        print("arc name is:",format(self.arcname))
        print("episode number:",format(self.epi))  

class devilfruit(onepiece):
    def display(self):                               #polymorphism
        print("The flare devilfruit ",format(self.name,self.pos)) 

    

r=onepiecearcs('luffy','captian','wano',1000)  #creating object
r.display()                                    #calling function

m=onepiecearcs('zoro','swordsman','marineford',500)
m.info()

p=devilfruit('Ace','vice-captian')
p.display()
