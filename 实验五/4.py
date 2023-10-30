
def validate_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False
    
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False
    
    # Check blocks
    for block_row in range(3):
        for block_col in range(3):
            block = [board[row][col] for row in range(block_row*3, block_row*3+3) for col in range(block_col*3, block_col*3+3)]
            if not is_valid_set(block):
                return False
    
    return True

def is_valid_set(nums):
    nums = [num for num in nums if num != 0]
    return len(set(nums)) == len(nums)