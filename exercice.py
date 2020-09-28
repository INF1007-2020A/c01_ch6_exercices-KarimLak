#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        value = [input("Entrez un nombre : ") for n in range(10)]
   

    return value == sorted(values)




def anagrams(words: list = None) -> bool:
    if words is None:
        words = [input("Entrez deux mots : ") for n in range(2)]
        first_word = sorted(words[0])
        second_word = sorted(words[1])
        
        if first_word == second_word:
            return True
        else :
            return False
        
      
 


def contains_doubles(items: list) -> bool:
    uniques = set(items)
    return len(items) == len(uniques) 


def best_grades(student_grades: dict) -> dict:
    

S = 0
for i in student_grades : 
  S = student_grades[i] + S
Moyenne = S/(len(student_grades))
print(f"La moyenne est de {Moyenne}")
note_max = 0
for j in student_grades : 
          
  if student_grades[j] > note_max:
    note_max = student_grades[j]
print(f"Meilleur note est de {note_max}")


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
