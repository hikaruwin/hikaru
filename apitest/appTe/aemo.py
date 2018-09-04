# coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from time import gmtime, strftime # this equls cv codes #...
from random import random

# class TutorialApp(App):
#     def build(self):
#         s = Scatter()
#         l = Label(text='WangYing', font_size=150)
#         s.add_widget(l)
#         return s

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        colour = (random(), 1, 1)
        with self.canvas:
            Color(*colour, mode='hsv')
            d = 30
            Ellipse(pos=(touch.x-d/2, touch.y-d/2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__=='__main__':
    MyPaintApp().run()