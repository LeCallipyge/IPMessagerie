import socket
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext

# === Fenêtre de configuration ===
config_fenetre = tk.Tk()
config_fenetre.title("Configuration Client")
config_fenetre.geometry("250x200")

tk.Label(config_fenetre, text="Adresse IP du serveur :").pack(pady=5)
ip_entry = ttk.Entry(config_fenetre)
ip_entry.insert(0, "127.0.0.1")  # localhost par défaut
ip_entry.pack(pady=5)

tk.Label(config_fenetre, text="Port du serveur :").pack(pady=5)
port_entry = ttk.Entry(config_fenetre)
port_entry.insert(0, "5566")
port_entry.pack(pady=5)

def lancer_client():
    global host, port
    host = ip_entry.get()
    port = int(port_entry.get())
    config_fenetre.destroy()

ttk.Button(config_fenetre, text="Se connecter", command=lancer_client).pack(pady=10)
config_fenetre.mainloop()

# === Connexion au serveur ===
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# === Interface chat ===
fenetre = tk.Tk()
fenetre.title(f"Client - {host}:{port}")
fenetre.geometry("400x500")

zone_texte = scrolledtext.ScrolledText(fenetre, state='disabled', wrap=tk.WORD)
zone_texte.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

cadre_bas = ttk.Frame(fenetre)
cadre_bas.pack(fill=tk.X, padx=10, pady=10)

champ_message = ttk.Entry(cadre_bas)
champ_message.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

def afficher_message(msg):
    zone_texte.config(state='normal')
    zone_texte.insert(tk.END, msg + "\n")
    zone_texte.config(state='disabled')
    zone_texte.yview(tk.END)

def envoyer_message(event=None):
    message = champ_message.get()
    if message.strip():
        client_socket.sendall(message.encode("utf8"))
        afficher_message(f"Moi : {message}")
        champ_message.delete(0, tk.END)

bouton_envoyer = ttk.Button(cadre_bas, text="Envoyer", command=envoyer_message)
bouton_envoyer.pack(side=tk.RIGHT)
fenetre.bind("<Return>", envoyer_message)

def recevoir_message():
    while True:
        try:
            message_recu = client_socket.recv(1024)
            if not message_recu:
                break
            message = message_recu.decode("utf8")
            afficher_message(f"Serveur : {message}")
        except:
            break

thread_recevoir = threading.Thread(target=recevoir_message, daemon=True)
thread_recevoir.start()

afficher_message("Connecté au serveur")

fenetre.mainloop()
