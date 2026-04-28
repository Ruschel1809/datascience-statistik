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

# Liste der Attribute, die wir vergleichen wollen
features = ['Outlook', 'Humidity']
target = 'PlayTennis'

# Berechne Informationsgewinn für jedes Feature
gains = {}
for feature in features:
    gain = information_gain(data, feature, target)
    gains[feature] = gain
    print(f"Informationsgewinn für '{feature}': {gain:.4f}")

# Bestes Feature finden
best_feature = max(gains, key=gains.get)
print(f"\n  Bestes Attribut ist: '{best_feature}' mit einem Informationsgewinn von {gains[best_feature]:.4f}")
