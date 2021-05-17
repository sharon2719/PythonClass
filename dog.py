class Dog:
    family_pet="Johnson's"

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        return f"{self.name} barks Wooh-Wooh!" 

    def jumps(self):
        return f"It jumps up and down showing its {self.color} spots"

    def pant(self):
        return f"{self.name} is always panting during the hot season.Its{self.color} spots glow in the sun."
        