class GameCharacter:
    def __init__(self,name=""):
        self._name=name
        self._health=100
        self._mana=50
        self._level=1
    @property    
    def name(self):
        return self._name 
    @property       
    def health(self):
        return self._health
    @health.setter
    def health(self,health):
        if health<0:
            self._health=0
        if health>100:
            self._health=100
        if 0<=health<=100:
            self._health=health
    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self,mana):
        if mana<0:
            self._mana=0
        if mana>50:
            self._mana=50
        if 0<=mana<=50:
            self._mana=mana
    def level(self):
        return self._level        
    

