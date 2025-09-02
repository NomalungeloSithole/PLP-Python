# ===============================
# Assignment 1: Smartphone Class
# ===============================

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.model} is calling {number}")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Inheritance
class MusicSmartphone(Smartphone):
    def __init__(self, brand, model, storage, audio_quality):
        super().__init__(brand, model, storage) 
        self.audio_quality = audio_quality

    def play_music(self, song):
        print(f"{self.model} is playing '{song}' with {self.audio_quality} audio 🎶")

    # Polymorphism
    def info(self):
        print(f"🎵 Music Smartphone - {self.brand} {self.model}, {self.storage}GB, Audio: {self.audio_quality}")


# Create Objects
phone1 = Smartphone("Apple", "iPhone 15", 256)
phone2 = MusicSmartphone("Sony", "Xperia Music Pro", 512, "Hi-Res Audio")

print("\n--- Smartphone Demo ---")
phone1.info()
phone1.call("+123456789")

phone2.info()
phone2.play_music("Bohemian Rhapsody - Queen")



# ====================================
# Activity 2: Polymorphism Challenge
# ====================================

class Vehicle:
    def move(self):
        print("The vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("The car is driving")


class Plane(Vehicle):
    def move(self):
        print("The plane is flying")


class Boat(Vehicle):
    def move(self):
        print("The boat is sailing")


print("\n--- Polymorphism Demo ---")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
