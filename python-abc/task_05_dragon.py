class SwimMixin:
    """Mixin permettant à une créature de nager."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin permettant à une créature de voler."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe Dragon héritant des mixins SwimMixin et FlyMixin."""
    def roar(self):
        print("The dragon roars!")
