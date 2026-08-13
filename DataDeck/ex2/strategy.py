from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability
from typing import Any


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class StrategyError(Exception):
    def __init__(self, creature: Creature, strategy: str) -> None:
        strategy_name = strategy.replace("Strategy", "").lower()
        message = (
            f"Battle error, aborting tournament: "
            f"Invalid Creature '{creature.name}' "
            f"for this {strategy_name} strategy"
        )
        super().__init__(message)


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise StrategyError(creature, self.__class__.__name__)
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise StrategyError(creature, self.__class__.__name__)
        target: Any = creature
        msg = target.transform()
        msg += "\n" + target.attack()
        msg += "\n" + target.revert()
        return msg

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise StrategyError(creature, self.__class__.__name__)
        target: Any = creature
        msg = target.attack()
        msg += "\n" + target.heal()
        return msg

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
