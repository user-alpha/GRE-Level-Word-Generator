import random
import os.path
import tkinter as tk
from tkinter import messagebox

words = [
    "abate", "aberrant", "abstemious", "acumen", "adamant", "adulterate",
    "adversary", "aesthetic", "alacrity", "aloof", "ameliorate", "amenable",
    "anachronism", "anomaly", "antipathy", "apathy", "apogee", "approbation",
    "arbitrary", "ascendancy", "ascertain", "ascetic", "aspersion", "assuage",
    "attenuate", "augment", "auspicious", "avarice", "aver", "aversion",
    "avow", "awry", "bolster", "bombast", "bucolic", "bungle", "buttress",
    "byzantine", "capricious", "castigation", "cataclysm", "caustic", "censure",
    "chicanery", "cogent", "complaisance", "concomitant", "condone", "confound",
    "congruent", "contempt", "contentious", "contrite", "conundrum", "conviction",
    "credulous", "culpable", "daunt", "dearth", "debacle", "decorum", "deference",
    "defray", "deleterious", "demur", "deride", "derivative", "descant", "desiccate",
    "desuetude", "deterrent", "deviance", "dexterous", "diaphanous", "diatribe",
    "dichotomy", "diffidence", "dilate", "disabuse", "discord", "discretion",
    "disenfranchise", "disparate", "disproof", "dissemble", "divest", "dogmatic",
    "ebullience", "economical", "effrontery", "egregious", "elegy", "elicit",
    "embroil", "emend", "emollient", "empirical", "encumber", "endemic",
    "enervate", "enumerate", "ephemeral", "equanimity", "equivocate", "erudite",
    "eschew", "evanescent", "evocative", "exculpate", "exigent", "exonerate",
    "extant", "extempore", "extenuate", "extirpate", "facetious", "fallacy",
    "fastidious", "fatuous", "fawn", "felicitous", "fractious", "fraternity",
    "fulminate", "gainsay", "garnish", "gauche", "germane", "glut", "grandiose",
    "gregarious", "halcyon", "harangue", "harbinger", "haughty", "heterogeneous",
    "hyperbole", "hypothesis", "iconoclast", "idolatrous", "ignominy", "imbibe",
    "immutable", "impair", "impartial", "impecunious", "impertinent", "impinge",
    "implacable", "importune", "impugn", "incontrovertible", "incursion", "indefatigable",
    "indigence", "indolence", "ineluctable", "infelicitous", "infer", "infraction",
    "infrastructure", "ingrain", "innocuous", "insidious", "insipid", "insurgent",
    "interlocutor", "interminable", "intransigent", "inured", "invective", "irascible",
    "irresolute", "itinerant", "jettison", "jocular", "juxtaposition", "laconic",
    "largess", "levee", "lexicon", "loathe", "luminescence", "macabre", "magnanimous",
    "malevolence", "malleable", "martial", "maverick", "mendacity", "mercurial",
    "metamorphosis", "meticulous", "misanthrope", "miscellany", "modicum", "mollify",
    "multifarious", "nebulous", "nefarious", "negligible", "neophyte", "noisome",
    "nonplussed", "obdurate", "obfuscate", "obsequious", "obviate", "occlude",
    "officious", "onerous", "opulence", "oscillate", "ostensible", "palliate",
    "palpable", "paragon", "parity", "parsimony", "partisan", "pathos", "pellucid",
    "penchant", "penury", "perennial", "perfidious", "perfunctory", "permeate",
    "pernicious", "perspicacious", "pervade", "petulant", "philistine", "phlegmatic",
    "pithy", "placate", "plethora", "ponderous", "pragmatic", "prattle", "precipitate",
    "precursor", "predilection", "prescient", "presumptuous", "prevaricate", "pristine",
    "probity", "proclivity", "prodigal", "profligate", "proliferate", "propensity",
    "proscribe", "provident", "pugnacious", "punctilious", "quaff", "quell", "quixotic",
    "quotidian", "rabid", "raconteur", "raffish", "rapprochement", "raze", "rebuttal",
    "recant", "reciprocate", "reclusive", "redoubtable", "redundant", "refute", "relegate", 
    "reparable", "rescind", "resigned", "resilient",
    "resolve", "restive", "reticent", "revere", "rife", "rigor", "ruffian", "ruse",
    "sanction", "sangfroid", "sardonic", "satiate", "savant", "scanty", "schism",
    "scintilla", "scrupulous", "seclusion", "shrewd", "sinecure", "sleight", "slovenly",
    "solicitous", "solitude", "somatic", "sophistry", "sparse", "spendthrift",
    "spurious", "squander", "staid", "stoic", "stupefy", "stymie", "succinct",
    "superficial", "surfeit", "surreptitious", "svelte", "swarthy", "tacit", "tenacity",
    "tendentious", "tenuous", "tether", "timorous", "tirade", "toady", "torpid",
    "tractable", "truculent", "tumid", "turbid", "ubiquitous", "umbrage", "uncanny",
    "unctuous", "untenable", "urbane", "vacillate", "vacuous", "variegated", "vehement",
    "veneer", "veracity", "vex", "vigilant", "vilify", "vindictive", "virulent",
    "visceral", "vituperate", "vocation", "volatile", "voracious", "wanton", "warily",
    "warrant", "wily", "wistful", "worldly", "wreak", "wrenching", "yoke", "zealot"
]


generated_words_file = "generated_words.txt"
generated_words = []

def load_generated_words():
    if os.path.exists(generated_words_file):
        with open(generated_words_file, "r") as f:
            for line in f:
                generated_words.append(line.strip())

def save_generated_words():
    with open(generated_words_file, "w") as f:
        for word in generated_words:
            f.write(word + "\n")

def generate_word():
    if len(words) == len(generated_words):
        generated_words.clear()
        
    random_word = random.choice(words)
    
    while random_word in generated_words:
        random_word = random.choice(words)
        
    generated_words.append(random_word)
    save_generated_words()
    
    return random_word

load_generated_words()

def show_words():
    message = "These are your words for today:\n"
    for i in range(10):
        message += str(i+1) + ". " + generate_word().capitalize() + "\n"
    messagebox.showinfo("Generated Words", message)

root = tk.Tk()
root.withdraw()
show_words()
root.mainloop()
