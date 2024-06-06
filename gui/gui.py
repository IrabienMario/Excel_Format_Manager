import tkinter as tk
from PIL import ImageTk 
import webbrowser

def run():
    """
    Function to run the program.
    """
    ask_qty("312892")
    ask_qty("12344")

# FUNCIONES -----------
def open_link(url):
    """
    Function to open a link in the default web browser.
    """
    webbrowser.open_new(url)

def start():
    """
    Function to start the program.
    """
    start_button.config(state=tk.DISABLED, cursor='arrow')
    start_var.set("Ejecutando...     ")
    for i in range(8):
        show_msg("mensaje {}".format(i))
    run()


def end():
    """
    Function to end the program.
    """
    start_button.config(state=tk.NORMAL, cursor='hand2')
    start_var.set("Hacer Formato FUMA")

def info():
    """
    Function to display information about the program.
    """
    def info_win_close():
        info_button.config(state=tk.NORMAL, cursor='hand2')
        info_window.destroy()

    info_window = tk.Toplevel()
    info_window.title("Información")
    info_window_x = root.winfo_x()
    info_window_y = root.winfo_y()
    info_window.geometry("+%d+%d" % ((info_window_x) + 100, (info_window_y) + 100))
    info_window.resizable(width=False, height=False)
    info_window.protocol("WM_DELETE_WINDOW", info_win_close)
    info_window.wait_visibility()

    info_label = tk.Label(info_window, text='Versión 1.0 \n \n Github:')
    info_label.pack(padx=20, pady=(20, 0))
    link_label = tk.Label(info_window, text="https://github.com/IrabienMario/Excel_Format_Manager",
                          fg='blue', cursor='hand2')
    link_label.pack(padx=20, pady=(0, 20))
    link_label.bind("<Button-1>", lambda e: open_link("https://github.com/IrabienMario/Excel_Format_Manager"))
    info_button.config(state=tk.DISABLED, cursor='arrow')

product_name = "NOMBRE"

#CANTIDAD DE PRODUCTOS
def ask_qty(ID=str()):
    """
    Function to ask for the quantity of a product.
    """
    def on_continue():
        if qty_entry.get():
            value = qty_entry.get()
            qty_window.destroy()
            show_msg("ID: {}".format(ID))
            show_msg("NOMBRE: {}".format(product_name))
            show_msg("CANTIDAD: {}".format(value))
            show_msg("--------")
            return value

    start_button.config(state=tk.DISABLED, cursor='arrow')
    qty_window = tk.Toplevel()
    qty_window.title("TEXTO ID")
    qty_window_x = root.winfo_x()
    qty_window_y = root.winfo_y()
    qty_window.geometry("+%d+%d" % ((qty_window_x) + 100, (qty_window_y) + 100))
    qty_window.resizable(width=False, height=False)
    qty_window.protocol("WM_DELETE_WINDOW", on_continue)
    qty_window.wait_visibility()

    #buscar nombre del producto
    name_label = tk.Label(qty_window, text='Nombre: ', font=('Consolas', 19))
    name_label.grid(row=0, column=0, sticky='w')
    product_name_label = tk.Label(qty_window, text=product_name, font=('Consolas', 19))
    product_name_label.grid(row=0, column=1, sticky='w')

    product_label = tk.Label(qty_window, text='Producto: ', font=('Consolas', 19))
    product_label.grid(row=1, column=0, sticky='w')

    id_prod = tk.StringVar()
    id_prod.set(ID)
    id_label = tk.Label(qty_window, textvariable=id_prod, font=('Consolas', 19))
    id_label.grid(row=1, column=1, sticky='w')

    qty_label = tk.Label(qty_window, text="Cantidad: ", font=('Consolas', 19))
    qty_label.grid(row=2, column=0, sticky='w')

    qty_entry = tk.Entry(qty_window, width=5, font=('Consolas', 19))
    qty_entry.grid(row=2, column=1, sticky='w')

    continue_button = tk.Button(qty_window, text="Siguiente", font=('Consolas', 15), command=on_continue)
    continue_button.grid(row=3, column=0, columnspan=2, pady=10)


def show_msg(string):
    """
    Function to display a message.
    """
    add_label(string)

def add_label(text):
    """
    Function to add a label to the GUI.
    """
    if not text:
        return

    if len(labels) >= max_labels:
        old_label = labels.pop(0)
        old_label.pack_forget()

    new_label = tk.Label(center_frame, text=text, font=('Consolas', 19), bg='white')
    new_label.pack(side=tk.TOP, fill=tk.X, pady=2)
    labels.append(new_label)

#ROOT ----- RAIZ DE LA VENTANA PRINCIPAL
root = tk.Tk()
root.iconphoto(False, ImageTk.PhotoImage(file='Vinden_fuma.png'))
root.geometry('350x350')
root.title("F.U.M.A.")
root.eval('tk::PlaceWindow . center')
root.resizable(width=False, height=False)
root.config(bg='#ffffff')

# FRAME PARA BOTONES (BARRA SUPERIOR)
top_frame = tk.Frame(root, bg='gray')
top_frame.pack(side=tk.TOP, fill=tk.X)

# BOTON PARA INICIAR EL PROGRAMA
start_var = tk.StringVar()
start_var.set("Hacer Formato FUMA")
start_button = tk.Button(top_frame, textvariable=start_var, font=('Consolas', 19), command=start, cursor='hand2')
start_button.pack(side=tk.LEFT, ipadx=10)

# BOTON DE INFORMACIÓN
info_button = tk.Button(top_frame, text="ⓘ", font=('Consolas', 19), command=info, cursor='hand2')
info_button.pack(side=tk.RIGHT, ipadx=10)

# FRAME CENTRAL
center_frame = tk.Frame(root, bg='white')
center_frame.pack(fill=tk.BOTH, expand=True)

# PARA DARLE UN MAXIMO A LOS LABELS
max_labels = 7
labels = []

# Mainloop
root.mainloop()

