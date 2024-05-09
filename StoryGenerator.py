import customtkinter as Ctk
from PIL import Image
import random


Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")



class StoryGenApp:
    def __init__(self):
        self.root = root
        self.root.title("Story Generator")
        self.root.geometry("500x500")
        self.root.resizable(False,False)
        
        self.setup_ui()

    def generate_story(self):
        story_templates = [
            "Once upon a time, there was  {name} who lived in  {place}.",
            "In  {place} far away, {name} found a magical {object}.",
            "Legend has it that {name} once saved the {animal} of {place} from a terrible fate.",
            "The kingdom of {place} was in danger, but {name} rose to the challenge and saved the day."
            "Deep in the {place}, {name} discovered a hidden {object} that would change their life forever.",
            "As the sun set on {place}, {name} embarked on a journey to find the legendary {animal} that was said to possess great powers.",
            "In the ancient city of {place}, {name} uncovered a secret that had been buried for centuries.",
            "Many years ago, {name} stumbled upon a {object} that granted them the ability to {action} at will.",
            "On the eve of the {event} festival, {name} stumbled upon a mysterious {object} that led them on a quest to {action}.",
            "In the heart of the {place}, {name} encountered a mystical {animal} that could speak the language of humans.",
            "Legend speaks of  {place} where {name} found a {object} that granted them eternal {attribute}.",
            "In the land of {place}, {name} was known as the {title} who possessed the {object} of {place}.",
            "On the edge of the {place}, {name} discovered a portal to another {world} where {animal} ruled supreme.",
            "After years of searching, {name} finally found the {object} that would fulfill their greatest {dream}.",
            "Under the starry skies of {place}, {name} made a pact with the {animal} to protect the {place} from {danger}.",

        ]

        story_templates1 = [
            "{name} lived in a {place}.",
            "{name} found a magical {object} in a {place} far away.",
            "{name} once saved the {animal} of {place} from a terrible fate.",
            "The kingdom of {place} was in danger, but {name} rose to the challenge and saved the day.",
            "{name} discovered a hidden {object} in the {place} that would change their life forever.",
            "As the sun set on {place}, {name} embarked on a journey to find the legendary {animal} that was said to possess great powers.",
            "{name} uncovered a secret in the ancient city of {place} that had been buried for centuries.",
            "{name} stumbled upon a {object} many years ago that granted them the ability to {action} at will.",
            "On the eve of the {event} festival, {name} stumbled upon a mysterious {object} that led them on a quest to {action}.",
            "{name} encountered a mystical {animal} in the heart of the {place} that could speak the language of humans.",
            "Legend speaks of {name} finding a {object} in a {place} where they granted them eternal {attribute}.",
            "In the land of {place}, {name} was known as the {title} who possessed the {object} of {place}.",
            "{name} discovered a portal on the edge of {place} to another {world} where {animal} ruled supreme.",
            "{name} finally found the {object} that would fulfill their greatest {dream} after years of searching.",
            "Under the starry skies of {place}, {name} made a pact with the {animal} to protect the {place} from {danger}.",
            "{name} stumbled upon a hidden {object} in the midst of a {event} that revealed the true nature of {place}.",
            "{name} encountered a {animal} that could grant wishes to those who proved themselves worthy as they journeyed through the {place}.",
            "{name} found a {object} in the ruins of {place} that allowed them to communicate with the spirits of the {animal}.",
            "{name} discovered a {object} many moons ago that could turn dreams into reality, but at a great cost.",
            "{name} uncovered a conspiracy on the day of the {event} that threatened to plunge the {place} into chaos.",
            "{name} encountered a {animal} that was rumored to hold the key to immortality as they ventured into the {world}.",
            "{name} discovered a {object} in the heart of the {world} that could bring about the end of {place} as they knew it.",
            "Legend tells of {name} becoming the {title} in a {place} where they wielded the {object} of {place} against the {danger}.",
            "{name} found a {object} in a hidden corner of {place} that revealed the true history of the {world} and its {animal}.",
            "{name} was bestowed with the {title} long ago for their bravery in facing the {danger} that threatened to consume the {place}."
        ]

        story_templates2 = [
            "{name}, a {title} known for their {attribute}, discovered a {object} that could bring about the {dream} of {place}, but also its {danger}. With great {attribute}, they had to make a choice that would impact the fate of {place}.",
            "{name}, a {title} with a deep desire for {dream}, ventured into the {world} in search of a {object} that could make their {dream} a reality. However, using this {object} came with a great {danger} that threatened to destroy {place}.",
            "{name}, a {title} known for their {attribute}, uncovered a conspiracy on the day of the {event} that threatened to plunge the {place} into chaos. With their {attribute} and {object}, they thwarted the conspiracy and saved the {place}.",
            "{name}, a {title} of {place}, ventured into the {world} in search of a {animal} that was rumored to hold the key to immortality. After a perilous journey, they encountered the {animal} and discovered the truth about immortality.",
            "{name}, a {title} with a reputation for {attribute}, discovered a {object} in the heart of the {world} that could bring about the end of {place} as they knew it. With great {attribute}, they made the ultimate sacrifice to protect {place}.",
            "Legend tells of {name}, a {title} who became the {title} in a {place} where they wielded the {object} of {place} against the {danger}. With the {object} in hand, they vanquished the {danger} and saved {place} from destruction.",
            "{name}, a {title} known for their {attribute}, found a {object} in a hidden corner of {place} that revealed the true history of the {world} and its {animal}. This discovery changed the course of history for {place} and its {animal}.",
            "{name}, a {title} bestowed with the {title} long ago for their bravery, returned to {place} many years after the {event} to find that the {object} they had once found had vanished. This disappearance led them on a new quest to uncover its whereabouts.",
            "{name}, a {title} who was on their deathbed, revealed the location of the {object} to their successor, who would carry on their legacy of {dream} and {action}. This act ensured that {name}'s {dream} would live on for generations to come.",
            "{name}, a {title} with a reputation for {attribute}, discovered a {object} in a hidden cave. This {object} was said to grant {dream}, but only to those who could pass its {danger}. {name} took on the challenge and emerged victorious, forever changed by the experience.",
            "{name}, a {title} known for their {attribute}, stumbled upon a {object} that could manipulate time itself. With this {object}, {name} was able to fulfill their {dream}, but soon realized the {danger} of altering the course of time.",
            "{name}, a {title} of {place}, discovered an ancient {object} that could control the elements. With this {object}, {name} protected {place} from natural disasters and became known as the {title} of the elements.",
            "{name}, a {title} with a longing for {dream}, discovered a {object} that could grant any wish. However, each wish came with a {danger} that {name} had to overcome. In the end, {name} learned that true fulfillment comes from within.",
            "{name}, a {title} who sought {dream}, found a {object} that could create anything they desired. With this {object}, {name} built a {place} of wonders, but soon realized that some {dream} are best left unrealized.",
            "{name}, a {title} known for their {attribute}, discovered a {object} that could unlock the secrets of the mind. With this {object}, {name} delved into the depths of their own psyche, confronting their fears and desires in a journey of self-discovery."
        ]


                
        place = random.choice(["Alcaxarzaray", "The 9 Pillers of Gusu", "WeiYang Mound", "Atlantis","Atlantis", "El Dorado", "Troy", "Babylon", "Shangri-La", "Avalon", "Lemuria", "Mu", "Hyperborea", "Agartha", "Thule", "Camelot", "Ys", "Tartessos", "Iram of the Pillars", "Cockaigne", "Shambhala", "Kitezh", "Aztlan", "Dilmun"])
        animal = random.choice(["dragon", "unicorn", "griffin", "phoenix", "gryphon"])
        name = random.choice(["Kyle", "Mikey", "Jessie", "Machibuster", "Layla"])
        object = random.choice(["ball", "magical tooth", "toast", "garlic", "slipper"])
        dream = random.choice(["fame","fortune","love","adventure","success","peace","happiness","knowledge","power","freedom"])

        danger = random.choice(["darkness","evil","monsters","war","destruction","chaos","betrayal","curses","loss","temptation"])

        event = random.choice(["harvest","full moon","celebration","ceremony","tournament","feast","ritual","competition","ritual","trial"])
        attribute = random.choice(["bravery", "wisdom", "strength", "intelligence", "kindness", "cunning", "power", "beauty", "loyalty", "magic"])
        title = random.choice(["chosen one", "hero", "savior", "legend", "warrior", "mage", "king", "queen", "prince", "princess"])
        action = random.choice(["fly", "teleport", "shapeshift", "control minds", "summon storms", "heal", "create illusions", "move objects with their mind", "become invisible", "breathe underwater"])
        world = random.choice(["fantasy", "mythical", "magical", "enchanted", "mystical", "fairy-tale", "legendary", "otherworldly", "supernatural", "whimsical"])
        
        story_template = random.choice(story_templates) +" "+ random.choice(story_templates1)  +" "+ random.choice(story_templates2)
        story = story_template.format(name=name,place=place, animal=animal, object=object, danger=danger, dream=dream, event=event, attribute=attribute, title=title,action=action, world=world)
        self.labelstory.configure(text=story)

    
    def setup_ui(self):
        self.title = Ctk.CTkLabel(self.root, text= "   Story \n  Generator",font=('FangSong ti', 45))
        self.title.place(x=80, y =17)

        self.generate = Ctk.CTkButton(self.root,text="Generate", width=80, height=40, command=self.generate_story)
        self.generate.place(x= 210, y = 420)

        self.labelstory = Ctk.CTkLabel(self.root, text='',font=('FangSong ti', 15),wraplength=400, justify="center")
        self.labelstory.place(x=60, y = 140)



if __name__ == "__main__":
    root = Ctk.CTk()
    app = StoryGenApp()
    root.mainloop()