from kivy.app import App
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from plyer import filechooser
from kivy.clock import Clock

Window.size = (1000, 600)


class Image_btn(ButtonBehavior, Image):
    pass


class Interface(BoxLayout):

    def uploader(self, dt):
        files = filechooser.open_file(title="Choose excel files", filters=[("*.xlsx")], multiple=True)
        print(files)
        self.ids.upload_btn.source = "Drag.png"

    def upload_menu(self):
        self.ids.upload_btn.source = "Drop.png"
        Clock.schedule_once(self.uploader)

    def switching(self):
        self.ids.sm.current = "visualizer_window"


class VisualizerApp(App):
    pass


VisualizerApp().run()
