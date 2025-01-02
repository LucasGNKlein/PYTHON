
import random
from stories import STORY_TEMPLATES
from data import NAMES, PLACES, OBJECTS, ACTIONS

def generate_story():
    template = random.choice(STORY_TEMPLATES)
    story = template.format(
        name=random.choice(NAMES),
        place=random.choice(PLACES),
        object=random.choice(OBJECTS),
        action=random.choice(ACTIONS)
    )
    return story

def main():
    print("=== Gerador de Histórias Aleatórias ===")
    while True:
        print("\nSua história:")
        print(generate_story())
        cont = input("\nGerar outra história? (s/n): ").strip().lower()
        if cont != 's':
            break

if __name__ == "__main__":
    main()
