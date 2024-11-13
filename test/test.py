import pytest

from app.chord import Chord
from app.library.enums import RootType, ThirdType, FifthType, SeventhType, NinthType, EleventhType, ThirteenthType
from config.config import CHROMATIC_SCALE, CHROMATIC_LEN, INTERVAL_NAMES, INTERVAL_DICT, INTERVAL_DEPENDENCIES_DICT, DEFAULT_INTERVAL_TYPES


def test_chord_instantiation():

    """
    A Chord class object defaults to a 'C Major' chord.

    All other optional intervals default to None values.
    
    """

    chord = Chord()

    assert chord.root_type == RootType.C
    assert chord.root_note == "C"
    assert chord.root_index == 0
    assert chord.root_interval == 0

    assert chord.third_type == ThirdType.MAJOR
    assert chord.third_note == "E"
    assert chord.third_interval == 4

    assert chord.fifth_type == FifthType.PERFECT
    assert chord.fifth_note == "G"
    assert chord.fifth_interval == 7

    attributes_set_to_none = [

        "second_type", "second_note", "second_interval",
        "fourth_type", "fourth_note", "fourth_interval",
        "sixth_type", "sixth_note", "sixth_interval",
        "seventh_type", "seventh_note", "seventh_interval",
        "ninth_type", "ninth_note", "ninth_interval",
        "eleventh_type", "eleventh_note", "eleventh_interval",
        "thirteenth_type", "thirteenth_note", "thirteenth_interval"

    ]

    assert all(getattr(chord, attribute) is None for attribute in attributes_set_to_none)



def test_set_new_root():

    chord = Chord()

    chord.set_new_root(RootType.G)

    assert chord.root_type == RootType.G
    assert chord.root_note == "G"
    assert chord.root_index == 7
    assert chord.root_interval == 0

    assert chord.third_type == ThirdType.MAJOR
    assert chord.third_note == "B"
    assert chord.third_interval == 4

    assert chord.fifth_type == FifthType.PERFECT
    assert chord.fifth_note == "D"
    assert chord.fifth_interval == 7

    attributes_set_to_none = [

        "second_type", "second_note", "second_interval",
        "fourth_type", "fourth_note", "fourth_interval",
        "sixth_type", "sixth_note", "sixth_interval",
        "seventh_type", "seventh_note", "seventh_interval",
        "ninth_type", "ninth_note", "ninth_interval",
        "eleventh_type", "eleventh_note", "eleventh_interval",
        "thirteenth_type", "thirteenth_note", "thirteenth_interval"

    ]

    assert all(getattr(chord, attribute) is None for attribute in attributes_set_to_none)



def test_add_or_remove_interval_type_and_attributes_none():

    chord = Chord()

    with pytest.raises(ValueError, match=r"Invalid interval_type: None must be an instance of a valid Enum type."):
        
        chord.add_or_remove_interval_type_and_attributes(None)



def test_add_or_remove_interval_type_and_attributes():

    chord = Chord()

    chord.add_or_remove_interval_type_and_attributes(SeventhType.MINOR)

    assert chord.root_type == RootType.C
    assert chord.root_note == "C"
    assert chord.root_index == 0
    assert chord.root_interval == 0

    assert chord.third_type == ThirdType.MAJOR
    assert chord.third_note == "E"
    assert chord.third_interval == 4

    assert chord.fifth_type == FifthType.PERFECT
    assert chord.fifth_note == "G"
    assert chord.fifth_interval == 7

    assert chord.seventh_type == SeventhType.MINOR
    assert chord.seventh_note == "Bb"
    assert chord.seventh_interval == 10

    attributes_set_to_none = [

        "second_type", "second_note", "second_interval",
        "fourth_type", "fourth_note", "fourth_interval",
        "sixth_type", "sixth_note", "sixth_interval",
        "ninth_type", "ninth_note", "ninth_interval",
        "eleventh_type", "eleventh_note", "eleventh_interval",
        "thirteenth_type", "thirteenth_note", "thirteenth_interval"

    ]

    assert all(getattr(chord, attribute) is None for attribute in attributes_set_to_none)



def test_all_interval_types_and_attributes_removed():

    chord = Chord()

    chord.add_or_remove_interval_type_and_attributes(RootType.C)
    chord.add_or_remove_interval_type_and_attributes(ThirdType.MAJOR)
    chord.add_or_remove_interval_type_and_attributes(FifthType.PERFECT)

    attributes_set_to_none = [

        "root_type", "root_note", "root_index", "root_interval",
        "second_type", "second_note", "second_interval",
        "fourth_type", "fourth_note", "fourth_interval",
        "sixth_type", "sixth_note", "sixth_interval",
        "seventh_type", "seventh_note", "sixth_interval",
        "ninth_type", "ninth_note", "ninth_interval",
        "eleventh_type", "eleventh_note", "eleventh_interval",
        "thirteenth_type", "thirteenth_note", "thirteenth_interval"

    ]

    assert all(getattr(chord, attribute) is None for attribute in attributes_set_to_none)



def test_all_default_interval_types_and_attributes_added():

    chord = Chord()

    chord.add_or_remove_interval_type_and_attributes(RootType.C)
    chord.add_or_remove_interval_type_and_attributes(ThirdType.MAJOR)
    chord.add_or_remove_interval_type_and_attributes(FifthType.PERFECT)

    for default_interval_name, default_interval_type in DEFAULT_INTERVAL_TYPES.items():

        chord.add_or_remove_interval_type_and_attributes(default_interval_type)

        assert getattr(chord, f"{default_interval_name}_type") == default_interval_type



"""

def test_chord_instantiation_with_custom_intervals():

    # Instantiates a chord with custom intervals.
    chord = Chord(root_type=RootType.D,
                  third_type=ThirdType.MINOR,
                  fifth_type=FifthType.DIMINISHED,
                  seventh_type=SeventhType.DIMINISHED,
                  #ninth_type=NinthType.MINOR,
                  eleventh_type=EleventhType.PERFECT)
    
    # Checks the root note is correctly assigned.
    assert chord.root_note == "D"

    # Checks the custom third interval and custom fifth interval are correctly assigned.
    assert chord.third_type == ThirdType.MINOR
    assert chord.fifth_type == FifthType.DIMINISHED

    # Checks the custom seventh, ninth and eleventh intervals are correctly assigned.
    assert chord.seventh_type == SeventhType.DIMINISHED
    #assert chord.ninth_type == NinthType.MINOR
    assert chord.eleventh_type == EleventhType.PERFECT

    # Checks if the remaining optional interval is correctly set to None by default.
    assert chord.ninth_type == None
    assert chord.thirteenth_type == None

def test_chord_instantiation_with_thirteenth_interval():

    # Instantiates a chord with a custom root note and custom thirteenth interval only.
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

    # Instantiates a chord based on custom intervals.
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

"""
