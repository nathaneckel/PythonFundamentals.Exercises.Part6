import io
from typing import Iterable, Tuple, List, Union
TicTacToeRow = List[str]
TicTacToeBoard = Tuple[TicTacToeRow, TicTacToeRow, TicTacToeRow]

def tic_tac_toe_finish(board: TicTacToeBoard, pos_y: int, pos_x: int, symbol: str) -> None:
    TicTacToeBoard2 = List[str]

    for i in range(len(board)):
        if i != pos_y:
            TicTacToeBoard2 = (board [i],)

        elif i == pos_y:
            row = board [i]
            row[pos_x] = symbol

            TicTacToeBoard2 = TicTacToeBoard2,(row,)

    """
    This function takes in a TicTacToeBoard and applies the finishing move based on the provided parameters 
    pos_y, pos_x, and symbol.
    :param board: A tuple containing 3 TicTacToeRows. Each TicTacToeRow in turn is a list containing 3 strings
    :param pos_y: The position of the TicTacToeRow that needs to be modified
    :param pos_x: The position of the column within a TicTacToeRow that needs to be modified
    :param symbol: The symbol that should be placed in the column (X, or O)
    :return: None
    """


def count_instances(collection: Tuple, instance: Union[int, str]) -> int:
    count = 0
    for item in collection:
        if item == instance:
            count += 1
    return count

"""
This function counts the number of occurrences of the ***INSTANCE VALUE*** within the ***COLLECTION*** parameter.
:param COLLECTION: A tuple containing 0 or more instances
:param INSTANCE: An ITEM IN the collection parameter
:return: An INTEGER.
"""


def print_indexes_and_entries(indexes: Iterable, entries: Iterable) -> None:
    for i, index in enumerate(indexes):
        entry = entries[i]
        print(f"Index: {index: <10} Entry: {entry}")

    """
    This function iterates through the given parameters and PRINTS the items formatted according to the following rules:
    The index of the indexes iterable correspond to the index of the ENTRIES iterable.
    The index takes 10 places even if it doesn't need all 10 places.
    :param indexes: A list or tuple
    :param entries: A list or tuple
    :return: None
    """
import io
from typing import Iterable, Tuple, List, Union


def print_items_with_index(items: Iterable):
        for i, item in enumerate(items, start=1):
            print(f"{i}: {item}")
        """
    This function iterates through the items parameter and prints the item formatted according to the following rules:
    Each item printed received the index 1-N where N is the size of the items parameter.
    Indexes start at 1.
    Each index and item are separated by a colon and a space.
    :param items: A tuple or a list
    :return: None
    """