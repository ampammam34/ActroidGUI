#!/usr/bin/env python
# -*- coding: cp932 -*-

import Tkinter as tk


my_tuple1 = (("8:left arm up       ",-14,130,0),#L1
                    ("9:left arm open    ",0,56,40),#L2
                    ("10:left upper arm   ",0,90,45),#L3
                    ("11:left elbow       ",0,112,0),#L4
                    ("12:left forearm     ",-90,90,0),#L5
                    ("13:left hand length ",-40,28,-6),#L6
                    ("14:left hand side   ",-15,25,5))#L7
my_tuple2 = (("15:right arm up     ",-14,130,130),#R1
                    ("16:right arm open   ",0,56,50),#R2
                    ("17:right upper arm  ",0,90,0),#R3
                    ("18:right elbow      ",0,112,0),#R4
                    ("19:right forearm    ",-90,90,-90),#R5
                    ("13:right hand length ",-40,28,-6),#R6
                    ("14:right hand side   ",-15,25,5))#R7

class TestFrame(tk.Frame):

        def __init__(self,root,number,label,min_,max_,init_):
                tk.Frame.__init__(self,root)
                self.root = root
                                
                row = 0
                column = 0
                self.label = tk.Label(self,text=label)
                self.label.grid(row=row, column=column)
                
                row = 0
                column = 1
                self.slider = tk.Scale(self,orient='h',from_ = min_, to = max_)
                self.slider.set(init_)
                self.slider.grid(row=row, column=column)

                
                row = 0
                column = 2
                self.strvar = tk.StringVar()
                self.strvar.set("0")
                self.entry =tk.Entry(self,textvariable=self.strvar)
                self.entry.grid(row=row,column=column)
                #
                #self.button = tk.Button(root, text = 'Gripper ON', bg = '#250')
                #self.button.grid(column=5,row=13)

        def setvalue(self, value):
                #value = self.slider.get()
                self.strvar.set(value)
                
                #self.strvar.set()
                
        def getvalue(self):
                return self.slider.get()

class ArmLeftFrame(tk.LabelFrame):
        def __init__(self,root, tuple_1):
                tk.LabelFrame.__init__(self,root,text = 'LEFT')
                self.root = root
                #label = tk.Label(self, text = '--------LEFT--------')
                #label.grid(row=0,column=0)
                row = 1
                column = 0
                for elem in my_tuple1:
                        title = elem[0]
                        value1 = elem[1]
                        value2 = elem[2]
                        value3 = elem[3]
                        tf = TestFrame(self,0,elem[0],elem[1],elem[2],elem[3])
                                #selfじゃなくてrootにしたら窓全体に追加されるということになる               
                        tf.grid(row=row,column=column)
                        row = row + 1

class ArmRightFrame(tk.LabelFrame):
        def __init__(self,root, tuple_2):
                tk.LabelFrame.__init__(self,root,text = 'RIGHT')
                self.root = root
                #label = tk.Label(self, text = '--------RIGHT-------')
                #label.grid(row=0,column=0)
                row = 1
                column = 0
                for elem in my_tuple2:
                        title = elem[0]
                        value1 = elem[1]
                        value2 = elem[2]
                        value3 = elem[3]
                        tf = TestFrame(self,0,elem[0],elem[1],elem[2],elem[3])
                                #selfじゃなくてrootにしたら窓全体に追加されるということになる               
                        tf.grid(row=row,column=column)
                        row = row + 1
                        
class CoordinateFrame(tk.Frame):
        def __init__(self, root):
                tk.Frame.__init__(self,root)
                self.strvar = tk.StringVar()
                self.root = root
                self.strvar.set("0")
                
                label = tk.Label(self, text = 'LEFT Target Pose  ')
                label.grid(row=1,column=3)
                self.entry_LT = tk.Entry(self,textvariable=self.strvar)
                self.entry_LT.grid(row=1,column=4)
                
                label = tk.Label(self, text = 'LEFT Current Pose ')
                label.grid(row=2,column=3)
                self.entry_LC = tk.Entry(self,textvariable=self.strvar)
                self.entry_LC.grid(row=2,column=4)
                
                label = tk.Label(self, text = 'RIGHT Target Pose ')
                label.grid(row=3,column=3)
                self.entry_RT = tk.Entry(self,textvariable=self.strvar)
                self.entry_RT.grid(row=3,column=4)
                
                label = tk.Label(self, text = 'RIGHT Current Pose')
                label.grid(row=4,column=3)
                self.entry_RC = tk.Entry(self,textvariable=self.strvar)
                self.entry_RC.grid(row=4,column=4)


class SwitchFrame(tk.Frame):
        def __init__(self, root):
                tk.Frame.__init__(self,root)
                self.strvar = tk.StringVar()
                label = tk.Label(self, text = 'JammingGripper')
                label.grid(row=0,column=0)
                button = tk.Button(self, text = 'ON')
                button.grid(row=0,column=1)


class RadioButtonFrame(tk.Frame):
        def __init__(self, root):
                tk.Frame.__init__(self,root)
                self.action = tk.IntVar()
                self.action.set(1)
                radio1 = tk.Radiobutton(self, text = 'Coordinate Input', variable = self.action, value = 0)
                radio1.grid(row=0,column=0)
                radio2 = tk.Radiobutton(self, text = 'Slider Input', variable = self.action, value = 1)
                radio2.grid(row=1,column=0)


class GUI:
        def __init__(self):
                self.root = tk.Tk()
                armleftFrame = ArmLeftFrame(self.root, my_tuple1)       
                armleftFrame.grid(row=1,column=0)
        
                armrightFrame = ArmRightFrame(self.root, my_tuple2)       
                armrightFrame.grid(row=3,column=0)

                coordinate = CoordinateFrame(self.root)
                coordinate.grid(row=1,column=3 and 4)

                switch = SwitchFrame(self.root)
                switch.grid(row=2,column=4)

                radiobutton = RadioButtonFrame(self.root)
                radiobutton.grid(row=3,column=4)

        def mainloop(self):
                self.root.mainloop()
           


if __name__ == '__main__':
        g = GUI()

        g.mainloop()

