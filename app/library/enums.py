from enum import Enum

class RootType(Enum):

    C = "C"
    C_SHARP = "C#"
    D_FLAT = C_SHARP
    D = "D"
    E_FLAT = "Eb"
    D_SHARP = E_FLAT
    E = "E"
    F = "F"
    F_SHARP = "F#"
    G_FLAT = F_SHARP
    G = "G"
    A_FLAT = "Ab"
    G_SHARP = A_FLAT
    A = "A"
    B_Flat = "Bb"
    A_SHARP = B_Flat
    B = "B"

class SecondType(Enum):

    ADD2 = "major_second"

class ThirdType(Enum):

    SUS2 = "major_second"
    MINOR = "minor_third"
    MAJOR = "major_third"
    SUS4 = "perfect_fourth"

class FourthType(Enum):

    ADD4 = "perfect_fourth"

class FifthType(Enum):

    DIMINISHED = "diminished_fifth"
    PERFECT = "perfect_fifth"
    AUGMENTED = "augmented_fifth"

class SixthType(Enum):

    ADD6 = "major_sixth"

class SeventhType(Enum):

    DIMINISHED = "diminished_seventh"
    MINOR = "minor_seventh"
    MAJOR = "major_seventh"

class NinthType(Enum):

    MINOR = "minor_ninth"
    MAJOR = "major_ninth"
    ADD9 = "major_ninth"

class EleventhType(Enum):

    PERFECT = "perfect_eleventh"
    AUGMENTED = "augmented_eleventh"
    ADD11 = "perfect_eleventh"

class ThirteenthType(Enum):

    MINOR = "minor_thirteenth"
    MAJOR = "major_thirteenth"
    ADD13 = "major_thirteenth"

class ExtensionType(Enum):

    ROOT = "root"
    THIRD = "third"
    FIFTH = "fifth"
    SEVENTH = "seventh"
    NINTH = "ninth"
    ELEVENTH = "eleventh"
    THIRTEENTH = "thirteenth"

class AddType(Enum):

    ADD2 = "major_second"
    ADD4 = "perfect_fourth"
    ADD6 = "major_sixth"
    ADD9 = "major_ninth"
    ADD11 = "perfect_eleventh"
    ADD13 = "major_thirteenth"
