import tkinter as tk

aisle_robot_nav = None
bin_robot_nav  =  None

class ProductSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Search")

        # frame for the entry widget
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10)

        # text entry widget
        self.entry = tk.Entry(self.entry_frame, width=40, font=('Arial', 24))
        self.entry.pack()

        # frame for the keyboard
        self.keyboard_frame = tk.Frame(root)
        self.keyboard_frame.pack()

        # keyboard layout
        self.keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Clear', 'Delete', 'Search'
        ]

        # create buttons for the keyboard
        self.create_keyboard()

        # label to display product information
        self.product_info_label = tk.Label(root, text="", font=('Arial', 18), wraplength=400)
        self.product_info_label.pack(pady=10)

        self.products = {        
            '00211088': (13, 1),
            '00298246': (24, 13),
            '00457235': (13, 10),
            '00529478': (13, 11),
            '20192828': (7, 12),
            '20275814': (1, 15),
            '20301554': (1, 19),
            '30481516': (22, 25),
            '50511857': (24, 16),
            '50556431': (10, 10),
            '70511903': (22, 16),
            '80489402': (10, 16),
            '80576079': (23, 23),
            '90282180': (1, 20),
            '90489029': (10, 15)

        }


    def create_keyboard(self):
        row = 0
        col = 0
        for key in self.keys:
            button = tk.Button(self.keyboard_frame, text=key, width=5, height=2, font=('Arial', 18),
                               command=lambda k=key: self.on_key_press(k))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4: 
                col = 0
                row += 1


    def on_key_press(self, key):
        # clear the entry
        if key == "Clear":
            self.entry.delete(0, tk.END)
        # delete the last character  
        elif key == "Delete":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)  
            self.entry.insert(0, current_text[:-1])
        # insert space  
        elif key == "Space":
            self.entry.insert(tk.END, ' ') 
        # trigger search 
        elif key == "Search":
            self.perform_search() 
        # insert the character 
        else:
            self.entry.insert(tk.END, key)  

    def perform_search(self):
        query = self.entry.get().strip()
        if query:  
            try:
                response = self.products[query]
                display_text = f'Aisle: {response[0]} Bin: {response[1]}'
                aisle_robot_nav = response[0]
                bin_robot_nav = response[1]
            except:
                display_text = f'Product with serial number {query} not found'
            self.product_info_label.config(text=display_text)
            # clear entry after search
            self.entry.delete(0, tk.END)
    

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductSearchApp(root)
    root.mainloop()