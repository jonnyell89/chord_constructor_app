from typing import List, Dict

from app.library.enums import RootType, SecondType, ThirdType, FourthType, FifthType, SixthType, SeventhType, NinthType, EleventhType, ThirteenthType

CHROMATIC_SCALE: List[str] = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

CHROMATIC_LEN: int = len(CHROMATIC_SCALE)

INTERVAL_NAMES: List[str] = ["second", "third", "fourth", "fifth", "sixth", "seventh", "ninth", "eleventh", "thirteenth"]

INTERVAL_DICT: Dict[str, int] = {
    
    "unison": 0,
    "minor_second": 1,
    "major_second": 2,
    "minor_third": 3,
    "major_third": 4,
    "perfect_fourth": 5,
    "augmented_fourth": 6,
    "diminished_fifth": 6,
    "perfect_fifth": 7,
    "augmented_fifth": 8,
    "minor_sixth": 8,
    "major_sixth": 9,
    "diminished_seventh": 9,
    "minor_seventh": 10,
    "major_seventh": 11,
    "octave": 12,
    "minor_ninth": 13,
    "major_ninth": 14,
    "minor_tenth": 15,
    "major_tenth": 16,
    "perfect_eleventh": 17,
    "augmented_eleventh": 18,
    "perfect_twelfth": 19,
    "minor_thirteenth": 20,
    "major_thirteenth": 21

    }

INTERVAL_DEPENDENCIES_DICT: Dict[str, List[str]] = {

    "thirteenth": ["seventh", "ninth", "eleventh"],
    "eleventh": ["seventh", "ninth"],
    "ninth": ["seventh"]

}

DEFAULT_INTERVAL_TYPES = {

    "root": RootType.C,
    "second": SecondType.ADD2,
    "third": ThirdType.MAJOR,
    "fourth": FourthType.ADD4,
    "fifth": FifthType.PERFECT,
    "sixth": SixthType.ADD6,
    "seventh": SeventhType.MINOR,
    "ninth": NinthType.MAJOR,
    "eleventh": EleventhType.PERFECT,
    "thirteenth": ThirteenthType.MAJOR

}
