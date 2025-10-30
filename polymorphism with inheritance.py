# polymorphism with inheritance
class widget:
    def render(self):
        pass

class Button(widget):
    def render(self):
        print("Rendering a button")

class TextBox(widget):
    def render(self):
        print("Rendering a text box")

widgets = [Button(), TextBox()]
for widget in widgets:
    widget.render()
