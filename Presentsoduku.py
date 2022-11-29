#solving a soduku using oop
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
    def print_board(self):
        for i in range(len(self.board)):#i is the row of the board so if i is 0 then we are at the first row
            if i % 3 == 0 and i != 0:#Check if we are at the end of a box
                print("- - - - - - - - - - - - ")#print a line to seperate the boxes
                
            for j in range(len(self.board[0])):#j is the column of the board so if j is 0 then we are at the first column
                if j % 3 == 0 and j != 0:#Check if we are at the end of a box
                    print(" | ", end="")#print a line to seperate the boxes
                    
                if j == 8:#Check if we are at the end of the row
                    print(self.board[i][j])#print the number in the board
                else:#if we are not at the end of the row
                    print(str(self.board[i][j]) + " ", end="")#print the number in the board
        
    def find_empty(self):#find an empty space in the board
        for i in range(len(self.board)):#i is the row of the board so if i is 0 then we are at the first row
            for j in range(len(self.board[0])):#j is the column of the board so if j is 0 then we are at the first column
                if self.board[i][j] == 0:#Check if the space is empty
                    return (i, j) # row, col
        return None#return none if there are no empty spaces
#return the position of the empty space if there is one
    def valid(self, num, pos):#Check if the number is valid in the position
        # Check row
        for i in range(len(self.board[0])):#i is the row of the board so if i is 0 then we are at the first row
            if self.board[pos[0]][i] == num and pos[1] != i:#Check if the number is in the row and if it is not in the same column as the position
                return False #return false if the number is in the row
        # Check column
        for i in range(len(self.board)):#i is the row of the board so if i is 0 then we are at the first row
            if self.board[i][pos[1]] == num and pos[0] != i:#Check if the number is in the column and if it is not in the same row as the position
                return False #return false if the number is in the column
            
        # Check box.
        box_x = pos[1] // 3#find the box the position is in
        box_y = pos[0] // 3#find the box the position is in
        for i in range(box_y*3, box_y*3 + 3):#i is the row of the board so if i is 0 then we are at the first row
            for j in range(box_x * 3, box_x*3 + 3):#j is the column of the board so if j is 0 then we are at the first column
                if self.board[i][j] == num and (i,j) != pos:#Check if the number is in the box and if it is not in the same position as the position we are checking
                    return False #return false if the number is in the box
        return True #return true if the number is valid

# the above functon uses the position of the empty space to check if the number is valid in that position
    def solve(self): #solve the soduku
        find = self.find_empty()#find an empty space in the board
        if not find: #if there are no empty spaces
            return True #return true
        else:#if there are empty spaces
            row, col = find #set the row and column of the empty space
        for i in range(1,10):#i is the number we are checking
            if self.valid(i, (row, col)): #check if the number is valid in the position
                self.board[row][col] = i #set the number in the position
                if self.solve(): #solve the soduku
                    return True #return true
                self.board[row][col] = 0 #set the position to 0
        return False #return false if the number is not valid in the position
def main(): 
    soduku = Soduku() #create a soduku object
    soduku.print_board() #print the board
    soduku.solve() ##solve the soduku
    print("_______________________solution_______________________")
    soduku.print_board() #print the board
main()
