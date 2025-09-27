class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        elif column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        # another_queen başka bir queen nesnesini temsil ediyor.
        
        if self.column == another_queen.column and self.row == another_queen.row:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        return ( self.row == another_queen.row or 
                 self.column == another_queen.column or 
                 abs(self.row - another_queen.row) == abs(self.column - another_queen.column))
