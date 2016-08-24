import ui
from math import pi,atan2

class CircularSlider(ui.View):
    def __init__(self,*args,**kwargs):
        ui.View.__init__(self,*args,**kwargs)
        self.image = None
        self.a = 0
        self.value = (self.a+pi)/(2*pi)
        self.action = None
        self.continuous = False

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value):
        if value < 0:
            self.__value = 0
        elif value > 1.0:
            self.__value = 1.0
        else:
            self.__value = value
        self.a = (self.__value - 0.5)*2*pi
        self.set_needs_display()
        
                        
    def draw(self):
        scl=min(self.width,self.height)
        self.scl=scl
        btn_siz=min(22/scl,0.05)
        #work in normalized units
        ui.concat_ctm(ui.Transform.scale(scl,scl))
        #origin at center
        ui.concat_ctm(ui.Transform.translation(.5,.5))
        ui.set_color('#d0d0d0')
        o = ui.Path.oval(-.5+btn_siz, -.5+btn_siz, 1-2*btn_siz, 1-2*btn_siz)
        o.line_width=2/scl
        o.stroke()
        if self.image:
            self.image.draw(-.5+2*btn_siz, -.5+2*btn_siz, 1-4*btn_siz, 1-4*btn_siz)
        #rotate by angle
        ui.concat_ctm(ui.Transform.rotation(self.a))
        ui.set_color(self.tint_color if self.tint_color else '#1aa1b5')
        arc = ui.Path()
        arc.move_to(.5-btn_siz, 0)
        ang = -(self.a+pi)
        arc.add_arc(0, 0, .5-btn_siz, 0, ang, False)
        arc.line_width=2/scl
        arc.stroke()
        # center origin at button
        ui.concat_ctm(ui.Transform.translation(.5-btn_siz,0))
        #optional: to keep images upright
        #ui.concat_ctm(ui.Transform.rotation(-self.a))
        p=ui.Path.oval(-btn_siz,-btn_siz,2*btn_siz,2*btn_siz)
        p.fill()

    def touch_moved(self,touch):
        dp=touch.location-touch.prev_location
        self.a=atan2(touch.location.y-self.scl/2.,touch.location.x-self.scl/2.)
        self.value = (self.a+pi)/(2*pi)
        if self.continuous:
            if self.action:
                self.action(self)
        self.set_needs_display()
        
    def touch_ended(self, touch):
        #print(self.value)
        if self.action:
            self.action(self)        

                
if __name__ == '__main__':
    ''' _use_theme = False
    w = h = 600
    f = (0, 0, w, h)
    mc = MyClass(frame=f, bg_color='white', name='Silly Demo')
    
    if not _use_theme:
        mc.present('sheet', animated=False)
    else:
        editor.present_themed(mc, theme_name='Oceanic', style='sheet',
                              animated=False)'''
    cs = CircularSlider(frame=(0,0,500, 500),bg_color='white')
    cs.present('sheet')
