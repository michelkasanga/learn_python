from tkinter import *
import webbrowser as web

def open_link():
    web.open("http://www.google.com") #ouvre un lien web

window = Tk() #cree une fenetre

#configuration du fenetre
window.title("Application") #titre de l'application
window.geometry("450x450") #la taille par defaut de la fenetre
window.minsize(250,250) #la taille minimum de la fenetre
#window.iconbitmap("logo.ico") #le logo de l'entete de la page
window.config(background='black') #ajout de la couleur d'arriere plan

#creation d'une boite
frame = Frame(window, background="black")

#ajouter du texte
label_title = Label(frame, 
                    text="Bienvenue sur mon application",
                    font=("Arial", 12), 
                    background="black", 
                    foreground= "white") #ajoute tu texte
label_title.pack() #affichage du texte (centre le texte)
label_subtitle = Label(frame, 
                    text=" dans cette application nous parlons de plusieur chose",
                    font=("Courriel", 10), 
                    background="black", 
                    foreground= "white") #ajoute tu texte
label_subtitle.pack() #affichage du texte (centre le texte)

#ajout du boutton
y_button = Button(frame, 
                text="Genere le mot de passe", 
                command=open_link, #l'action du boutton
                background="blue", 
                foreground="white", 
                font=("Arial", 10)) #ajoute un boutton
y_button.pack(pady=10) #affichage du boutton (centre le boutton)

frame.pack(expand = YES) #affichage de la boite

if __name__ == "__main__":
    window.mainloop( ) 