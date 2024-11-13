import sys
from pathlib import Path

# Adds the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from typing import List, Tuple, Optional, TypeVar

from app.library.enums import RootType, SecondType, ThirdType, FourthType, FifthType, SixthType, SeventhType, NinthType, EleventhType, ThirteenthType
from config.config import CHROMATIC_SCALE, CHROMATIC_LEN, INTERVAL_NAMES, INTERVAL_DICT, INTERVAL_DEPENDENCIES_DICT, DEFAULT_INTERVAL_TYPES

class Chord:

    """
    A class to construct chords, built of a maximum of ten notes.

    The root note defines the fundamental tone of the chord, and the optional (second, third, fourth, fifth, sixth, seventh, ninth, eleventh and thirteenth) notes shape the chord's overall quality.

    A Chord class object defaults to a C Major chord; a "C" root note, a major third interval and a perfect fifth interval.

    Attributes:

        root_type (RootType): The root note of the chord; defaults to "RootType.C".
        root_note (str): The string representation of the root note.
        root_index (int): The position of the root note in the chromatic scale, represented as an index.
        root_interval (int): The root interval that all other intervals are relative to, initialised to 0.

        third_type (ThirdType): The type of third interval, including sus2, minor, major and sus4; defaults to ThirdType.MAJOR
        fifth_type (FifthType): The type of fifth interval, including diminished, perfect and augmented; defaults to FifthType.PERFECT

        second_type (Optional[SecondType]): The type of second interval, including major only for add2 chords; defaults to None.
        fourth_type (Optional[FourthType]): The type of fourth interval, including major only for add4 chords; defaults to None.
        sixth_type (Optional[SixthType]): The type of sixth interval, including major only for add6 chords; defaults to None.
        seventh_type (Optional[SeventhType]): The type of seventh interval, including diminished, minor and major; defaults to None.
        ninth_type (Optional[NinthType]): The type of ninth interval, including minor and major; defaults to None.
        eleventh_type (Optional[EleventhType]): The type of eleventh interval, including perfect and augmented; defaults to None.
        thirteenth_type (Optional[ThirteenthType]): The type of thirteenth interval, including minor and major; defaults to None.

    """

    def __init__(self):

        # Initialises the fundamental tone of the chord to the default interval type.
        self.root_type: RootType = DEFAULT_INTERVAL_TYPES.get("root")        
        # Initialises the string representation of the root note.
        self.root_note: str = self.root_type.value
        # Initialises the root note index position in the chromatic scale.
        self.root_index: int = CHROMATIC_SCALE.index(self.root_note)
        # Initialises the root interval that all other intervals are relative to.
        self.root_interval: int = 0

        # Initialises the third and fifth interval types to their default interval types.
        self.third_type: ThirdType = DEFAULT_INTERVAL_TYPES.get("third")
        self.fifth_type: FifthType = DEFAULT_INTERVAL_TYPES.get("fifth")

        # Initialises all optional interval types to None by default.
        self.second_type: Optional[SecondType] = None
        self.fourth_type: Optional[FourthType] = None
        self.sixth_type: Optional[SixthType] = None
        self.seventh_type: Optional[SeventhType] = None
        self.ninth_type: Optional[NinthType] = None
        self.eleventh_type: Optional[EleventhType] = None
        self.thirteenth_type: Optional[ThirteenthType] = None
        
        # Calculates the note and interval attributes for all interval types.
        self.initialise_notes_and_intervals()



    # Defines a generic variable Type Hint for Enum interval types used across various methods.
    IntervalType = TypeVar("IntervalType", SecondType, ThirdType, FourthType, FifthType, SixthType, SeventhType, NinthType, EleventhType, ThirteenthType) 

    def initialise_notes_and_intervals(self) -> None:

        """
        Determines if an interval type has been set for each interval name in the list of interval names.
        
        """

        for interval_name in INTERVAL_NAMES:

            # Retrieves the interval type attribute.
            interval_type = getattr(self, f"{interval_name}_type")

            # Sets the corresponding note and interval attributes, based on the interval type attribute.
            self._process_note_and_interval(interval_name, interval_type)

    def _process_note_and_interval(self, 
                                   interval_name: str, 
                                   interval_type: Optional[IntervalType]
                                   ) -> None:
        
        """
        Sets the note and interval attributes, based on the interval type attribute.

        Args:

            interval_name (str): The name of the interval type (e.g., "thirteenth").
            interval_type (Optional[IntervalType]): The interval type Enum that refers to the interval name. 
                                                    The interval name returns the value in semitones between the root note and the target note from INTERVAL_DICT.        
        
        """

        if interval_type:

            # Calculates the note and interval relative to the root note, if the interval type has been provided.
            note, interval = self.calculate_note_and_interval(interval_type)
        
        else:

            # Sets the note and interval relative to the root note to None, if the interval type has not been provided.
            note, interval = None, None

        setattr(self, f"{interval_name}_note", note)

        setattr(self, f"{interval_name}_interval", interval)



    def initialise_dependencies(self) -> None:
        
        """
        Determines if an interval type has been set that requires additional interval dependencies.
        
        """

        for interval_name, dependencies in INTERVAL_DEPENDENCIES_DICT.items():

            # Retrieves the interval type attribute.
            interval_type = getattr(self, f"{interval_name}_type")

            if interval_type:

                for dependency in dependencies:

                    # Retrieves the dependency interval type attribute.
                    interval_dependency_type = getattr(self, f"{dependency}_type")

                    # Sets the dependency interval type attribute to a default value, if the interval type has not been provided.
                    if interval_dependency_type is None:

                        default_interval_type = DEFAULT_INTERVAL_TYPES.get(dependency)
                        
                        # Sets the corresponding note and interval attributes, based on the dependency interval type attribute.
                        self._add_interval_type_and_attributes(dependency, default_interval_type)

                break

    def _add_interval_type_and_attributes(self, 
                                          interval_name: str, 
                                          interval_type: Optional[IntervalType]
                                          ) -> None:
        
        """
        Sets the interval type with its note and interval attributes.

        Args:

            interval_name (str): The name of the interval type (e.g., "thirteenth").
            interval_type (Optional[IntervalType]): The interval type Enum that refers to the interval name. 
                                                    The interval name returns the value in semitones between the root note and the target note from INTERVAL_DICT.        
        
        """

        # Calculates the note and interval relative to the root note for the corresponding interval type.
        note, interval = self.calculate_note_and_interval(interval_type)

        setattr(self, f"{interval_name}_type", interval_type)

        setattr(self, f"{interval_name}_note", note)

        setattr(self, f"{interval_name}_interval", interval)

        # Ensures that the root interval type is fully added.
        if interval_name == "root":

            setattr(self, f"{interval_name}_index", CHROMATIC_SCALE.index(self.root_note))



    def set_new_root(self, 
                     new_root_type: RootType
                     ) -> None:

        """
        Updates the root note and recalculates the note and interval attributes for all other assigned interval types.

        Sets a new root note for the chord, and recalculates all other assigned interval types, relative to the new root note.

        Args:

            new_root_type (RootType): The new root note for the chord.
        
        """

        # Initialises the fundamental tone of the chord.
        self.root_type: RootType = new_root_type
        # Initialises the string representation of the new root note.
        self.root_note: str = self.root_type.value
        # Initialises the new root index position in the chromatic scale.
        self.root_index: int = CHROMATIC_SCALE.index(self.root_note)

        # Calculates the note and interval attributes for all interval types provided.
        self.initialise_notes_and_intervals()



    def calculate_note_and_interval(self, 
                                    interval_type: Optional[IntervalType]
                                    ) -> Tuple[str, int]:
        
        """
        Calculates and returns the note and interval relative to the root note for all interval types.

        Args:

            interval_type (Optional[IntervalType]): The interval type Enum that refers to the interval name. 
                                                    The interval name returns the value in semitones between the root note and the target note from INTERVAL_DICT.
                                                    If the interval type Enum is RootType, the value refers directly to the note and the value in semitones is directly accessed from INTERVAL_DICT.
        
        Returns:

            str: The note in the chromatic scale that corresponds to the root note index position and the interval type.
            int: The interval in the chromatic scale that corresponds to the root note index position and the note.
        
        """

        if interval_type.__class__ == RootType:

            # Retrieves the interval as a value in semitones between the root note and the target note.
            interval: int = INTERVAL_DICT["unison"]

            # Accesses the string representation from the RootType value directly.
            note: str = interval_type.value
        
        else:

            # Retrieves the interval as a value in semitones between the root note and the target note.
            interval: int = INTERVAL_DICT[interval_type.value]

            # Calculates the string representation of the interval.
            note: str = CHROMATIC_SCALE[(self.root_index + interval) % CHROMATIC_LEN]

        return note, interval
    


    def add_or_remove_interval_type_and_attributes(self, 
                                                   interval_type: Optional[IntervalType]
                                                   ) -> None:
        
        """
        Adds or removes interval types from the chord.

        If the interval type is already present, it is removed along with its note and interval attributes.
        
        If the interval type is not present, it is added along with its note and interval attributes.

            When an interval type is added to the chord, a check is run on its possible interval type dependencies.
        
        Args:

            interval_type (Optional[IntervalType]): The interval type Enum to be added or removed.
        
        """

        valid_enum_types = (RootType, SecondType, ThirdType, FourthType, FifthType, SixthType, SeventhType, NinthType, EleventhType, ThirteenthType)

        if not isinstance(interval_type, valid_enum_types):

            raise ValueError(f"Invalid interval_type: {interval_type} must be an instance of a valid Enum type.")
        


        interval_name = self._extract_name_from_type(interval_type)

        if interval_type == getattr(self, f"{interval_name}_type"):

            # Removes the interval type and its note and interval attributes, if the interval type is already present in the chord.
            self._remove_interval_type_and_attributes(interval_name)

        else:

            # Adds the interval type and its note and interval attributes, if the interval type is not already present in the chord.
            self._add_interval_type_and_attributes(interval_name, interval_type)

            # Calculates the note and interval attributes for all interval types dependencies that are currently set to None values.
            self.initialise_dependencies()

    def _remove_interval_type_and_attributes(self, 
                                             interval_name: str
                                             ) -> None:
        
        """
        Sets the interval type, note and interval attributes to None values.

        Args:

            interval_name (str): The name of the interval type (e.g., "thirteenth").
        
        """

        setattr(self, f"{interval_name}_type", None)
        setattr(self, f"{interval_name}_note", None)
        setattr(self, f"{interval_name}_interval", None)

        # Ensures that the root interval type is fully removed.
        if interval_name == "root":

            setattr(self, f"{interval_name}_index", None)



    def get_note_signature(self) -> List[str]:

        """
        Generates a list of string representations for all notes in the chord.

        Aggregates the note attributes for all assigned interval types, ordered relative to the root note in the chromatic scale.

        Returns:

            List[str]: An ordered list containing the note attributes for all assigned interval types, with any None values removed.

        """

        # Stores all note attributes from the chord, including None values.
        note_signature = [
            
            self.root_note, 
            self.second_note, 
            self.third_note, 
            self.fourth_note, 
            self.fifth_note, 
            self.sixth_note, 
            self.seventh_note, 
            self.ninth_note, 
            self.eleventh_note, 
            self.thirteenth_note
            
            ]

        # Returns an ordered list comprehension containing the notes from the chord, with any None values removed.
        return [note for note in note_signature if note is not None]

    def get_interval_signature(self) -> List[int]:

        """
        Generates a list of intervals for all notes in the chord.

        Aggregates the interval attributes for all assigned interval types, ordered relative to the root note in the chromatic scale.
        
        Returns:

            List[int]: An ordered list containing the interval attributes for all assigned interval types, with any None values removed.

        """

        interval_signature = [

            self.root_interval,
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
        
        # Returns an ordered list comprehension containing the intervals from the chord, with any None values removed.
        return [interval for interval in interval_signature if interval is not None]



    def _extract_name_from_type(self, 
                                interval_type: Optional[IntervalType]
                                ) -> str:
        
        """
        Extracts and formats the interval name from the interval type (e.g., ThirteenthType -> "thirteenth").

        Args:

            interval_type (Optional[IntervalType]): The interval type Enum to have its interval name extracted and formatted.

        Returns:

            str: The name of the interval type, reformatted as a lowercase string (e.g., "thirteenth").
                    
        """

        interval_name: str = interval_type.__class__.__name__.lower().replace("type", "")

        return interval_name



if __name__ == "__main__":

    print("--------------------")

    chord = Chord()

    print(f"With object root: {chord.root_note}")

    print(f"With object third: {chord.third_note}")

    print(f"With object fifth: {chord.fifth_note}")

    print(f"With object seventh: {chord.seventh_note}")

    print(f"With object ninth: {chord.ninth_note}")

    print(f"With object eleventh: {chord.eleventh_note}")

    print(f"With object thirteenth: {chord.thirteenth_note}")

    print(f"With object note signature: {chord.get_note_signature()}")

    print(f"With object index signature: {chord.get_interval_signature()}")

    print("--------------------")

    chord.set_new_root(new_root_type=RootType.G)

    chord.add_or_remove_interval_type_and_attributes(interval_type=ThirteenthType.MAJOR)

    print(f"With object root: {chord.root_note}")

    print(f"With object third: {chord.third_note}")

    print(f"With object fifth: {chord.fifth_note}")

    print(f"With object seventh: {chord.seventh_note}")

    print(f"With object ninth: {chord.ninth_note}")

    print(f"With object eleventh: {chord.eleventh_note}")

    print(f"With object thirteenth: {chord.thirteenth_note}")

    print(f"With object note signature: {chord.get_note_signature()}")

    print(f"With object index signature: {chord.get_interval_signature()}")

    print("--------------------")

    chord.add_or_remove_interval_type_and_attributes(interval_type=ThirteenthType.MAJOR)

    print(f"With object root: {chord.root_note}")

    print(f"With object third: {chord.third_note}")

    print(f"With object fifth: {chord.fifth_note}")

    print(f"With object seventh: {chord.seventh_note}")

    print(f"With object ninth: {chord.ninth_note}")

    print(f"With object eleventh: {chord.eleventh_note}")

    print(f"With object thirteenth: {chord.thirteenth_note}")

    print(f"With object note signature: {chord.get_note_signature()}")

    print(f"With object index signature: {chord.get_interval_signature()}")

    print("--------------------")
