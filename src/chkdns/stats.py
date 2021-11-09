from typing import DefaultDict


class Stats(object):
    """A utility object used to store statistics."""

    def __init__(self, server_count: int):
        """A utility object used to store statistics.

        Args:
            server_count (int): The number of servers. Used to calculate percentages.
        """
        self.server_count = server_count
        self.stats: dict[str, int] = DefaultDict(int)

    def get_types(self) -> list[str]:
        """Returns a list of all types."""
        return list(self.stats.keys())

    def add(self, type) -> None:
        """Increment the count of the given type. If the type does not exist, it is added to the data structure."""
        self.stats[type] += 1

    def percentage_of(self, type) -> str:
        """Returns the percentage of the given type as a string."""
        return f"{self.stats[type] / self.server_count * 100:.2f}%"
