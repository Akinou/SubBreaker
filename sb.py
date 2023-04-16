import string

# Fonction pour chiffrer un message avec un chiffrement de substitution monoalphabétique
def monoalphabetic_substitution_encrypt(message, key):
    # On crée une table de correspondance qui permet de chiffrer les lettres
    translation_table = str.maketrans(string.ascii_lowercase, key.lower())
    # On chiffre le message en utilisant la table de correspondance
    ciphertext = message.translate(translation_table)
    return ciphertext

# Fonction pour générer une clé aléatoire pour un chiffrement de substitution monoalphabétique
def generate_random_key():
    # On crée une liste contenant toutes les lettres de l'alphabet en ordre aléatoire
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    # On crée la clé en associant chaque lettre de l'alphabet à une lettre dans la liste
    key = ''.join(letters)
    return key

# Fonction pour effectuer une attaque de cryptanalyse par substitution fréquentielle
def frequency_analysis_attack(ciphertext):
    # On calcule la fréquence de chaque lettre dans le texte chiffré
    freq = {}
    for char in ciphertext:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in freq:
                freq[char_lower] += 1
            else:
                freq[char_lower] = 1
    # On trie les lettres par fréquence décroissante
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # On crée une table de correspondance entre les lettres du texte chiffré et les lettres de la langue anglaise
    correspondence_table = {}
    for i in range(len(freq_sorted)):
        correspondence_table[freq_sorted[i][0]] = string.ascii_lowercase[i]
    # On déchiffre le texte chiffré à l'aide de la table de correspondance
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            char_lower = char.lower()
            plaintext += correspondence_table[char_lower].upper() if char.isupper() else correspondence_table[char_lower]
        else:
            plaintext += char
    return plaintext

# Fonction pour effectuer une attaque de cryptanalyse par force brute
def brute_force_attack(ciphertext, max_key_length):
    # On crée une liste de toutes les lettres de l'alphabet
    alphabet = list(string.ascii_lowercase)
    # On initialise une variable pour stocker le message déchiffré
    plaintext = ""
    # On essaie toutes les combinaisons possibles de clé
    for key_length in range(1, max_key_length + 1):
        for key in itertools.product(alphabet, repeat=key_length):
            key = ''.join(key)
            candidate_plaintext = monoalphabetic_substitution_encrypt(ciphertext, key)
            if is_english(candidate_plaintext):
                plaintext = candidate_plaintext
                break
        if plaintext:
            break
    return plaintext

# Fonction pour déterminer si un texte est en anglais
def is_english(text):
    # On calcule le pourcentage de lettres anglaises dans le texte
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_letter_count = sum(text.lower().count(letter) for letter in english_letters)
    text_letter_count = len([char for char in text.lower() if char.isalpha()])
   
