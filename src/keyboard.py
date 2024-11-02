from src.item import Item


class MixinLanguage:

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self) -> str:
        return self._language

    def change_lang(self) -> None:
        """
        Переключает языковой ввод с клавиатуры.
        """
        if self.language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Item, MixinLanguage):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
