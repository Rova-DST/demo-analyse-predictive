# Ajout d'une gestion d'erreurs
def prevision_stock(historique_ventes):
    if not historique_ventes:
        return "Pas de données disponibles"
    moyenne_ventes = sum(historique_ventes) / len(historique_ventes)
    return int(moyenne_ventes * 1.1)
