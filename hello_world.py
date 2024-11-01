

class Car:
    def __init__ (self, brand):
        self.brand = brand

    def show_brand(self):

        print(f"The car brand is: {self.brand}")
    
    def change_brand(self, new_brand):
        self.brand = new_brand
        print(f"The car brand has been changed to: {self.brand}")

    def models(self, models):

        self.models = models

    def engine (self, engines):
        self.engines = engines

    def prices(self, prices):
        self.prices = prices
        

    def car_info (self, engines, models, prices):
        for model, engine, price in zip(models, engines, prices):
            print(f"The {model} has engine type of {engine} and the price is {price}")


mercedes = Car("Mercedes")
mercedes.car_info(
    engines = ["V8", "V12"],
    models = ["C200", "S550"],
    prices = ["Kes 2M", "Kes 10M"]
)


    





