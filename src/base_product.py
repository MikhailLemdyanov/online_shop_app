from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, родительский для класса продуктов"""

    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
