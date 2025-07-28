from tkinter import *
import string
from random import randint, choice

def generate_passeword(): #creation d'une fonction pour generer le mot de passe aleatoire
    password_min = 6
    password_max = 12
    all_string = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_string) for x in range(randint(password_min, password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0, password)

window = Tk()  # Create a window
window.title("password generator") #creation  du titre
window.geometry("450x450")  # Set the default size of the window
window.config(background="black")

#create frame
frame = Frame(window, bg="black")  # Create a frame with a black background
right_frame = Frame(frame, bg="black") #create a subframe 
 
#image create
width = 300 
height = 300
image = PhotoImage(file="images.png").zoom(33).subsample(32)  # Load an image
canvas = Canvas(frame, width=width, height=height, background="black", border=0, highlightthickness= 0) # Create a canvas
canvas.create_image(width / 2, height / 2, image=image)  # Place
canvas.grid(row=0, column=0, sticky=E)  # Display the canvas

#insert text 
label = Label(right_frame, text="Password Generator", font=("Arial", 20), bg="black", fg="white")  # Create a label
label.pack()

#create an entry field
password_entry = Entry(right_frame, font=("Arial", 20), bg="black", fg="white", border=2)  # Create a label
password_entry.pack()

#create a button
generate_button = Button(right_frame, text="Generate", font=("Arial", 20), bg="black", fg="white", command=generate_passeword)  # Create a button
generate_button.pack(fill=X)


right_frame.grid(row=0, column=1, sticky=W)  # Pack the label with some padding
frame.pack(expand=YES)  # Pack the frame with some padding

#creation d'une barre  de menu
menu_bar = Menu(window)  # Create a menu bar    
# Create a menu
file_menu = Menu(menu_bar, tearoff=0)  # Create a file menu
file_menu.add_command(label="Generate Password", command=generate_passeword)  # Add a command to the file menu
file_menu.add_separator()  # Add a separator
file_menu.add_command(label="Exit", command=window.quit)  # Add an exit command to the file menu
menu_bar.add_cascade(label="File", menu=file_menu)  # Add the file menu
# Create an "About" menu    
about_menu = Menu(menu_bar, tearoff=0)  # Create an about menu
about_menu.add_command(label="About", command=lambda: print("This is a password generator application."))  # Add an about command
menu_bar.add_cascade(label="About", menu=about_menu)  # Add the about menu to the menu bar
# Add the menu bar to the window
window.config(menu=menu_bar)  # Configure the window to use the menu bar

if __name__ == "__main__":
   
    window.mainloop()  # Start the main loop 