from arrays import Array
"""
Implement a basic grid, or 2D array, class.
"""

class Grid:
    """Represent a grid, or 2D array."""

    def __init__(self, rows, columns, fill_value = 0):
        """Initialize grid with fill_value."""
        self.data = Array(rows, Array(columns, fill_value))
        
##        # Don't need underlying deep copy with this version of Grid init
##        self.data = Array(rows)
##        for row in range(rows):
##            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        """Return number of rows."""
        return len(self.data)

    def get_width(self):
        """Return number of colunms."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Get item at index."""
        return self.data[index]

    def __str__(self):
        """Get string representation of Grid."""
        out = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                out += f"{self.data[row][col]:2d}" + ' '
            out += '\n'
        return out

    def __repr__(self):
        """Get representation of Grid."""
        out = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                out += f"{self.data[row][col]:2d}" + ' '
            out += '\n'
        return out

    def find_neg(self):
        """Get indices of first negative number position."""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                if self.data[row][col] < 0:
                    return row + 1, col + 1
        return row + 1, col + 1

        
                
