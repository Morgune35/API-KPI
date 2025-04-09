import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

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

# Couleurs avec un dégradé bleu et cyan
line_color = '#00FFFF'
fill_color = '#1E90FF'
point_color = '#00FFFF'

# Création du radar
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Tracés des lignes avec un dégradé (plus graphique)
ax.plot(angles, values, color=line_color, linewidth=2, linestyle='solid')
ax.fill(angles, values, color=fill_color, alpha=0.4)

# Ajouter les points à chaque sommet avec un effet lumineux
ax.scatter(angles, values, color=point_color, s=100, edgecolors='white', zorder=5, linewidth=2)

# Affichage des données à côté des points avec un léger effet d'ombre
for i, value in enumerate(values[:-1]):
    # Positionner les chiffres plus loin des points
    ax.text(angles[i], value + 12, f'{value}%', color=line_color, ha='center', va='center', fontsize=12, fontweight='bold',
            path_effects=[path_effects.withStroke(linewidth=3, foreground='black')],
            bbox=dict(facecolor='none', edgecolor=line_color, boxstyle="round,pad=0.3", lw=2))  # Boîte transparente avec contour turquoise

# Configurer les étiquettes avec une police moderne
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, color='white', fontsize=12, fontweight='bold')

# Configurer les cercles internes avec des lignes plus claires et nettes
ax.set_rlabel_position(0)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], color='lightgray', size=10)
ax.spines['polar'].set_color('#00FFFF')
ax.grid(color='#00FFFF', linestyle='dotted', linewidth=1, alpha=0.5)

# Titre avec un style plus fun et créatif
plt.title("🚀 Performance des KPI de la Supply Chain 🌟", size=20, color='white', pad=20, fontweight='bold', family='Segoe UI Emoji')

plt.tight_layout()
plt.show()
