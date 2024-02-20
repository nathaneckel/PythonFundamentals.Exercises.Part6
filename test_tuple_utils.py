import unittest
import unittest.mock
from io import StringIO
import tuple_utils


class TupleUtilsTest(unittest.TestCase):

    def test_tic_tac_toe_finish(self):
        board_in = (
            ['O', 'X', ''],
            ['X', 'X', ''],
            ['', '', '']
        )
        board_out = (
            ['O', 'X', ''],
            ['X', 'X', 'X'],
            ['', '', '']
        )
        tuple_utils.tic_tac_toe_finish(board_in, 1, 2, 'X')
        self.assertEqual(board_in, board_out)

    def test2_tic_tac_toe_finish(self):
        board_in = (
            ['', '', ''],
            ['X', 'O', ''],
            ['X', '', 'O']
        )
        board_out = (
            ['O', '', ''],
            ['X', 'O', ''],
            ['X', '', 'O']
        )
        tuple_utils.tic_tac_toe_finish(board_in, 0, 0, 'O')
        self.assertEqual(board_in, board_out)

    def test_count_instances(self):
        test_cases = [
            ((1, 1, 1, 0), 1, 3),
            (('A', 'B', 'B', 'C'), 'B', 2)
        ]
        for tuple_to_evaluate, item_to_count, expected in test_cases:
            with self.subTest(f"{tuple_to_evaluate}, {item_to_count} -> {expected}"):
                self.assertEqual(expected, tuple_utils.count_instances(tuple_to_evaluate, item_to_count))

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_indexes_and_entries(self, mock_stdout):
        indexes = ('Bilbo', 'Thorin', 'Gandalf')
        entries = ('Burglar', 'Leader', 'Wizard')
        tuple_utils.print_indexes_and_entries(indexes, entries)

        expected = "Index: Bilbo      Entry: Burglar\n" \
                   "Index: Thorin     Entry: Leader\n" \
                   "Index: Gandalf    Entry: Wizard\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test2_print_indexes_and_entries(self, mock_stdout):
        indexes = (1, 2, 3)
        entries = ('A', 'B', 'C')
        tuple_utils.print_indexes_and_entries(indexes, entries)

        expected = "Index: 1          Entry: A\n" \
                   "Index: 2          Entry: B\n" \
                   "Index: 3          Entry: C\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_items_with_index(self, mock_stdout):
        items = ('Pride', 'Envy', 'Gluttony', 'Lust', 'Anger', 'Greed', 'Sloth')
        tuple_utils.print_items_with_index(items)

        expected = "1: Pride\n" \
                   "2: Envy\n" \
                   "3: Gluttony\n" \
                   "4: Lust\n" \
                   "5: Anger\n" \
                   "6: Greed\n" \
                   "7: Sloth\n"
        self.assertEqual(expected, mock_stdout.getvalue())
