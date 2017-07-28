from persistentdatatools import remove_spaces, remove_spaces_add_hyphen, remove_extra_spaces,  \
    remove_symbol_add_symbol, split_string_retain_spaces, join_split_string, split_strings_in_list_retain_spaces

# test with pytest


def test_remove_spaces():
    assert remove_spaces('a b   c d  e       f') == 'abcdef'


def test_remove_spaces_add_hyphen():
    assert remove_spaces_add_hyphen('a  b  c  d  e  f') == 'a-b-c-d-e-f'


def test_remove_extra_spaces():
    assert remove_extra_spaces('a b  c   d     e       f') == 'a b c d e f'


def test_remove_symbol_add_symbol():
    assert remove_symbol_add_symbol('a-b-c- -', '-', '*') == 'a*b*c* *'


def test_split_string_retain_spaces():
    assert split_string_retain_spaces('hello there    you') == ['hello', ' ', 'there', '    ', 'you']


def test_join_split_string():
    assert join_split_string(['hello', ' ', 'there', '    ', 'you']) == 'hello there    you'


def test_split_strings_in_list_retain_spaces():
    assert split_strings_in_list_retain_spaces(['hey there', 'hi  there', 'ho      there']) == [['hey', ' ', 'there'],
                                                                                                ['hi', '  ', 'there'],
                                                                                                ['ho', '      ',
                                                                                                 'there']]