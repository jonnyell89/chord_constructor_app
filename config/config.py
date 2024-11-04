from typing import List

CHROMATIC_SCALE: List[str] = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

INTERVALS: List[str] = ["R", "b2", "2", "3m", "3M", "4", "b5", "5", "#5", "6", "7m", "7M", "8", "b9", "9", "#9", "b11", "11", "#11", "12", "b13", "13", "#13"]

INTERVALS_DICT = {
    
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
