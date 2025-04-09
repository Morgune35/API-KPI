import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import requests
from collections import defaultdict
from datetime import datetime

# Paramètres de filtrage
date_debut = datetime(2025, 1, 1)
date_fin = datetime(2025, 12, 31)

# Récupérer les données
url = 'http://10.101.1.116:8000/kpis'

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la récupération des données : {e}")
    data = []

# Filtrage des données par date
donnees_filtrees = []
for item in data:
    try:
        date_obj = datetime.strptime(item["date"], "%Y-%m-%d")
        if date_debut <= date_obj <= date_fin:
            item["date_obj"] = date_obj
            donnees_filtrees.append(item)
    except ValueError:
        print(f"Date invalide ignorée : {item.get('date')}")

# Regrouper par (mois, KPI)
mensuel_kpis = defaultdict(lambda: defaultdict(list))
for item in donnees_filtrees:
    mois = item["date_obj"].strftime("%Y-%m")  # ex: '2025-03'
    kpi = item["kpi_name"]
    value = item["value"]
    mensuel_kpis[mois][kpi].append(value)

# Liste de tous les KPI pour un ordre cohérent
tous_kpis = sorted({item["kpi_name"] for item in donnees_filtrees})
angles = np.linspace(0, 2 * np.pi, len(tous_kpis), endpoint=False).tolist()
angles += angles[:1]

# Design général
plt.style.use('dark_background')
ncols = 3
nrows = int(np.ceil(len(mensuel_kpis) / ncols))
fig, axs = plt.subplots(nrows, ncols, figsize=(18, nrows * 6), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#121212')
axs = axs.flatten()

# Couleurs
line_color = '#00FFFF'
fill_color = '#1E90FF'
point_color = '#00FFFF'

# Tracer chaque mois
for idx, (mois, kpis) in enumerate(sorted(mensuel_kpis.items())):
    ax = axs[idx]
    moyennes = [np.mean(kpis.get(kpi, [0])) for kpi in tous_kpis]
    moyennes += moyennes[:1]  # boucle

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.plot(angles, moyennes, color=line_color, linewidth=2)
    ax.fill(angles, moyennes, color=fill_color, alpha=0.3)
    ax.scatter(angles, moyennes, color=point_color, s=80, edgecolors='white', linewidth=1.5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(tous_kpis, color='white', fontsize=10, fontweight='bold')

    ax.set_rlabel_position(0)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], color='lightgray', size=9)
    ax.spines['polar'].set_color('#00FFFF')
    ax.grid(color='#00FFFF', linestyle='dotted', linewidth=1, alpha=0.4)

    ax.set_title(f"📆 {mois}", color='white', fontsize=14, pad=20)

# Supprimer les sous-graphiques vides si moins de 12 mois
for i in range(len(mensuel_kpis), len(axs)):
    fig.delaxes(axs[i])

plt.suptitle("📈 Évolution Mensuelle des KPI - 2025", color='white', fontsize=20, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
