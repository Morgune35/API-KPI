

---

# 📊 Visualisation des KPI Mensuels (2025)

Ce script Python récupère, filtre, et visualise des indicateurs de performance (KPI) au format graphique radar, pour chaque mois de l'année 2025. Il utilise les bibliothèques `matplotlib`, `numpy` et `requests` pour générer des graphiques interactifs et esthétiques sur fond sombre.

## 🔧 Fonctionnalités

- Récupération des données via une API HTTP
- Filtrage des données sur une période définie (ici, l'année 2025)
- Agrégation mensuelle des KPI
- Génération de graphiques radar pour chaque mois
- Design en mode sombre et responsive (grille ajustable)
- Gestion des erreurs (réseau, données mal formées)

---

## 🗂️ Structure du Code

### 1. **Paramètres de filtrage**
```python
date_debut = datetime(2025, 1, 1)
date_fin = datetime(2025, 12, 31)
```

### 2. **Récupération des données**
Les données sont obtenues depuis l'URL : `http://10.101.1.116:8000/kpis`.

### 3. **Filtrage des données**
On conserve uniquement les données dont la date est comprise entre `date_debut` et `date_fin`.

### 4. **Agrégation**
Les données sont regroupées par mois et par nom de KPI pour calculer une moyenne mensuelle.

### 5. **Visualisation**
Pour chaque mois, un **graphe radar** est tracé représentant les moyennes de tous les KPI pour ce mois.

---

## 📦 Dépendances

Installe les dépendances via pip :

```bash
pip install numpy matplotlib requests
```

---

## 📈 Exemple de rendu

Le script affiche une série de graphiques en radar, un par mois, avec :

- Les KPI disposés autour du cercle
- Les valeurs moyennes représentées par des lignes et des zones remplies
- Un style sombre élégant et lisible

---

## 📌 Remarques

- Assure-toi que l’URL de l’API est accessible depuis ton réseau local.
- Si l’API ne retourne pas de données ou est indisponible, un message d’erreur est affiché.
- Les KPI dont la date est mal formatée sont ignorés.

---

## ✍️ Auteur

Projet de visualisation KPI – 2025  
Réalisé dans le cadre d’un projet de gestion de données et visualisation.

---
