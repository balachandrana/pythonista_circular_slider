import ui
from circularslider import CircularSlider

def slider_action(sender):
    sender.superview['view1'].value = sender.value
    
def circular_slider_action(sender):
    sender.superview['slider1'].value = sender.value
    
v = ui.load_view()
v['view1'].continuous = True
v['view1'].image = ui.Image.named('Dog_Face')
v['view1'].action = circular_slider_action
v.present('sheet')
