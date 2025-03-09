import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Charger les données
file_path = r"C:\Users\user\Downloads\Votre Avis Compte! Aidez-nous à créer l'application sportive ultime! (Responses) - Form Responses 1.csv" 
df = pd.read_csv(file_path)

# Nettoyer les colonnes
df.columns = [col.strip() for col in df.columns]

# Titre du Dashboard
st.title("📊 Dashboard : Analyse du Sondage Sportif")

# Sélection de l'analyse
option = st.sidebar.selectbox(
    "Choisissez une analyse",
    ["Tranche d'âge", "Fréquence Sportive", "Sports Pratiqués", "Applications Sportives", "Fonctionnalités Demandées"]
)

# 1️⃣ Répartition des tranches d'âge
if option == "Tranche d'âge":
    st.subheader("Répartition des tranches d'âge")
    age_counts = df["Quel est votre âge ? (Veuillez sélectionner une tranche d'âge)"].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=age_counts.index, y=age_counts.values, ax=ax, palette="viridis")
    ax.set_xlabel("Tranche d'âge")
    ax.set_ylabel("Nombre de répondants")
    st.pyplot(fig)

# 2️⃣ Fréquence de pratique sportive
elif option == "Fréquence Sportive":
    st.subheader("Fréquence de pratique sportive")
    freq_counts = df["À quelle fréquence pratiquez-vous une activité sportive ?"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(freq_counts, labels=freq_counts.index, autopct='%1.1f%%', colors=sns.color_palette("viridis", len(freq_counts)))
    st.pyplot(fig)

# 3️⃣ Sports les plus pratiqués
elif option == "Sports Pratiqués":
    st.subheader("Sports les plus pratiqués")
    sports_list = df["Quels sports pratiquez-vous ? (Plusieurs réponses possibles)"].dropna().str.split(", ")
    all_sports = [sport for sublist in sports_list for sport in sublist]
    sports_counts = Counter(all_sports)
    sports_df = pd.DataFrame(sports_counts.items(), columns=["Sport", "Nombre de pratiquants"]).sort_values(by="Nombre de pratiquants", ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=sports_df["Sport"], x=sports_df["Nombre de pratiquants"], ax=ax, palette="viridis")
    ax.set_xlabel("Nombre de pratiquants")
    ax.set_ylabel("Sports")
    st.pyplot(fig)

# 4️⃣ Fonctionnalités les plus demandées
elif option == "Fonctionnalités Demandées":
    st.subheader("Fonctionnalités les plus demandées")
    features_list = df["Quelles fonctionnalités seraient les plus importantes pour vous dans une application sportive ? (Plusieurs réponses possibles)"].dropna().str.split(", ")
    all_features = [feature.strip() for sublist in features_list for feature in sublist]
    all_features = [feature for feature in all_features if "@" not in feature and not feature.isnumeric()]
    features_counts = Counter(all_features)
    features_df = pd.DataFrame(features_counts.items(), columns=["Fonctionnalité", "Nombre de votes"]).sort_values(by="Nombre de votes", ascending=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=features_df["Fonctionnalité"], x=features_df["Nombre de votes"], ax=ax, palette="rocket")
    ax.set_xlabel("Nombre de votes")
    ax.set_ylabel("Fonctionnalités")
    st.pyplot(fig)

# 5️⃣ Utilisation des applications sportives
elif option == "Applications Sportives":
    st.subheader("Utilisation des applications sportives")
    apps_counts = df["Utilisez-vous actuellement des applications mobiles pour le sport ? Si oui, lesquelles ? (Plusieurs réponses possibles)"].value_counts()
    
    fig, ax = plt.subplots()
    ax.pie(apps_counts, labels=apps_counts.index, autopct='%1.1f%%', colors=sns.color_palette("viridis", len(apps_counts)))
    st.pyplot(fig)

