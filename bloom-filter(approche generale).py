from bloom_filter import BloomFilter

# Créer un filtre de Bloom avec une capacité de 100 éléments et un taux d'erreur de 0.1%
bloom = BloomFilter(max_elements=100, error_rate=0.001)

# Ajouter des éléments au filtre de Bloom
bloom.add("element1")
bloom.add("element2")

# Vérifier si un élément est présent
print("element1" in bloom)  # True
print("element3" in bloom)  # False