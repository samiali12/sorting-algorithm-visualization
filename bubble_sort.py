import time
from app_ui import Window

def bubble_sort(self):
    for i in range(len(self.array)-1):
        for j in range(len(self.array)-1):
            if self.array[j] > self.array[j+1]:
                self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                current_color = [ "blue" if k == j   else "#333" for k in range(0,len(self.array))]
                self.draw_blocks(current_color)
                time.sleep(0.2)