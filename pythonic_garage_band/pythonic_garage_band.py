from abc import abstractmethod

class Musician():
    """
    A super class to handle common 
    functionality which particular 
    kinds of musicians that will inherit from it.
    """
    def __init__(self,arr):
        self.members = arr
    @abstractmethod
    def __str__(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass
    @abstractmethod
    def get_instrument(self):
        pass
    @abstractmethod
    def play_solo(self):
        pass

class Band(Musician):
    """
    Band class that inherit musican calss also have
    play_solos method that asks each member musician to play a solo, 
    in the order they were added to band.
    and have class method to_list which returns a list of previously created.
    """
    instances = []
    def __init__(self,name,arr):
        self.name=name
        super().__init__(arr)
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        return cls.instances
    def play_solos(self):
        solos=[]
        for i in self.members:
            solos.append(i.play_solo())
        return solos
    def __str__(self):
        return f'our name is {self.name}, and we rock'
    def __repr__(self):
        return f"Band instance. Name = {self.name}"


class Guitarist(Musician):
    """
    Kind of the class Musician that have two static methods 
    get_instrument and play_sole that returns string.
    """
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod
    def play_solo():
        return "face melting guitar solo"
        

class Drummer(Musician):
    """
    Kind of the class Musician that have two static methods 
    get_instrument and play_sole that returns string.
    """
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "drums"
    @staticmethod
    def play_solo():
        return "rattle boom crash"
    

class Bassist(Musician):
    """
    Kind of the class Musician that have two static methods 
    get_instrument and play_sole that returns string.
    """
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "bass"
    @staticmethod
    def play_solo():
        return "bom bom buh bom"
