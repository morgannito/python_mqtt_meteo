import pygame
from tkinter import *
from functools import partial

import paho.mqtt.client as mqtt_client

# se connecter au broker
client = mqtt_client.Client()
client.connect("localhost", 1883, 60)
# utilise un login et un mot de passe
client.username_pw_set("user", "password")



def mqttsend():
    #mqtt_client.mqtt_client()
    pass

def mqttreceive():
    pass


# Page Home creer la fenetre d'accueil du jeu
def main():
    # Creer une fenetre
    fenetre = Tk()
    # Fullscreen
    # fenetre.attributes('-fullscreen', 1)
    # Donne un titre à la fenetre
    fenetre.title("Méteo")
    # Dimension de la fenetre
    fenetre.geometry("800x600")
    # Taille minimun de la fenetre
    fenetre.minsize(800, 600)
    # Couleur de fond de la fenetre
    fenetre.config(background="black")
    # Ajout du titre du jeu dans la fenetre
    title = Label(fenetre, text="Météo ", font=("caveat", 40), bg="black", fg="white")
    # Ajoute le titre
    title.pack()
    # Creation d'une frame
    frame = Frame(fenetre, bg="black")

    # Ajouter la frame
    frame.pack(expand=YES)
    # Cration d'un label pour le texte
    text = Label(frame, text="Temperature :", font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Humidité Sol :", font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Pression :", font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Precipitation :", font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Pluie :", font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Cycle Jour / Nuit :", font=("caveat", 20), bg="black", fg="white")
    text.pack(side=BOTTOM)
    text = Label(frame, text="Altitude :", font=("caveat", 20), bg="black", fg="white")
    text.pack(side=BOTTOM)
    fenetre.mainloop()

main()