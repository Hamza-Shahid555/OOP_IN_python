class Car:
    @staticmethod
    def start():
        print("Car is starting")

    @staticmethod
    def stop():
        print("Car is stopping")    

    class ToyotaCar(Car):
        def __init__(self, name):
            self.name=name

        def toytaCar(self):
            print(f"{self.name} is a toyta car")

car1=Car()
car1.start()
car2=Car()
car2.stop()