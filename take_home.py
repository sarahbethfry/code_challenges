class Canvas():    
    def __init__(self, size):
        self.size = size;
        self.shape = [];
        
    def render(self): 
        for y in range(self.size):
            for x in range(self.size):
                self.draw_coord(y,x)
                
            print("")

    def draw_coord(self,y,x):
        
        if (y == 0):
            print(x, end="")
        elif (x == 0):
            print(y, end="")
        else:
            if self.has_shape(y,x):
                print("*", end="")
            else:
                print(" ", end="")

    def has_shape(self, x,y):
        x0 = self.shape[0]
        y0 = self.shape[1]
        x1 = self.shape[2]
        y1 = self.shape[3]

        return x >= x0 and x <= x1 and y >= y0 and y <= y1 
        
        

    def rectangle(self, x0, y0, x1, y1, char):
         self.shape = [x0,y0,x1,y1,char]
              

   

canvas = Canvas(8)
canvas.rectangle(2,2,4,4,'*')
canvas.render()

        


        
    
