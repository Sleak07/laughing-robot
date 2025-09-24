"""Utilities to clean user input, count words, and render simple reports.

Classes:
- CleanInput: capture and normalize user input
- UniqueWords: compute frequencies and stats
- Diagram: filter stop words, render charts, and save reports
"""
# TODO:  Accept the user input and clean the input
from collections import Counter
from typing import Counter as CounterType, Dict, List, Tuple, Optional, Set

class CleanInput:
    """Manage raw user input and provide normalization utilities.

    Attributes:
        user: The current input string.
    """
    def __init__(self, user: str) -> None:
        self.user = user

    def take_input_string(self) -> str:
        """Prompt the user for a sentence and store it.

        Returns:
            str: The raw input string as entered by the user.
        """
        self.user = input("Enter a sentence of your choice: ")
        return self.user

    def clean_user(self) -> str:
        """Normalize the current input by lowercasing and stripping whitespace.

        Returns:
            str: The cleaned input string.
        """
        return self.user.lower().strip()


# FIX: Write Test for these classes
class UniqueWords(CleanInput):
    """Utilities for word frequency analysis derived from cleaned input."""
    def __init__(self, user: str) -> None:
        super().__init__(user)

    def word_frequency(self) -> CounterType[str]:
        """Compute the frequency of each word in the cleaned input.

        Returns:
            Counter[str]: A counter mapping words to their counts.
        """
        words = self.clean_user().split()
        return Counter(words)

    def most_common(self, n: int = 5) -> List[Tuple[str, int]]:
        """Return the top-N most common words.

        Args:
            n (int): Number of items to return. Defaults to 5.

        Returns:
            List[Tuple[str, int]]: Word/count pairs ordered by frequency.
        """
        return self.word_frequency().most_common(n)

    def stats(self) -> Dict[str, int]:
        """Compute simple statistics about the cleaned input.

        Returns:
            Dict[str, int]: Total and unique word counts.
        """
        words = self.clean_user().split()
        return {"total_words": len(words), "unique_words": len(set(words))}

    def report(self) -> None:
        """Print a frequency report of all words in descending order."""
        freq = self.word_frequency()
        for word, count in freq.most_common():
            print(f"{word:15} {count}")


# List of common stop words to filter
STOP_WORDS: Set[str] = {"the", "and", "of", "to", "a", "in", "is", "it", "you", "that"}


class Diagram(UniqueWords):
    """Visualization and reporting helpers built on word frequencies."""
    def __init__(self, user: str) -> None:
        super().__init__(user)

    # Filter out stop words
    def filtered_frequency(self) -> CounterType[str]:
        """Compute word frequencies excluding common stop words.

        Returns:
            Counter[str]: A counter of non-stop words.
        """
        words = [w for w in self.clean_user().split() if w not in STOP_WORDS]
        return Counter(words)

    # Simple text-based bar chart
    def bar_chart(self, n: int = 10) -> None:
        """Print a simple text-based bar chart of the top-N words.

        Args:
            n (int): Number of words to display. Defaults to 10.
        """
        freq = self.filtered_frequency().most_common(n)
        for word, count in freq:
            print(f"{word:10} {'#' * count}")

    # Save word frequency report to a file
    def save_report(self, filename: str = "report.txt") -> None:
        """Save the filtered word frequency report to a file.

        Args:
            filename (str): Output file path. Defaults to "report.txt".
        """
        freq = self.filtered_frequency()
        with open(filename, "w") as f:
            for word, count in freq.most_common():
                f.write(f"{word:15} {count}\n")

    # Find longest and shortest words
    def word_lengths(self) -> Dict[str, Optional[str]]:
        """Find the longest and shortest non-stop words.

        Returns:
            Dict[str, Optional[str]]: Longest and shortest words, or None if no words.
        """
        words = [w for w in self.clean_user().split() if w not in STOP_WORDS]
        if not words:
            return {"longest": None, "shortest": None}
        return {"longest": max(words, key=len), "shortest": min(words, key=len)}


def main() -> None:
    """Run a demo workflow that prompts for input and prints reports."""
    user_input = ""
    diag = Diagram(user_input)
    diag.take_input_string()
    print("\nCleaned Input:", diag.clean_user())
    print("\nWord Frequency Report:")
    diag.report()
    print("\nFiltered Word Frequency:")
    for word, count in diag.filtered_frequency().most_common():
        print(f"{word:15} {count}")
    print("\nBar Chart:")
    diag.bar_chart()
    stats = diag.stats()
    print(
        f"\nTotal words: {stats['total_words']}, Unique words: {stats['unique_words']}"
    )
    lengths = diag.word_lengths()
    print(f"Longest word: {lengths['longest']}, Shortest word: {lengths['shortest']}")
    diag.save_report()
    print("\nReport saved to 'report.txt'")


if __name__ == "__main__":
    main()
