import ui
from circularslider import CircularSlider

def slider_action(sender):
    sender.superview['view1'].value = sender.value
    
def circular_slider_action(sender):
    sender.superview['slider1'].value = sender.value
    
v = ui.load_view()
v['view1'].image = ui.Image.named('Snake')
v['view1'].tint_color = 'red'
v['view1'].action = circular_slider_action
v.present('sheet')
