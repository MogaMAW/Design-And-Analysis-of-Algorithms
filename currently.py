import time
class Soduku:
    def __init__(self): #initialize the soduku
        self.board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]
    def printing(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

                    #####The complexity of this function is O(n^2)#######
    def get_null(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None #return none if there are no empty spaces
                    #####The complexity of this function is O(n^2)#####

    def isValid(self, num, pos):#Check if the number is valid in the position
        # Check row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False 
        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False #return false if the number is in the column
        # Check box
        xBox = pos[1] // 3
        yBox = pos[0] // 3
        for i in range(yBox*3, yBox*3 + 3):#The reason for the +3 is because the range function does not include the last number
            for j in range(xBox * 3, xBox*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:#Check if the number is in the box and if it is not in the same position as the position we are checking
                    return False 
        return True #return true if the number is valid
                    #####The complexity of this function is O(n^2)#####

# the above functon uses the position of the empty space to check if the number is valid in that position
    def sodukuSolve(self): #sodukuSolve the soduku 
        find = self.get_null() 
        if not find: 
            return True 
        else:
            row, col = find 
        for i in range(1,10): 
            if self.isValid(i, (row, col)):  
                self.board[row][col] = i 
                if self.sodukuSolve(): # this is the recursive part of the function and it repeats the process until the soduku is solved therefore the complexity is O(n^2) because it is a nested loop
                    return True #return true
                self.board[row][col] = 0 
        return False #return false if the number is not valid in the position
                    
def main():     
    t1 = time.time()   
    soduku = Soduku() #create a soduku object
    soduku.printing() #print the board
    soduku.sodukuSolve() ##sodukuSolve the soduku

    print("_______________________solution_______________________")
    t2 = time.time()
    soduku.printing() #print the board
    print("time taken: ", t2-t1)
main()
