import tkinter as tk
from itertools import combinations

def generate_tableaux():
    n = int(entry_n.get())
    m = int(entry_m.get())
    numbers = list(range(1, n+m+1))
    
    output_text.delete(1.0, tk.END)
    count_text.delete(1.0, tk.END)  # Clear the count text box when clicked

    count = 0

    # Generate all combinations of size n from numbers
    for comb in combinations(numbers, n):
        first_column = sorted(list(comb))
        remaining_numbers = sorted(list(set(numbers) - set(comb)))

        # cheesing it -> Checking if the first number of first_column is 1
        if first_column[0] != 1:
            continue

        # Generate all combinations of size m from the remaining numbers
        for subcomb in combinations(remaining_numbers, m):
            remaining_columns = sorted(list(subcomb))
            # Check if the combinations are strictly increasing
            if (first_column == sorted(first_column) and remaining_columns == sorted(remaining_columns)):
                tableaux = [first_column] + [[i] for i in remaining_columns]
                # Print the 'L-Shpaed'tableaux
                for i in range(n):
                    row_str = ' '.join(str(tableaux[j][i]) if i < len(tableaux[j]) else ' ' for j in range(m+1))
                    output_text.insert(tk.END, row_str + '\n')
                output_text.insert(tk.END, '\n')
                count += 1  # Perm counter


    count_text.insert(tk.END, str(count))

root = tk.Tk()
root.title('Young Tableaux Generator')

frame = tk.Frame(root)
frame.pack()

label_n = tk.Label(frame, text='Enter n (height of first column):')
label_n.pack(side=tk.LEFT)

entry_n = tk.Entry(frame)
entry_n.pack(side=tk.LEFT)

label_m = tk.Label(frame, text='Enter m (number of remaining columns):')
label_m.pack(side=tk.LEFT)

entry_m = tk.Entry(frame)
entry_m.pack(side=tk.LEFT)

button = tk.Button(frame, text='Generate', command=generate_tableaux)
button.pack(side=tk.LEFT)

# New frame for output
output_frame = tk.Frame(root)
output_frame.pack(expand = True)

count_label = tk.Label(output_frame, text='Number of permutations (|λ|):')
count_label.pack(side=tk.TOP)

count_text = tk.Text(output_frame, width=20, height=2)
count_text.pack(side=tk.TOP)

output_text = tk.Text(output_frame)  # Pack output_text in output_frame
output_text.pack()

root.mainloop()
