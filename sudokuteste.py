import random
class Cell:
    def __init__(self,value:int):
        self._value = value
        self._isFixed = False
    def __repr__(self):
        return str(self._value)
    def __eq__(self,other):
        if isinstance(other,Cell):
            return self._value == other._value
        else:
            return self._value==other  
    @property
    def isFixed(self):
        return self._isFixed
    @isFixed.setter
    def isFixed (self,value:bool):
        self._isFixed = value
class Su:
    def __init__(self):
        self._su = []
        for i in range(9):#make a 9x9 grid and fill with 0
            self._su.append([])
            for j in range(9):
                self._su[i].append(Cell(0))
    def __repr__(self):
        r =''
        for j in range(9):
            for i in range(9):
                if (i+1)%3==0 and i!=0 and i!=9:
                    r+=str(self._su[i][j])+'|'
                else:
                    r+=str(self._su[i][j])
            if (j+1)%3==0 and j!=0 and j!=9:
                r+='\n------------'
            r+='\n'
        return r 
    def legal(self,value:int,x:int,y:int) -> bool:#verify if it's legal to place a number in a x, y position
        return self.__verify_colum_row(value,x,y) and self.__verify_square(value,x,y) and value!=0 and not self._su[x][y].isFixed
    def __verify_colum_row(self,value:int,x:int,y:int)-> bool:
        for i in range(9):#verify the row
            if value == self._su[i][y]:
                return False
        return not(value in self._su[x])#verify row
    def __verify_square(self,value:int,x:int,y:int) -> bool:
        sqr = self.__what_sqr(x,y)
        if sqr == 1:#based on the smaller grid, take the initial and final position xi-xf, yi-yf
            return self.__validate_sqr(value,0,3,0,3)
        elif sqr == 2:
            return self.__validate_sqr(value,3,6,0,3)
        elif sqr == 3:
            return self.__validate_sqr(value,6,9,0,3)
        elif sqr == 4:
            return self.__validate_sqr(value,0,3,3,6)
        elif sqr == 5:
            return self.__validate_sqr(value,3,6,3,6)
        elif sqr == 6:
            return self.__validate_sqr(value,6,9,3,6)
        elif sqr == 7:
            return self.__validate_sqr(value,0,3,6,9)
        elif sqr == 8:
            return self.__validate_sqr(value,3,6,6,9)
        elif sqr == 9:
            return self.__validate_sqr(value,6,9,6,9)
        else:
            raise Exception
    def __what_sqr(self,x:int,y:int) -> int: #get the number/positon of the smaller grid
        if x < 3:
            if y < 3:
                return 1
            elif y < 6:
                return 4
            else:
                return 7
        elif x < 6:
            if y < 3:
                return 2
            elif y < 6:
                return 5
            else:
                return 8
        else:
            if y < 3:
                return 3
            elif y < 6:
                return 6
            else:
                return 9
    def __validate_sqr(self,value:int,x1:int,x2:int,y1:int,y2:int)->bool:
        for y in range(y1,y2):#using the limitation of the smaller grid given in the __verify_square method, verify the smaller grid
            for x in range(x1,x2):
                if value == self._su[x][y]:
                    return False
        return True
    def change(self,value:int,x:int,y:int):
        if self.legal(value,x,y):
            self._su[x][y]._value = value
            return True
        return False
    def create(self,dif:str):#call create_rec with correct start
        self.__create_rec(0,0)
        print(self)
        self.__clean_grid(dif)
    def __create_rec(self,x:int,y:int,count:int=0,tries:list = None):#creates a sudoku recursively
        if tries == None:# list of numbers tried
            tries = []
        r = random.randint(1,9)#number to try
        a=0 #just a verification
        if count == 9: #number of tries
            temp = True
            for a in range(1,10): #a last try passing through all numbers
                if self.legal(a,x,y) and not(a in tries):
                    r= a
                    temp = False
                    break
            if temp: #verify if it had found the number on the loop
                return
        if x==0 and y==0:# first number, no need to check
            self._su[0][0]._value = r
            self.__create_rec(x+1,y)
        elif x==8 and y==8: # last number, just one possibility, so no need to return to the previous calls int he stack
            if not self.legal(r,x,y):
                self.__create_rec(x,y)
            else:
                self._su[8][8]._value=r
        elif x  == 8 or y==8: # just trying every number on the last space of a column or row -- not really needed tough
            if a ==0:
                for a in range(1,10):
                    if self.legal(a,x,y) and not(a in tries):
                        self._su[x][y]._value = a
                        break
                tries.append(self._su[x][y])
            if self._su[x][y]==0:
                self.__create_rec(x,y,9,tries) #if none, return to previous calls
            elif x == 8:
                self.__create_rec(0,y+1)
            else:
                self.__create_rec(x+1,y)
        else:
            if tries !=  []:
                if r in tries:
                    self._su[x][y]._value=0
                    return
            if not self.legal(r,x,y):#see if it's legal
                self.__create_rec(x,y,count+1,tries)
            else:
                self._su[x][y]._value=r
                tries.append(r)
                self.__create_rec(x+1,y)
        if self._su[x][y]==0:#pop every call for a same position tha has reached 9 tries
            return
        elif 0 in self._su[8]:#just enter if there's a zero on the last column
            self._su[x][y]._value = 0
            self.__create_rec(x,y,count,tries)
    def __clean_grid(self,dif:str):
        if dif.lower() == 'easy':
            clean = 40
        elif dif.lower() == 'medium':
            clean = 60
        elif dif.lower() == 'hard':
            clean = 70
        else:
            return
        for a in range(clean):
            x = random.randint(0,8)
            y = random.randint(0,8)
            self._su[x][y]._value = 0
        for i in range(9):
            for j in range(9):
                if self._su[i][j] !=0:
                    self._su[i][j].isFixed = True
    def solve(self):#first solve, sometimes works, sometimes not, gets maximum recursion depth exception. I just gave up this one
        self.__solve_rec(0,0)
    def __solve_rec(self,x:int,y:int,count:int=0,tries:list = None):
        if tries == None:# list of numbers tried
            tries = []
        r = random.randint(1,9)#number to try
        a=0 #just a verification
        if count == 9: #number of tries
            temp = True
            for a in range(1,10): #a last try passing through all numbers
                if self.legal(a,x,y) and not(a in tries):
                    r= a
                    temp = False
                    break
            if temp: #verify if it had found the number on the loop
                return
        if self._su[x][y].isFixed: #if it's an already fixed number, just call the next position  
            if x!=8:
                self.__solve_rec(x+1,y)
            elif x==8 and y!=8:
                self.__solve_rec(0,y+1)
        elif x==0 and y==0:
            if not self.change(r,x,y):
                self.__solve_rec(x,y)
            else:
                self.__solve_rec(x+1,y)
        elif x==8 and y==8: # last number, just one possibility, so no need to return to the previous calls int he stack
            if not self.legal(r,x,y):
                self.__solve_rec(x,y)
            else:
                self._su[8][8]._value=r
        elif x  == 8 or y==8: # just trying every number on the last space of a column or row -- not really needed tough
            if a ==0:
                for a in range(1,10):
                    if self.legal(a,x,y) and not(a in tries):
                        self._su[x][y]._value = a
                        break
                tries.append(self._su[x][y])
            if self._su[x][y]==0:
                self.__solve_rec(x,y,9,tries) #if none, return to previous calls
            elif x == 8:
                self.__solve_rec(0,y+1)
            else:
                self.__solve_rec(x+1,y)
        else:
            if tries !=  []:
                if r in tries:
                    self._su[x][y]._value=0
                    return
            if not self.legal(r,x,y):#see if it's legal
                self.__solve_rec(x,y,count+1,tries)
            else:
                self._su[x][y]._value=r
                tries.append(r)
                self.__solve_rec(x+1,y)
        if not self.verify_cells():#verify if the sudoku is already solved
            if (self._su[x][y]==0 or self._su[x][y].isFixed) and not(x ==0 and y ==0) :#pop every call for a same position tha has reached 9 tries
                return
            else:
                self._su[x][y]._value = 0
                self.__solve_rec(x,y,count,tries)
    def verify_cells(self)->bool:
        for i in range(9):
            for j in range (9):
                if self._su[i][j] ==0:
                    return False
        return True
    def solve2(self):
        self.__solve_rec2(0,0)
    def __solve_rec2(self,x:int,y:int,tries:list = None):
        if tries == None:# list of numbers tried
            tries = []
        if self._su[x][y].isFixed: #if it's already a fixed number, just call the next position  
            if x!=8:
                self.__solve_rec2(x+1,y)
            elif x==8 and y!=8:
                self.__solve_rec2(0,y+1)
        else:
            temp = True
            self._su[x][y]._value = 0
            for a in range(1,10): #passing through all numbers
                if self.legal(a,x,y) and not(a in tries):
                    self._su[x][y]._value = a
                    temp = False
                    tries.append(a)
                    break
            if temp: #verify if it had found the number on the loop
                return
            elif x==8 and y!=8:
                self.__solve_rec2(0,y+1)
            elif not(x==8 and y==8):
                self.__solve_rec2(x+1,y)
        if not self.verify_cells():
            if (self._su[x][y]==0 or self._su[x][y].isFixed) and not(x ==0 and y ==0) :#pop every call for a same position tha has reached 9 tries
                return
            else:
                self._su[x][y]._value = 0
                self.__solve_rec2(x,y,tries)

if __name__ == '__main__':
    mano = Su()
    mano.create('easy')
    print(mano)
    mano.solve2()
    print(mano)