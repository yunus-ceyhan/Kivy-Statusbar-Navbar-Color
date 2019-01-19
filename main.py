from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from android.runnable import run_on_ui_thread
from jnius import autoclass


Color = autoclass("android.graphics.Color")
WindowManager = autoclass('android.view.WindowManager$LayoutParams')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

Builder.load_string('''
<MainApp>:
    orientation: 'vertical'
              
    Button:
        text: 'White'
        on_press: root.statusbar("#FFFFFF")

    Button:
        text: 'Red'
        on_press: root.statusbar("#FF0000")

    Button:
        text: 'Green'
        on_press: root.statusbar("#00FF00")

    Button:
        text: 'Blue'
        on_press: root.statusbar("#0000FF")

    Button:
        text: 'Yellow'
        on_press: root.statusbar("#FFFF00")

    Button:
        text: 'Gray'
        on_press: root.statusbar("#808080")

''')

class MainApp(BoxLayout):
    
    @run_on_ui_thread
    def statusbar(self,color):
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color)) 
        window.setNavigationBarColor(Color.parseColor(color))

class TestApp(App):
        
    def build(self):
        return MainApp()
        
if __name__ == '__main__':
    TestApp().run() 
