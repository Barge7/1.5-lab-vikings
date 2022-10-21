
import random
# Soldier


class Soldier:
    
    def __init__(self,health,strength):
        
        self.health = health
        self.strength = strength
            
    def attack(self):
            
        return self.strength
        
    def receiveDamage(self,damage):
            
        self.health -= damage


class Viking(Soldier):
    
    def __init__(self,name,health,strength):
        
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self,damage):
        
        self.health -= damage
           
        if self.health > 0:
            return self.name + ' has received ' + str(damage) + ' points of damage'
        
        else:
            return self.name + ' has died in act of combat'
    
    
    def battleCry(self):
        return 'Odin Owns You All!'


class Saxon(Soldier):
    
    def __init__(self,health,strength):
        
        
        self.health = health
        self.strength = strength
        
    def receiveDamage(self,damage):
        
        self.health -= damage
           
        if self.health > 0:
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        
        else:
            return 'A Saxon has died in combat'
    


class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
          
    
    def addViking(self,Viking): 
            
        self.vikingArmy.append(Viking)
        
                      
    def addSaxon(self,Saxon):
            
        self.saxonArmy.append(Saxon)        
        
        
    
    def vikingAttack(self):
        
        sajon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)
        
        vida = sajon.receiveDamage(vikingo.strength)
        
        if sajon.health <= 0:
            self.saxonArmy.remove(sajon)
            
        return vida
        
               
        
    def saxonAttack(self):
        
        sajon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)
        
        vida = vikingo.receiveDamage(sajon.strength)
        
        if vikingo.health <= 0:
            self.vikingArmy.remove(vikingo)
            
        return vida
                
        
        
    def showStatus(self):
        
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            
            return 'Vikings have won the war of the century!'
        
        if len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            
            return 'Saxons have fought for their lives and survive another day...'
        
        else:
            return 'Vikings and Saxons are still in the thick of battle.'

        
    
