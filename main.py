from datetime import time
import pygame
from tkinter import *
from functools import partial

import paho.mqtt.client as mqtt
import json

humi = "000"
humidite_sol = ""
luminosite = ""
pluie = ""
precipitation = ""
pression = ""
temperature = ""

# Info du Broker
MQTT_BROKER_HOST = 'eu1.cloud.thethings.network'
MQTT_BROKER_PORT = 1883
MQTT_KEEP_ALIVE_INTERVAL = 60
BROKER_USERNAME = "yolo@ttn"
BROKER_PASSWORD = "NNSXS.E76A75GYWJRSSK674DPUUMKFWGBEUFIYCFCLOHQ.4ND3D2PSBOO2FHHVQ7APZSKMB3M5RCRSNS2QIUWPK2SWMDQHB7UA"

Json = None

# Creer une fenetre
fenetre = Tk()

# ----------------------------------------------- Connection au Broker ----------------------------------------------- #
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print(userdata)
    print(flags)
    # souscrire sur le topic field/camera/CAM1/scan
    client.subscribe("#", 1)


# ---------------------------------------------- Message recu Broker  ------------------------------------------------ #
def on_message(client, userdata, msg):
    global Json

    # print("Message Recieved. ", msg.payload.decode())
    # message recu sur le topic field/camera/CAM1/scan
    message = msg.payload.decode()
    Json = json.loads(message)
    print(Json['uplink_message']['decoded_payload'])
    humi = Json['uplink_message']['decoded_payload']['humidite']
    print(humi)
    humidite_sol = Json['uplink_message']['decoded_payload']['humidite_sol']
    print(humidite_sol)
    luminosite = Json['uplink_message']['decoded_payload']['luminosite']
    print(luminosite)
    pluie = Json['uplink_message']['decoded_payload']['pluie']
    print(pluie)
    precipitation = Json['uplink_message']['decoded_payload']['precipitation']
    print(precipitation)
    pression = Json['uplink_message']['decoded_payload']['pression']
    print(pression)
    temperature = Json['uplink_message']['decoded_payload']['temperature']
    print(temperature)
    # creation de la nouvelle fenetre
    for widget in fenetre.winfo_children():
        widget.destroy()
    title = Label(fenetre, text="Météo ", font=("caveat", 40), bg="black", fg="white")
    # Ajoute le titre
    title.pack()
    # Creation d'une frame
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    # Cration d'un label pour le texte
    text = Label(frame, text="Temperature : " + str(temperature), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Humidité Sol :" + str(humidite_sol), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Pression :" + str(pression), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Precipitation :" + str(precipitation), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Pluie :" + str(pluie), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Cycle Jour / Nuit :" + str(pluie), font=("caveat", 20), bg="black", fg="white")
    text.pack(side=BOTTOM)
    text = Label(frame, text="Altitude :" + str(humi), font=("caveat", 20), bg="black", fg="white")
    text.pack(side=BOTTOM)


# Page Home creer la fenetre d'accueil du jeu
def main():
    client = mqtt.Client()
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_KEEP_ALIVE_INTERVAL)
    client.username_pw_set(BROKER_USERNAME, BROKER_PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    # creer un thread pour la reception des messages
    client.loop_start()

    # -------------------------------------------------- Initialisation -------------------------------------------------- #

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
    text = Label(frame, text="Temperature : " + str(temperature), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Humidité Sol :" + str(humidite_sol), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Pression :" + str(pression), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Precipitation :" + str(precipitation), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Pluie :" + str(pluie), font=("caveat", 20), bg="black", fg="white")
    # Ajouter le label
    text.pack(side=BOTTOM)
    # Creation d'un label pour le texte
    text = Label(frame, text="Cycle Jour / Nuit :"+str(pluie), font=("caveat", 20), bg="black", fg="white")
    text.pack(side=BOTTOM)
    text = Label(frame, text="Altitude :"+str(humi), font=("caveat", 20), bg="black", fg="white")
    text.pack(side=BOTTOM)
    fenetre.mainloop()


main()