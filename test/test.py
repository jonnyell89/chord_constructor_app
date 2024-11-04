import pytest

from app.chord import Chord
from app.utils import calculate_note, calculate_interval
from app.library.enums import RootType, ThirdType, FifthType, SeventhType, NinthType, EleventhType, ThirteenthType, ExtensionType, AddType
from config.config import CHROMATIC_SCALE, INTERVALS_DICT

def test_chord_instantiation_with_default_values():

    # Instantiates a chord based on the root note.
    chord = Chord(root_type=RootType.C)

    # Checks the root note is correctly assigned.
    assert chord.root_note == "C"

    # Checks the third interval and fifth interval are correctly assigned by default.
    assert chord.third_type == ThirdType.MAJOR
    assert chord.fifth_type == FifthType.PERFECT

    # Checks if the optional intervals are correctly set to None
    assert chord.seventh_type == None
    assert chord.ninth_type == None
    assert chord.eleventh_type == None
    assert chord.thirteenth_type == None

def test_chord_instantiation_with_custom_intervals():

    # Instantiates a chord based on the custom intervals.
    chord = Chord(root_type=RootType.D,
                  third_type=ThirdType.MINOR,
                  fifth_type=FifthType.DIMINISHED,
                  seventh_type=SeventhType.DIMINISHED,
                  ninth_type=NinthType.MINOR,
                  eleventh_type=EleventhType.PERFECT)
    
    # Checks the root note is correctly assigned.
    assert chord.root_note == "D"

    # Checks the custom third interval and custom fifth interval are correctly assigned.
    assert chord.third_type == ThirdType.MINOR
    assert chord.fifth_type == FifthType.DIMINISHED

    # Checks the custom seventh, ninth and eleventh intervals are correctly assigned.
    assert chord.seventh_type == SeventhType.DIMINISHED
    assert chord.ninth_type == NinthType.MINOR
    assert chord.eleventh_type == EleventhType.PERFECT

    # Checks if the remaining optional interval is correctly set to None
    assert chord.thirteenth_type == None

def test_chord_instantiation_with_thirteenth_interval():

    # Instantiates a chord based on the custom intervals.
    chord = Chord(root_type=RootType.F,
                  thirteenth_type=ThirteenthType.MINOR)
    
    # Checks the root note is correctly assigned.
    assert chord.root_note == "F"

    # Checks the third interval and fifth interval are correctly assigned by default.
    assert chord.third_type == ThirdType.MAJOR
    assert chord.fifth_type == FifthType.PERFECT

    # Checks the optional seventh, ninth and eleventh intervals are correctly assigned by default.
    assert chord.seventh_type == SeventhType.MINOR
    assert chord.ninth_type == NinthType.MAJOR
    assert chord.eleventh_type == EleventhType.PERFECT

    # Checks the custom thirteenth interval is correctly assigned.
    assert chord.thirteenth_type == ThirteenthType.MINOR

def test_chord_instantiation_with_all_intervals():

    # Instantiates a chord based on the custom intervals.
    chord = Chord(root_type=RootType.G,
                  third_type=ThirdType.MAJOR,
                  fifth_type=FifthType.AUGMENTED,
                  seventh_type=SeventhType.MAJOR,
                  ninth_type=NinthType.MAJOR,
                  eleventh_type=EleventhType.AUGMENTED,
                  thirteenth_type=ThirteenthType.MAJOR)
    
    # Checks the root note is correctly assigned.
    assert chord.root_note == "G"

    # Checks the third interval and fifth interval are correctly assigned.
    assert chord.third_type == ThirdType.MAJOR
    assert chord.fifth_type == FifthType.AUGMENTED

    # Checks the custom seventh, ninth, eleventh and thirteenth intervals are correctly assigned.
    assert chord.seventh_type == SeventhType.MAJOR
    assert chord.ninth_type == NinthType.MAJOR
    assert chord.eleventh_type == EleventhType.AUGMENTED
    assert chord.thirteenth_type == ThirteenthType.MAJOR
