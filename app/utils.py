from typing import List

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
