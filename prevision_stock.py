def prevision_stock(historique_ventes):
    moyenne_ventes = sum(historique_ventes) / len(historique_ventes)
    return int(moyenne_ventes * 1.1)  # Prévision avec une marge de 10%

# Exemple d'utilisation
print(prevision_stock([100, 120, 110, 115]))
