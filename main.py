from kivy.app import App
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.label import Label
from plyer import filechooser
from kivy.clock import Clock
import pandas as pd

Window.size = (1000, 600)


class Image_btn(ButtonBehavior, Image):
    pass


class Interface(BoxLayout):

    def binder(self, checkbox, value):
        if value:
            print(self.obj_dict[checkbox], "added")
        else:
            print(self.obj_dict[checkbox], "removed")

    def uploader(self, dt):
        self.obj_dict = dict()
        self.column_dict =dict()
        files = filechooser.open_file(title="Choose excel files", filters=[("*.xlsx")], multiple=True)
        for file in files:
            file_name = file.split("\\")[-1]
            box = BoxLayout(size_hint_y=None, height=70, padding=[30, 0, 0, 0])
            checkbox = CheckBox(size_hint_x=.25, background_checkbox_normal="checkbox_nor.png",
                                background_checkbox_down="checkbox_tic.png")
            checkbox.bind(active=self.binder)
            label = Label(text=f"[color=#3f51b5]{file_name}[/color]", markup=True, text_size=(150, 75))
            box.add_widget(checkbox)
            box.add_widget(label)
            self.ids.file_placeholder.add_widget(box)
            self.obj_dict[checkbox] = file_name
        print(self.obj_dict)
        columns = pd.read_excel(files[0]).columns.values.tolist()
        for column in columns:
            box = BoxLayout(size_hint_y=None, height=30, padding=[30, 0, 0, 0])
            checkbox = CheckBox(size_hint_x=.25, background_checkbox_normal="checkbox_nor.png",
                                background_checkbox_down="checkbox_tic.png")
            label = Label(text=f"[color=#3f51b5]{column}[/color]", markup=True, text_size=(150, 30))
            box.add_widget(checkbox)
            box.add_widget(label)
            self.ids.property_placeholder.add_widget(box)
            self.column_dict[checkbox] = column
        print(self.column_dict)
        self.ids.upload_btn.source = "Drag.png"

    def upload_menu(self):
        self.ids.upload_btn.source = "Drop.png"
        Clock.schedule_once(self.uploader)

    def switching(self):
        self.ids.sm.current = "visualizer_window"


class VisualizerApp(App):
    pass


VisualizerApp().run()
