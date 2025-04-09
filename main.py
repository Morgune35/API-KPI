import numpy as np
import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def charger_donnees_api():
    try:
        url = "http://10.101.1.116:8000/kpis"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()[0]

        # Exemple : on suppose que l'API retourne directement les KPI normalisés en %
        # Sinon, tu peux adapter avec des calculs comme dans la version précédente
        kpi_normalized = {
            'Ponctualité Commandes Clients': data.get("ponctualite_clients", 0),
            'Ratio Stock / Ventes': data.get("ratio_stock_ventes", 0) * 100,
            'Coût de Possession du Stock': data.get("cout_possession_stock", 0) / 1000,
            'Ponctualité Fournisseurs': data.get("ponctualite_fournisseurs", 0),
            'Durée Rotation des Stocks (DSI)': data.get("dsi", 0) / 10,
            'Coût de Transport par Tonne': data.get("cout_transport_tonne", 0) / 10,
            'Taux de Commandes Parfaites': data.get("commandes_parfaites", 0),
            'Livraison à l\'heure des Fournisseurs': data.get("ponctualite_fournisseurs", 0),
        }

        afficher_graphique(kpi_normalized)

    except requests.RequestException as e:
        messagebox.showerror("Erreur API", f"Impossible de récupérer les données :\n{e}")

def afficher_graphique(kpi_normalized):
    for widget in frame_graphique.winfo_children():
        widget.destroy()

    labels = list(kpi_normalized.keys())
    values = list(kpi_normalized.values())
    values += values[:1]  # pour fermer le radar
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    # Style graphique inspiré du visuel fourni
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#121212')

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Radar
    ax.plot(angles, values, color='#00FFFF', linewidth=2)
    ax.fill(angles, values, color='#00FFFF', alpha=0.3)
    ax.scatter(angles, values, color='#00FFFF', s=50, edgecolors='white', zorder=5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10, color='white')

    ax.set_rlabel_position(0)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], color='gray', size=9)
    ax.grid(color='#00FFFF', linestyle='dotted', linewidth=0.8, alpha=0.3)
    ax.spines['polar'].set_color('#00FFFF')

    ax.set_title("Radar KPI (données API)", size=16, color='white', pad=20)

    canvas = FigureCanvasTkAgg(fig, master=frame_graphique)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Interface Tkinter
root = tk.Tk()
root.title("Analyse KPI - Source API")

# Bouton API
btn_api = tk.Button(root, text="Charger les KPI depuis l'API", command=charger_donnees_api, bg="#00CCCC", fg="white", font=("Arial", 12, "bold"))
btn_api.pack(pady=15)

# Zone de graphique
frame_graphique = tk.Frame(root, bg="#121212")
frame_graphique.pack(padx=10, pady=10)

# Lancer l'interface
root.mainloop()
