from abc import ABC, abstractmethod
from .creature import Creature, Aquabub, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """
    the super factory to produce other factories with common interfaces
    """
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    """
    a concrete factory to create a concrete product
    """
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
