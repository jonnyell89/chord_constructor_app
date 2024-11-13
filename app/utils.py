from typing import List

from config.config import CHROMATIC_SCALE

def calculate_note(chromatic_scale: List[str], root_index: int, interval_type: object) -> str:

    """
    Calculates the note in the chromatic scale based on the root note index position and the interval type.

    Args:

        chromatic_scale (List[str]): A list of strings representing the twelve note chromatic scale.
        root_index (int): The index position of the root note in the chromatic scale.
        interval_type (object): The interval type Enum that refers to the value in semitones between the root note and the target note.

    Returns:

        str: The note in the chromatic scale that corresponds to the root note index position and the interval type.
    
    """
    
    return chromatic_scale[(root_index + interval_type) % len(chromatic_scale)]

def calculate_interval(chromatic_scale: List[str], root_index: int, note_type: str) -> int:

    """
    Calculates the interval in the chromatic scale based on the root note index position and the note type.

    Args:

        chromatic_scale (List[str]): A list of strings representing the twelve note chromatic scale.
        root_index (int): The index position of the root note in the chromatic scale.
        note_type (str): The target note from the chromatic scale. 

    Returns:

        int: The interval in the chromatic scale that corresponds to the root note index position and the note type.
    
    """

    return (chromatic_scale.index(note_type) - root_index) % len(chromatic_scale)

def interval_signature(self) -> List[int]:

    """
    Generates a list of the chord intervals.

    This method constructs the chord interval signature by aggregating the interval values of all notes in the chord that have been assigned values.
    The chord interval signature is ordered with each value relative to the root note in the chromatic scale.
    
    Returns:

        List[int]: An ordered list containing the interval values of the chord notes, starting from the root note (0).

    """

    # Stores the root note interval.
    interval_signature = [0]

    all_intervals = [

        self.second_interval, 
        self.third_interval,
        self.fourth_interval,
        self.fifth_interval, 
        self.sixth_interval, 
        self.seventh_interval, 
        self.ninth_interval, 
        self.eleventh_interval, 
        self.thirteenth_interval
        
        ]
    
    # Calculates the length of the chromatic scale.
    chromatic_len: int = len(CHROMATIC_SCALE)

    for interval in all_intervals:

        if interval:

            # Ensures the interval values of the optional notes in the chord remain in sequence, relative to the root note.
            while interval <= interval_signature[-1]:

                interval += chromatic_len

            interval_signature.append(interval)

    return interval_signature
