import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Liste des KPI (labels) et leurs valeurs (exemple)
labels = [
    'Ponctualité Clients',
    'Stock/Ventes',
    'Coût Stock',
    'Ponctualité Fournisseurs',
    'DSI (Rotation Stock)',
    'Coût Transport/Tonne',
    'Commandes Parfaites',
    'Livraison Fournisseurs'
]

# Exemple de valeurs (entre 0 et 100 %)
values = [84, 25, 30, 70, 50, 60, 77, 70]

# Boucler les valeurs pour fermer le radar
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

# Personnalisation du thème
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#121212')  # fond de la figure

# Couleurs
line_color = '#00FFFF'
fill_color = '#00FFFF'
point_color = '#00FFFF'

# Création du radar
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Tracés des lignes
ax.plot(angles, values, color=line_color, linewidth=2, linestyle='solid')
ax.fill(angles, values, color=fill_color, alpha=0.25)

# Ajouter les points à chaque sommet
ax.scatter(angles, values, color=point_color, s=50, edgecolors='white', zorder=5)

# Configurer les étiquettes
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, color='white', fontsize=11, fontweight='bold')

# Configurer les cercles internes
ax.set_rlabel_position(0)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], color='gray', size=9)
ax.spines['polar'].set_color('#00FFFF')
ax.grid(color='#00FFFF', linestyle='dotted', linewidth=0.8, alpha=0.3)

# Titre
plt.title("Radar des KPI Supply Chain", size=16, color='white', pad=20)
plt.tight_layout()
plt.show()
