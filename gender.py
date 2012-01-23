import re

class AmbiguousGenderException(Exception):pass
class UnknownGenderException(Exception):pass

def make_find_word_fcn(word):
    return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

male_identifiers = ("he", "his", "mr")
male_fcns = [make_find_word_fcn(ident) for ident in male_identifiers]

female_identifiers = ("she", "her", "ms", "mrs")
female_fcns = [make_find_word_fcn(ident) for ident in female_identifiers]

def is_male(text):
    return filter(lambda f:f(text), male_fcns)

def is_female(text):
    return filter(lambda f:f(text), female_fcns)

def get_gender(text):
    gender = None
    if is_male(text):
        gender = "male"

    if is_female(text):
        if not gender:
            gender = "female"
        else:
            raise AmbiguousGenderException

    if not gender:
        raise UnknownGenderException

    return gender

def classify(speakers):
    male = []
    female = []
    ambig = []
    unknown = []
    for s in speakers:
        try:
            g = get_gender(s.bio)
            print s.name, "is", g
            s.gender = g
            if g == "male":
                male.append(s)
            elif g == "female":
                female.append(s)
        except AmbiguousGenderException:
            ambig.append(s)
        except UnknownGenderException:
            unknown.append(s)
    return male, female, ambig, unknown

