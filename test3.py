import ui
from circularslider import CircularSlider


image_list = [ ui.Image.named(
    i) for i in 'Rabbit_Face Mouse_Face Cat_Face Dog_Face Octopus Cow_Face'.split()]
    
   
def circular_slider_action(sender):
    index = int(sender.value*len(image_list))
    sender.image = image_list[index]

# Set up and present a view with a single button:
v = ui.View(frame=(0,0,500,500), background_color='white')
cslider = CircularSlider(frame=(0,0,500, 500))
cslider.action = circular_slider_action
v.add_subview(cslider)
v.present('sheet')
cslider.action(cslider)
