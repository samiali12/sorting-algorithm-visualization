from  tkinter import * 
from  tkinter.ttk import Combobox
from  random import randint
import time

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.ui_frame = None
        self.algo_combo_box = None
        self.array = []
        self.canvas = None

        self.initUI()

    def initUI(self):
        self.master.title("Algorithm Visualization")
        self.master.config(bg="#333")
        self.master.maxsize(700,600)
        self.master.minsize(700,600)

        # design UI FRAME For Buttons and Inputs
        self.ui_frame = Frame(self.master, width="700", height="100", bg="white")
        self.ui_frame.grid(row=0,column=0, padx=0, pady=0)

        #canvas for plot shapes on it
        self.canvas = Canvas(self.master, width="700",height="500", bg="white")
        self.canvas.grid(row=1, column=0, padx=0, pady=0)

        #algorithm selection
        Label(self.ui_frame, text="Select Algorithm", bg="#333" \
                    , fg="#fff", font=("Arial",13)).grid(row=0,column=0,padx=10,pady=10,sticky=W)

        #combo box for algorithm
        self.algo_combo_box = Combobox(self.ui_frame, \
                                        values=['Bubble Sort','Insertion Sort','Selection Sort',
                                        'Quick Sort', 'Merge Sort'])
        self.algo_combo_box.current(0)
        self.algo_combo_box.grid(row=0,column=1,padx=10,pady=10)

        Label(self.ui_frame, text="Array Size", bg="#333", fg="#fff", \
                                                            font=("Arial",13)).grid(row=0,column=2)
        self.algo_combo_box_size = Combobox(self.ui_frame, \
                                         values=["10","20","30"])
        self.algo_combo_box_size.current(0)
        self.algo_combo_box_size.grid(row=0,column=3,padx=10,pady=10)

        #generate array button
        button0 = Button(self.ui_frame, text="Generate", bg="#333", fg="white", \
                                                             bd=0, font=("Arial",13), command=self.generate)
        button0.grid(row=0,column=4,padx=10,pady=10)

        #start sorting button
        button1 = Button(self.ui_frame, text="Start Sorting", bg="#333", fg="white", \
                                                        bd=0, font=("Arial",13), command=self.start_sorting)
        button1.grid(row=1,column=2,padx=10,pady=10)

    def generate(self):

        self.array.clear()

        for i in range(int(self.algo_combo_box_size.get())):
            rand_num = randint(0,100) # generate random number every time
            self.array.append(rand_num)

        colorArray = ["#333" for i in range(0,len(self.array))]
        self.draw_blocks(colorArray)


    def draw_blocks(self,colorArray):

        self.canvas.delete("all") # canvas delete all previous stuff already draw on it 
        canvas_height = 500
        canvas_width  = 700
        x_width =  canvas_width // (len(self.array) + 1)
        offset = 20
        spacing = 20

        for i,height in enumerate(self.array):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height
            ###################################
            x1 = (i+1) * x_width + offset
            y1 = canvas_height
            # create_rectangle(x1,y1,x2,y2)
            self.canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
            self.canvas.create_text(x0+2,y0-10,anchor=SW, text=str(self.array[i]))

        self.master.update_idletasks()


    def bubble_sort(self):

        for i in range(len(self.array)-1):
            for j in range(len(self.array)-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    current_color = [ "blue" if k == j   else "#333" for k in range(0,len(self.array))]
                    self.draw_blocks(current_color)
                    time.sleep(0.2)

    
    def insertion_sort(self):

        for i in range(1,len(self.array)):

            key, j = self.array[i], i-1

            while j >= 0 and self.array[j] >= key:
                self.array[j+1] = self.array[j]
                current_color = [ "blue" if k == j   else "#333" for k in range(0,len(self.array))]
                self.draw_blocks(current_color)
                time.sleep(0.2)
                j -= 1

            self.array[j+1] = key 
            current_color = [ "blue" if k == j   else "#333" for k in range(0,len(self.array))]
            self.draw_blocks(current_color)
            time.sleep(0.2)

    def selection_sort(self):

        for i in range(0,len(self.array)-1):

            min_index = i

            for j in range(i+1,len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j
            
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            current_color = [ "blue" if k == j   else "#333" for k in range(0,len(self.array))]
            self.draw_blocks(current_color)
            time.sleep(0.2)


    def partition(self):
        pass 
    def quick_sort(self):
        print("Quick Sort")

    
    def merge_sort(self):
        pass 

    def merge(self):
        pass 


    def start_sorting(self):

        if self.algo_combo_box.get() == "Bubble Sort":
            self.bubble_sort()
        elif self.algo_combo_box.get() == "Insertion Sort":
            self.insertion_sort()
        elif self.algo_combo_box.get() == "Selection Sort":
            self.selection_sort()
        elif self.algo_combo_box.get() == "Quick Sort":
            self.quick_sort()
        elif self.algo_combo_box.get() == "Merge Sort":
            self.merge_sort()
        


master = Tk()
app = Window(master)
master.mainloop()