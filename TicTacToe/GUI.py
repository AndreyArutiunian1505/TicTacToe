# Библеотека для демки
import random

# Библиотеки для интерфейса
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

# Библеотека для захвата нажатия кнопки
from functools import partial

# Конфигурация размера окна
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')

# Класс приложения
class TicTacToe(App):
    arr = ['', '', '', '', '', '', '', '', '']
    bl = GridLayout(rows=3, cols=3)
    buttons = []
    steps = 0
    label = Label(text='...')

    # Ставим крестик
    def post_x(self, instance):
        instance.disabled = True
        instance.color = [0, 0, 1, 1]
        instance.text = 'X'
        self.post_zero()
        self.steps += 1

    # Основа приложения
    def build(self):
        self.create_new()
        root = BoxLayout(orientation='vertical', padding=5)
        self.label.size_hint = (1, .1)
        root.add_widget(self.label)
        root.add_widget(self.bl)
        return root

    # Обрабатываю нажатие кнопок
    def hold_button_num(self, x, instance):
        self.post_x(instance=instance)

        self.arr[x] = instance.text
        print(self.arr[0], self.arr[1], self.arr[2])
        print(self.arr[3], self.arr[4], self.arr[5])
        print(self.arr[6], self.arr[7], self.arr[8])

        if self.arr[0] == 'X' and self.arr[1] == 'X' and self.arr[2] == 'X' or self.arr[3] == 'X' and \
                self.arr[4] == 'X' and self.arr[5] == 'X' or self.arr[6] == 'X' and self.arr[7] == 'X' \
                and self.arr[8] == 'X' or self.arr[2] == 'X' and self.arr[5] == 'X' and self.arr[8] == 'X'\
                or self.arr[0] == 'X' and self.arr[4] == 'X' and self.arr[8] == 'X' or self.arr[2] == 'X' \
                and self.arr[4] == 'X' and self.arr[6] == 'X' or self.arr[1] == 'X' and self.arr[4] == 'X' \
                and self.arr[7] == 'X' or self.arr[0] == 'X' and self.arr[3] == 'X' and self.arr[6] == 'X':
            self.label.text = 'WIN!'
            self.create_new()
        elif self.arr[0] == '0' and self.arr[1] == '0' and self.arr[2] == '0' or self.arr[3] == '0' \
                and self.arr[4] == '0' and self.arr[5] == '0' or self.arr[6] == 'X' and self.arr[7] == '0' \
                and self.arr[8] == '0' or self.arr[2] == '0' and self.arr[5] == '0' and self.arr[8] == '0' \
                or self.arr[0] == '0' and self.arr[4] == '0' and self.arr[8] == '0' or self.arr[2] == '0' \
                and self.arr[4] == '0' and self.arr[6] == '0' or self.arr[1] == '0' and self.arr[4] == '0' \
                and self.arr[7] == '0' or self.arr[0] == '0' and self.arr[3] == '0' and self.arr[6] == '0':
            self.label.text = 'LOSE!'
            self.create_new()
        else:
            if self.arr[x] != '' and self.steps == 5:
                self.label.text = 'DRAW!'
                self.create_new()

    # Ставим нолик
    def post_zero(self):
        coordinate = random.randint(0, 8)
        if self.buttons[coordinate].text == '':
            self.buttons[coordinate].text = '0'
            self.arr[coordinate] = self.buttons[coordinate].text
            self.buttons[coordinate].disabled = True
            self.buttons[coordinate].color = [1, 0, 0, 1]
        else:
            for i in range(9):
                if self.buttons[i].text == '':
                    self.buttons[i].text = '0'
                    self.arr[i] = self.buttons[i].text
                    self.buttons[i].disabled = True
                    self.buttons[i].color = [1, 0, 0, 1]
                    break

    # Создаю новую игру
    def create_new(self):
        self.buttons = []
        self.steps = 0
        self.bl.clear_widgets()
        for i in range(9):
            self.arr[i] = ''
            btn = Button(text='', font_size=84)
            self.buttons.append(btn)
            self.bl.add_widget(self.buttons[i])
            self.buttons[i].bind(on_release=partial(self.hold_button_num,  i))

# Запускаю
if __name__ == '__main__':
    TicTacToe().run()
