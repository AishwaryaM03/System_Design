
from abc import ABC, abstractmethod


# 1. Abstract Products

class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


# 2. Concrete Products - Modern Family

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair"


class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a modern sofa"


# 3. Concrete Products - Victorian Family

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair"


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa"


# 4. Abstract Factory

class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


# 5. Concrete Factories

class ModernFactory(FurnitureFactory):

    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


class VictorianFactory(FurnitureFactory):

    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()


# 6. Client Code

def furnish_room(factory: FurnitureFactory):

    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(chair.sit_on())
    print(sofa.lie_on())


# 7. Main Program

if __name__ == "__main__":

    print("Modern Furniture:")
    modern_factory = ModernFactory()
    furnish_room(modern_factory)

    print("\nVictorian Furniture:")
    victorian_factory = VictorianFactory()
    furnish_room(victorian_factory)
