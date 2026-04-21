# vergleich zwei Features:
import math
from collections import Counter

# Beispiel-Daten mit zwei Attributen
data = [
    {'Outlook': 'Sunny',    'Humidity': 'High',   'PlayTennis': 'No'},
    {'Outlook': 'Sunny',    'Humidity': 'High',   'PlayTennis': 'No'},
    {'Outlook': 'Overcast', 'Humidity': 'High',   'PlayTennis': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'High',   'PlayTennis': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'Normal', 'PlayTennis': 'No'},
    {'Outlook': 'Rain',     'Humidity': 'Normal', 'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Humidity': 'Normal', 'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny',    'Humidity': 'High',   'PlayTennis': 'No'},
    {'Outlook': 'Sunny',    'Humidity': 'Normal', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'High',   'PlayTennis': 'Yes'},
    {'Outlook': 'Sunny',    'Humidity': 'Normal', 'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Humidity': 'High',   'PlayTennis': 'Yes'},
    {'Outlook': 'Overcast', 'Humidity': 'Normal', 'PlayTennis': 'Yes'},
    {'Outlook': 'Rain',     'Humidity': 'High',   'PlayTennis': 'No'},
]

def entropy(labels):
    total = len(labels)
    counts = Counter(labels)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

def information_gain(data, attribute, target):
    total_labels = [row[target] for row in data]
    total_entropy = entropy(total_labels)
    values = set(row[attribute] for row in data)

    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attribute] == value]
        subset_labels = [row[target] for row in subset]
        weight = len(subset) / len(data)
        weighted_entropy += weight * entropy(subset_labels)

    return total_entropy - weighted_entropy

# 🔍 Liste der Attribute, die wir vergleichen wollen
features = ['Outlook', 'Humidity']
target = 'PlayTennis'

# 📊 Berechne Informationsgewinn für jedes Feature
gains = {}
for feature in features:
    gain = information_gain(data, feature, target)
    gains[feature] = gain
    print(f"Informationsgewinn für '{feature}': {gain:.4f}")

# 🥇 Bestes Feature finden
best_feature = max(gains, key=gains.get)
print(f"\n➡️  Bestes Attribut ist: '{best_feature}' mit einem Informationsgewinn von {gains[best_feature]:.4f}")


# mit pandas:
# import pandas as pd
# import math
# from collections import Counter
#
# # Beispiel-Daten
# data = pd.DataFrame({
#     'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast',
#                 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
#     'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes',
#                    'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
# })
#
# # Entropie-Berechnung
# def entropy(labels):
#     total = len(labels)
#     counts = Counter(labels)
#     return -sum((count/total) * math.log2(count/total) for count in counts.values())
#
# # Informationsgewinn für ein Attribut berechnen
# def information_gain(df, attribute, target):
#     total_entropy = entropy(df[target])
#     values = df[attribute].unique()
#     weighted_entropy = 0
#
#     for value in values:
#         subset = df[df[attribute] == value]
#         weight = len(subset) / len(df)
#         subset_entropy = entropy(subset[target])
#         weighted_entropy += weight * subset_entropy
#
#     return total_entropy - weighted_entropy
#
# # Anwendung
# gain = information_gain(data, 'Outlook', 'PlayTennis')
# print(f"Informationsgewinn für 'Outlook': {gain:.4f}")

# ohne pandas:
# import math
# from collections import Counter
#
# # Die Daten: eine Liste von Beispielen (Dictionary pro Beispiel)
# data = [
#     {'Outlook': 'Sunny',    'PlayTennis': 'No'},
#     {'Outlook': 'Sunny',    'PlayTennis': 'No'},
#     {'Outlook': 'Overcast', 'PlayTennis': 'Yes'},
#     {'Outlook': 'Rain',     'PlayTennis': 'Yes'},
#     {'Outlook': 'Rain',     'PlayTennis': 'No'},
#     {'Outlook': 'Rain',     'PlayTennis': 'Yes'},
#     {'Outlook': 'Overcast', 'PlayTennis': 'Yes'},
#     {'Outlook': 'Sunny',    'PlayTennis': 'No'},
#     {'Outlook': 'Sunny',    'PlayTennis': 'Yes'},
#     {'Outlook': 'Rain',     'PlayTennis': 'Yes'},
#     {'Outlook': 'Sunny',    'PlayTennis': 'Yes'},
#     {'Outlook': 'Overcast', 'PlayTennis': 'Yes'},
#     {'Outlook': 'Overcast', 'PlayTennis': 'Yes'},
#     {'Outlook': 'Rain',     'PlayTennis': 'No'},
# ]
#
# # Funktion zur Berechnung der Entropie einer Liste von Zielwerten
# def entropy(labels):
#     total = len(labels)
#     counts = Counter(labels)
#     return -sum((count/total) * math.log2(count/total) for count in counts.values())
#
# # Funktion zur Berechnung des Informationsgewinns
# def information_gain(data, attribute, target):
#     # Gesamte Entropie berechnen
#     total_labels = [row[target] for row in data]
#     total_entropy = entropy(total_labels)
#
#     # Werte des Attributs sammeln
#     values = set(row[attribute] for row in data)
#
#     # Gewichtete Entropie berechnen
#     weighted_entropy = 0
#     for value in values:
#         subset = [row for row in data if row[attribute] == value]
#         subset_labels = [row[target] for row in subset]
#         weight = len(subset) / len(data)
#         weighted_entropy += weight * entropy(subset_labels)
#
#     # Informationsgewinn = Gesamtentropie - gewichtete Entropie
#     return total_entropy - weighted_entropy
#
# # Anwendung
# gain = information_gain(data, attribute='Outlook', target='PlayTennis')
# print(f"Informationsgewinn für 'Outlook': {gain:.4f}")