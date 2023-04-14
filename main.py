# Back-end

# I used kivy library to create the graphic interface of this application 
# It was necessary to installed it: pip install kivy

# To import the App
# To import the Builder - that will allow to connect the screen.kv to main.py
# To creat the App
# To creat the build function

# To import the App
from kivy.app import App

# To import the Builder - that will allow to connect the screen.kv to main.py
from kivy.lang import Builder

# Graphical User Interface
GUI = Builder.load_file("screen.kv")

# It's my application
class Application(App):
    
    # Basic function - when build the application, show me the screen
    def build(self):
        return GUI
    
    # Define what will happen when the App is open
    def on_start(self):
        
        # root is the screen.kv
        self.root.ids["base_message"].text = "Digite o nº da base do número que você vai digitar:"
        self.root.ids["number_message"].text = "Digite o seu número:"
        self.root.ids["decimal_number"].text = "Decimal:"
        self.root.ids["binary_number"].text = "Binário:"
        self.root.ids["octal_number"].text = "Octal:"
        self.root.ids["hexadecimal_number"].text = "Hexadecimal:"

# To run the application    
Application().run()
    