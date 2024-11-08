import sys
from pathlib import Path

# Adds the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from typing import List, Dict, Optional, Callable

from app.utils import calculate_note, calculate_interval
from app.library.enums import RootType, SecondType, ThirdType, FourthType, FifthType, SixthType, SeventhType, NinthType, EleventhType, ThirteenthType, ExtensionType, AddType
from config.config import CHROMATIC_SCALE, INTERVAL_NAMES, INTERVAL_DICT, INTERVAL_DEPENDENCIES_DICT, DEFAULT_INTERVAL_TYPES

class Chord:

    """
    A class to construct chords, built of a maximum of ten notes.

    The root note defines the fundamental tone of the chord, and the optional second, third, fourth, fifth, sixth, seventh, ninth, eleventh and thirteenth notes shape the chord's overall quality.

    If only a root note is provided, the third note defaults to major, and the fifth note defaults to perfect.

    Attributes:

        root_type (RootType): The root note of the chord.
        root_note (str): The string representation of the root note.
        root_index (int): The index position of the root note in the chromatic scale.

        third_type (ThirdType): The type of third interval, including sus2, minor, major and sus4.
        third_note (str): The string representation of the third note.

        fifth_type (FifthType): The type of fifth interval, including diminished, perfect and augmented.
        fifth_note (str): The string representation of the fifth note.

        seventh_type (Optional[SeventhType]): The type of seventh interval, including diminished, minor and major.
        seventh_note (Optional[str]): The string representation of the seventh note.

        ninth_type (Optional[NinthType]): The type of ninth interval, including minor and major.
        ninth_note (Optional[str]): The string representation of the ninth note.

        eleventh_type (Optional[EleventhType]): The type of eleventh interval, including perfect and augmented.
        eleventh_note (Optional[str]): The string representation of the eleventh note.

        thirteenth_type (Optional[ThirteenthType]): The type of thirteenth interval, including minor and major.
        thirteenth_note (Optional[str]): The string representation of the thirteenth note.

    Args:

        root_type (RootType): The root note of the chord.
        third_type (Optional[ThirdType]): The type of third interval, defaults to "ThirdType.MAJOR".
        fifth_type (Optional[FifthType]): The type of fifth interval, defaults to "FifthType.PERFECT".
        seventh_type (Optional[SeventhType]): The type of seventh interval, defaults to None or "SeventhType.MINOR".
        ninth_type (Optional[NinthType]): The type of ninth interval, defaults to None or "NinthType.MAJOR".
        eleventh_type (Optional[EleventhType]): The type of eleventh interval, defaults to None or "EleventhType.PERFECT".
        thirteenth_type (Optional[ThirteenthType]): The type of thirteenth interval, defaults to None or "ThirteenthType.MAJOR".
    
    """

    def __init__(self, 
                 root_type: RootType = None,
                 second_type: SecondType = None, 
                 third_type: ThirdType = None,
                 fourth_type: FourthType = None,
                 fifth_type: FifthType = None,
                 sixth_type: SixthType = None,
                 seventh_type: SeventhType = None,
                 ninth_type: NinthType = None,
                 eleventh_type: EleventhType = None,
                 thirteenth_type: ThirteenthType = None,
                 ):

        # Initialises the fundamental tone of the chord, according to the user input or the default interval type.
        self.root_type: RootType = root_type if root_type is not None else DEFAULT_INTERVAL_TYPES.get("root")        
        # Initialises the string representation of the root note.
        self.root_note: str = self.root_type.value
        # Initialises the root index, essential to all calculation operations.
        self.root_index: int = CHROMATIC_SCALE.index(self.root_note)

        # Initialises the third and fifth interval types, according to the user input or the default interval type.
        self.third_type: ThirdType = third_type if third_type is not None else DEFAULT_INTERVAL_TYPES.get("third")
        self.fifth_type: FifthType = fifth_type if fifth_type is not None else DEFAULT_INTERVAL_TYPES.get("fifth")

        # Initialises any optional interval types.
        self.second_type: Optional[SecondType] = second_type
        self.fourth_type: Optional[FourthType] = fourth_type
        self.sixth_type: Optional[SixthType] = sixth_type
        self.seventh_type: Optional[SeventhType] = seventh_type
        self.ninth_type: Optional[NinthType] = ninth_type
        self.eleventh_type: Optional[EleventhType] = eleventh_type
        self.thirteenth_type: Optional[ThirteenthType] = thirteenth_type
        
        self.set_intervals(INTERVAL_NAMES, self._process_interval)

        self.set_interval_dependencies(INTERVAL_DEPENDENCIES_DICT)



    def set_intervals(self, interval_names: List[str], action: Callable):

        for interval_name in interval_names:

            interval_type = getattr(self, f"{interval_name}_type")

            action(interval_name, interval_type)

    def _process_interval(self, interval_name, interval_type):

        if interval_type:

            # Calculates the default note, relative to the root note.
            note: str = calculate_note(CHROMATIC_SCALE, self.root_index, INTERVAL_DICT.get(interval_type.value))
            
            # Calculates the default interval, relative to the root note.
            interval: int = calculate_interval(CHROMATIC_SCALE, self.root_index, note)
        
        else:

            note, interval = None, None

        # Sets the default note as an instance variable.
        setattr(self, f"{interval_name}_note", note)

        # Sets the default note as an instance variable.
        setattr(self, f"{interval_name}_interval", interval)



    def set_interval_dependencies(self, interval_dependencies: Dict[str, List[str]]):

        for interval_name, intervals in interval_dependencies.items():

            interval_type = getattr(self, f"{interval_name}_type")

            if interval_type:

                for interval in intervals:

                    interval_dependency_type = getattr(self, f"{interval}_type")

                    if interval_dependency_type is None:

                        default_interval_type = DEFAULT_INTERVAL_TYPES.get(interval)

                        setattr(self, f"{interval}_type", default_interval_type)
                        
                        self._process_interval_dependencies(interval, default_interval_type)

                break

    def _process_interval_dependencies(self, interval_name, interval_type):

        # Calculates the default note, relative to the root note.
        note: str = calculate_note(CHROMATIC_SCALE, self.root_index, INTERVAL_DICT.get(interval_type.value))
        
        # Sets the default note as an instance variable.
        setattr(self, f"{interval_name}_note", note)

        # Calculates the default interval, relative to the root note.
        interval: int = calculate_interval(CHROMATIC_SCALE, self.root_index, note)

        # Sets the default note as an instance variable.
        setattr(self, f"{interval_name}_interval", interval)



if __name__ == "__main__":

    demo = Chord(root_type=RootType.G, thirteenth_type=ThirteenthType.MAJOR)

    print(f"Demo object root: {demo.root_type}")

    print(f"Demo object third: {demo.third_type}")

    print(f"Demo object fifth: {demo.fifth_type}")

    print(f"Demo object seventh: {demo.seventh_type}")

    print(f"Demo object ninth: {demo.ninth_type}")

    print(f"Demo object eleventh: {demo.eleventh_type}")

    print(f"Demo object thirteenth: {demo.thirteenth_type}")

    print(dir(demo))
