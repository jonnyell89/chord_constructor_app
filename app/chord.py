from typing import List, Optional

from app.utils import calculate_note, calculate_interval
from app.library.enums import RootType, SecondType, ThirdType, FourthType, FifthType, SixthType, SeventhType, NinthType, EleventhType, ThirteenthType, ExtensionType, AddType
from config.config import CHROMATIC_SCALE, INTERVALS_DICT

class Chord:

    """
    A class to construct chords, built of up to seven notes.

    The root note defines the fundamental tone of the chord, and the optional third, fifth, seventh, ninth, eleventh and thirteenth notes shape the chord's overall quality.

    If only a root note is provided, the third note defaults to major, and the fifth note defaults to perfect.

    Attributes:

        root_type (RootType): The root note of the chord.
        root_note (str): The string representation of the root note.
        _root_index (int): The index position of the root note in the chromatic scale.

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
                 root_type: RootType, 
                 third_type: ThirdType = None,
                 fifth_type: FifthType = None,
                 seventh_type: SeventhType = None,
                 ninth_type: NinthType = None,
                 eleventh_type: EleventhType = None,
                 thirteenth_type: ThirteenthType = None
                 ):

        # Initialises the fundamental tone of the chord
        self.root_type: RootType = root_type
        # Initialises the string representation of the root note
        self.root_note: str = self.root_type.value
        # Initialises the root index, essential to all calculate_note operations.
        self._root_index: int = CHROMATIC_SCALE.index(self.root_note)

        # Initialises the third interval type, defaulting to major if not provided.
        self.third_type: ThirdType = third_type or ThirdType.MAJOR
        # Calculates the third note, relative to the root note.
        self.third_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.third_type.value])
        # Calculates the interval value of the third note in the chord, relative to the root note.
        self.third_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.third_note)

        # Initialises the fifth interval type, defaulting to perfect if not provided.
        self.fifth_type: FifthType = fifth_type or FifthType.PERFECT
        # Calculates the fifth note, relative to the root note.
        self.fifth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.fifth_type.value])
        # Calculates the interval value of the fifth note in the chord, relative to the root note.
        self.fifth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.fifth_note)

        # Initialises optional interval types to None
        self.second_type: Optional[SecondType] = None
        self.fourth_type: Optional[FourthType] = None
        self.sixth_type: Optional[SixthType] = None
        self.seventh_type: Optional[SeventhType] = None
        self.ninth_type: Optional[NinthType] = None
        self.eleventh_type: Optional[EleventhType] = None
        self.thirteenth_type: Optional[ThirteenthType] = None

        # Initialises optional notes to None
        self.second_note: Optional[str] = None
        self.fourth_note: Optional[str] = None
        self.sixth_note: Optional[str] = None
        self.seventh_note: Optional[str] = None
        self.ninth_note: Optional[str] = None
        self.eleventh_note: Optional[str] = None
        self.thirteenth_note: Optional[str] = None

        # Initialises optional interval values to None
        self.second_interval: Optional[int] = None
        self.fourth_interval: Optional[int] = None
        self.sixth_interval: Optional[int] = None
        self.seventh_interval: Optional[int] = None
        self.ninth_interval: Optional[int] = None
        self.eleventh_interval: Optional[int] = None
        self.thirteenth_interval: Optional[int] = None

        """
        This if statement block ensures that, if any of the seventh, ninth, eleventh or thirteenth interval types are provided, all preceding optional interval types and interval values are initialised in sequence.

        """

        if seventh_type or ninth_type or eleventh_type or thirteenth_type:

            self.seventh_type: SeventhType = seventh_type or SeventhType.MINOR
            self.seventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.seventh_type.value])
            self.seventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.seventh_note)

        if ninth_type or eleventh_type or thirteenth_type:

            self.ninth_type: NinthType = ninth_type or NinthType.MAJOR
            self.ninth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.ninth_type.value])
            self.ninth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.ninth_note)

        if eleventh_type or thirteenth_type:

            self.eleventh_type: EleventhType = eleventh_type or EleventhType.PERFECT
            self.eleventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.eleventh_type.value])
            self.eleventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.eleventh_note)

        if thirteenth_type:

            self.thirteenth_type: ThirteenthType = thirteenth_type or ThirteenthType.MAJOR
            self.thirteenth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.thirteenth_type.value])
            self.thirteenth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.thirteenth_note)



    def note_signature(self) -> List[str]:

        """
        Generates a list of the chord note string representations.

        This method constructs the chord note signature by aggregating the string representations of all notes in the chord that have been assigned values. 
        The chord note signature is ordered with each value relative to the root note in the chromatic scale.
                
        Returns:

            List[str]: An ordered list containing the string representations of the chord notes, starting from the root note.

        """

        # Stores all available notes from the chord, including None values.
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
        return [note for note in note_signature if note]

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

    def set_root(self, new_root_type: RootType):

        """
        Re-initialises the class constructor according to the new root note.

        This method sets a new root note of the chord, and recalculates the third note, fifth note, and any optional notes, relative to the new root note.

        Args:

            new_root_type (RootType): The new root note of the chord.
        
        """

        # Initialises the fundamental tone of the chord
        self.root_type: RootType = new_root_type
        # Initialises the string representation of the new root note
        self.root_note: str = self.root_type.value
        # Initialises the new root index, essential to all calculate_note operations.
        self._root_index: int = CHROMATIC_SCALE.index(self.root_note)

        # Calculates and directly sets the third note, relative to the new root note.
        self.third_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.third_type.value])

        # Calculates the directly sets the fifth note, relative to the new root note.
        self.fifth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.fifth_type.value])

        # Stores the prefixes for each extension instance variable
        optional_extensions = ["second", "fourth", "sixth", "seventh", "ninth", "eleventh", "thirteenth"]

        for extension in optional_extensions:

            # Accesses self.second_type, self.fourth_type, self.sixth_type, self.seventh_type, self.ninth_type, self.eleventh_type, self.thirteenth_type.
            note_type = getattr(self, f"{extension}_type")

            if note_type:

                self._update_extension(extension=extension, note_type=note_type)

    def _update_extension(self, extension: str, note_type):

        # Calculates the updated extension note, relative to the new root note.
        updated_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[note_type.value])
        
        # Sets the updated extension note instance variable.
        setattr(self, f"{extension}_note", updated_note)

        # Calculates the updated extension interval, relative to the new root note.
        updated_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, updated_note)
        
        # Sets the updated extension note instance variable.
        setattr(self, f"{extension}_interval", updated_interval)

    def set_third(self, new_third_type: ThirdType):

        """
        Updates the instance variable specific to the third note in the chord.

        This method sets a new third note of the chord.

        Args:

            new_third_type (ThirdType): The new third note of the chord.
        
        """

        self.third_type: ThirdType = new_third_type
        self.third_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.third_type.value])
        self.third_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.third_note)

    def set_fifth(self, new_fifth_type: FifthType):

        """
        Updates the instance variable specific to the fifth note in the chord.

        This method sets a new fifth note of the chord.

        Args:

            new_fifth_type (FifthType): The new fifth note of the chord.
        
        """

        self.fifth_type: FifthType = new_fifth_type
        self.fifth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.fifth_type.value])
        self.fifth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.fifth_note)

    def set_seventh(self, new_seventh_type: Optional[SeventhType] = None):
        
        """
        Updates the instance variable specific to the seventh note in the chord.

        This method either sets a new seventh note of the chord, or removes the seventh note from the chord entirely.

        Args:

            new_seventh_type (SeventhType): The new seventh note of the chord.
        
        """

        # Sets the type instance variable.
        self.seventh_type: SeventhType = new_seventh_type

        if new_seventh_type:

            # Sets the note and interval instance variables.
            self.seventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.seventh_type.value])
            self.seventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.seventh_note)

        else:

            # If type instance variable is set to None, the note and interval are also set to None.
            self.seventh_note: str = None
            self.seventh_interval: int = None

    def set_ninth(self, new_ninth_type: Optional[NinthType] = None):

        """
        Updates the instance variable specific to the ninth note in the chord.

        This method either sets a new ninth note of the chord, or removes the ninth note from the chord entirely if new_ninth_type is set to None.

        If a new ninth note is added to the chord without a pre-existing seventh note, the seventh note is also added to the chord automatically.

        Args:

            new_ninth_type (NinthType): The new ninth note of the chord.
        
        """

        # Sets the type instance variable.
        self.ninth_type: NinthType = new_ninth_type

        if new_ninth_type:

            # Ensures that a chord featuring an ninth note also features a seventh note.
            if not self.seventh_type:

                self.seventh_type: SeventhType = SeventhType.MINOR
                self.seventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.seventh_type.value])
                self.seventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.seventh_note)
            
            # Sets the note and interval instance variables.
            self.ninth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.ninth_type.value])
            self.ninth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.ninth_note)

        else:

            # If type instance variable is set to None, the note and interval are also set to None.
            self.ninth_note: str = None
            self.ninth_interval: int = None

    def set_eleventh(self, new_eleventh_type: EleventhType = None):

        """
        Updates the instance variable specific to the eleventh note in the chord.

        This method either sets a new eleventh note of the chord, or removes the eleventh note from the chord entirely if new_eleventh_type is set to None.

        If a new eleventh note is added to the chord without a pre-existing ninth note or seventh note, these notes are also added to the chord automatically.

        Args:

            new_eleventh_type (EleventhType): The new eleventh note of the chord.
        
        """

        # Sets the type instance variable.
        self.eleventh_type: EleventhType = new_eleventh_type

        if new_eleventh_type:

            # Ensures that a chord featuring an eleventh note also features a seventh note.
            if not self.seventh_type:

                self.seventh_type: SeventhType = SeventhType.MINOR
                self.seventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.seventh_type.value])
                self.seventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.seventh_note)
            
            # Ensures that a chord featuring an eleventh note also features a ninth note.
            if not self.ninth_type:

                self.ninth_type: NinthType = NinthType.MAJOR
                self.ninth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.ninth_type.value])
                self.ninth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.ninth_note)

            # Sets the note and interval instance variables.
            self.eleventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.eleventh_type.value])
            self.eleventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.eleventh_note)

        else:

            # If type instance variable is set to None, the note and interval are also set to None.
            self.eleventh_note: str = None
            self.eleventh_interval: int = None

    def set_thirteenth(self, new_thirteenth_type: ThirteenthType = None):

        """
        Updates the instance variable specific to the thirteenth note in the chord.

        This method either sets a new thirteenth note of the chord, or removes the thirteenth note from the chord entirely if new_thirteenth_type is set to None.

        If a new thirteenth note is added to the chord without a pre-existing eleventh note, ninth note or seventh note, these notes are also added to the chord automatically.

        Args:

            new_thirteenth_type (ThirteenthType): The new thirteenth note of the chord.
        
        """

        # Sets the type instance variable.
        self.thirteenth_type: ThirteenthType = new_thirteenth_type

        if new_thirteenth_type:

            # Ensures that a chord featuring an thirteenth note also features a seventh note.
            if not self.seventh_type:

                self.seventh_type: SeventhType = SeventhType.MINOR
                self.seventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.seventh_type.value])
                self.seventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.seventh_note)

             # Ensures that a chord featuring an thirteenth note also features a ninth note.           
            if not self.ninth_type:

                self.ninth_type: NinthType = NinthType.MAJOR
                self.ninth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.ninth_type.value])
                self.ninth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.ninth_note)

            # Ensures that a chord featuring an thirteenth note also features a eleventh note.
            if not self.eleventh_type:

                self.eleventh_type: EleventhType = EleventhType.PERFECT
                self.eleventh_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.eleventh_type.value])
                self.eleventh_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.eleventh_note)

            # Sets the note and interval instance variables.
            self.thirteenth_note: str = calculate_note(CHROMATIC_SCALE, self._root_index, INTERVALS_DICT[self.thirteenth_type.value])
            self.thirteenth_interval: int = calculate_interval(CHROMATIC_SCALE, self._root_index, self.thirteenth_note)

        else:

            # If type instance variable is set to None, the note and interval are also set to None.
            self.thirteenth_note: str = None
            self.thirteenth_interval: int = None



if __name__ == "__main__":

    """
    print("--------------------")

    print("Instantiate Chord object: Chord(root_type=RootType.C, thirteenth_type=ThirteenthType.MAJOR)")
    
    print("--------------------")

    chord = Chord(root_type=RootType.C, thirteenth_type=ThirteenthType.MAJOR)

    print(f"Chord object root: {chord.root_note}")

    print(f"Chord object third: {chord.third_note}")

    print(f"Chord object fifth: {chord.fifth_note}")

    print(f"Chord object note signature: {chord.note_signature()}")

    print(f"Chord object index signature: {chord.interval_signature()}")

    print("--------------------")

    print("Set new root note: chord.set_root(new_root_type=RootType.G)")

    print("--------------------")

    chord.set_root(new_root_type=RootType.G)

    print(f"Chord object root: {chord.root_note}")

    print(f"Chord object third: {chord.third_note}")

    print(f"Chord object fifth: {chord.fifth_note}")

    print(f"Chord object note signature: {chord.note_signature()}")

    print(f"Chord object index signature: {chord.interval_signature()}")

    """

    print("--------------------")

    print("Instantiate Chord object: demo_without = Chord(root_type=RootType.C)")

    print("set_thirteenth")

    print("--------------------")

    demo_without = Chord(root_type=RootType.C)

    demo_without.set_thirteenth(new_thirteenth_type=ThirteenthType.MAJOR)

    print(f"Without object root: {demo_without.root_note}")

    print(f"Without object third: {demo_without.third_note}")

    print(f"Without object fifth: {demo_without.fifth_note}")

    print(f"Without object seventh: {demo_without.seventh_note}")

    print(f"Without object ninth: {demo_without.ninth_note}")

    print(f"Without object eleventh: {demo_without.eleventh_note}")

    print(f"Without object thirteenth: {demo_without.thirteenth_note}")

    print(f"Without object note signature: {demo_without.note_signature()}")

    print(f"Without object index signature: {demo_without.interval_signature()}")

    print("--------------------")

    print("Instantiate Chord object: demo_with = Chord(root_type=RootType.C)")

    print("set_seventh, set_ninth, set_eleventh, set_thirteenth")

    print("--------------------")

    demo_with = Chord(root_type=RootType.C)

    demo_with.set_seventh(new_seventh_type=SeventhType.MINOR)

    demo_with.set_ninth(new_ninth_type=NinthType.MAJOR)

    demo_with.set_eleventh(new_eleventh_type=EleventhType.PERFECT)

    demo_with.set_thirteenth(new_thirteenth_type=ThirteenthType.MAJOR)

    print(f"With object root: {demo_with.root_note}")

    print(f"With object third: {demo_with.third_note}")

    print(f"With object fifth: {demo_with.fifth_note}")

    print(f"With object seventh: {demo_with.seventh_note}")

    print(f"With object ninth: {demo_with.ninth_note}")

    print(f"With object eleventh: {demo_with.eleventh_note}")

    print(f"With object thirteenth: {demo_with.thirteenth_note}")

    print(f"With object note signature: {demo_with.note_signature()}")

    print(f"With object index signature: {demo_with.interval_signature()}")

    print("--------------------")

    demo_with.set_root(new_root_type=RootType.G)

    print(f"With object root: {demo_with.root_note}")

    print(f"With object third: {demo_with.third_note}")

    print(f"With object fifth: {demo_with.fifth_note}")

    print(f"With object seventh: {demo_with.seventh_note}")

    print(f"With object ninth: {demo_with.ninth_note}")

    print(f"With object eleventh: {demo_with.eleventh_note}")

    print(f"With object thirteenth: {demo_with.thirteenth_note}")

    print(f"With object note signature: {demo_with.note_signature()}")

    print(f"With object index signature: {demo_with.interval_signature()}")

    print("--------------------")
