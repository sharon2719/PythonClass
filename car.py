class Car:
    owner="Peter Smith"

    def __init__(self,make,model):
        self.make=make
        self.model=model

    def start(self):
        return f"{self.owner} your car {self.make} starts at ignition."

    def drive(self):
        return f"{self.model} is very comfortable when driving {self.owner}."

    def park(self):
        return f"Dear driver,you have arrived at your destination.Please park {self.make} here."    