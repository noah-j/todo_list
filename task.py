

from datetime import *

class Task():


    def __init__(self,name):

        self.name = name

        gen_date = False
        self.gen_date = gen_date
        if not gen_date:
            self.gen_date = date.today()

        self.color = self.color_picker(self.days_on_list())


    def days_on_list(self):

        today = date.today()
        num_days = today - self.gen_date
        print num_days
        return int(num_days.days)

    def color_picker(self,dayCount):

        color_list = [(0,0,255),(0,128,255),(0,255,255),(0,255,128),(0,255,0),
                      (128,255,0),(255,255,0),(255,128,0),(255,0,0)]

        task_color = self.color_formatter(color_list[0])

        if dayCount in range(len(color_list)):
            task_color = self.color_formatter(color_list[dayCount])
            return task_color

        elif dayCount >= range(len(color_list)):
            task_color = self.color_formatter(color_list[-1])
            return task_color

        else:
            return task_color

    def color_formatter(self, color):
        tk_color = "#%02x%02x%02x" % (color[0],color[1],color[2])
        return tk_color