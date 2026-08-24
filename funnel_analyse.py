# Importation des librairies
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuration esthétique
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# 1. Chargement du jeu de données
df = pd.read_csv("user_data.csv")

print("--- APERÇU DES DONNÉES DU FUNNEL ---")
print(df.head(5))
print(f"\nNombre total de lignes / interactions : {df.shape[0]:,}")

# 2. Analyse des étapes du funnel et des taux de conversion
# Regroupons par étape (stage) pour voir le nombre d'utilisateurs et le taux de succès (conversion = True)
funnel_summary = (
    df.groupby("stage")
    .agg(
        total_users=("user_id", "count"),
        converted_users=("conversion", lambda x: (x == True).sum()),
    )
    .reset_index()
)

# Calcul du taux de conversion par étape
funnel_summary["conversion_rate_%"] = (
    funnel_summary["converted_users"] / funnel_summary["total_users"]
) * 100

print("\n" + "=" * 50)
print("RAPPORT DE PERFORMANCE DE L'ENTONNOIR (FUNNEL)")
print("=" * 50)
print(funnel_summary)

# 3. Génération d'un graphique de l'entonnoir
plt.figure(figsize=(8, 5))
sns.barplot(
    data=funnel_summary,
    x="stage",
    y="total_users",
    palette="Blues_r",
    hue="stage",
    legend=False,
)
plt.title(
    "Volume d'Utilisateurs par Étape du Funnel Marketing",
    fontsize=13,
    fontweight="bold",
)
plt.xlabel("Étape du Funnel (Stage)", fontsize=11)
plt.ylabel("Nombre d'Utilisateurs", fontsize=11)
plt.tight_layout()
plt.show()