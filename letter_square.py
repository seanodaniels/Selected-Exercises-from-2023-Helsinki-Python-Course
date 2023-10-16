alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    for row_pos in range(0, (layers-1)):

        print(f"\nBeginning of row {row_pos}\n")
        direction = "minus"
        current_count = layers
        current_row = layers

        for col_pos in range(0, (layers * 2)-1):            
            if layers - col_pos == 0:
                print(alphabet[current_count-1], end="")
                direction = "plus"
            else:                
                if direction == "plus":
                    current_count += 1

                if direction == "minus":
                    current_count -= 1
            print(alphabet[current_count], end="")
    
def print_row(max, min):
    for row_pos in range(max, 1, -1):
        if row_pos > min:
            print(f"{alphabet[row_pos-1]}", end="")
        else:
            print(f"{alphabet[min-1]}", end="")
    for row_pos in range(1, max+1):
        if row_pos > min:
            print(f"{alphabet[row_pos-1]}", end="")
        else:
            print(f"{alphabet[min-1]}", end="")

def print_cols(layers):
    for col_pos in range(layers, 1, -1):
        print_row(layers,col_pos)
        print()

    for col_pos in range(1, layers+1):
        print_row(layers,col_pos)
        print()

layers = int(input("Layers: "))
print_cols(layers)
