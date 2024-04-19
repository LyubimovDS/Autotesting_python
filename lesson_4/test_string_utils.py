from string_utils import * 


stringUtils = StringUtils()


def test_capitilize():
    assert stringUtils.capitilize("hello") == "Hello" 


def test_trim():
    assert stringUtils.trim("  hello  ") == "hello  " 


def test_string_to_list():
    assert stringUtils.to_list("H, e, l, l, o") == ["H", " e", " l", " l", " o"]


def test_string_sep_with_spase_to_list():
    assert stringUtils.to_list("H, e, l, l, o", ", ") == ["H", "e", "l", "l", "o"]

def test_contains_false():
    assert stringUtils.contains("hello", "H") == False 


def test_contains_true():
    assert stringUtils.contains("hello", "h") == True


def test_delete_symbol():
    assert stringUtils.delete_symbol("abracadabra", "ra") == "abcadab"


def test_starts_with_true():
    assert stringUtils.starts_with("Hello", "H") == True 


def test_starts_with_False():
    assert stringUtils.starts_with("Hello", "h") == False


def test_end_with_true():
    assert stringUtils.end_with("hello", "o") == True 


def test_end_with_false():
    assert stringUtils.end_with("hello", "O") == False


def test_is_empty_true():
    assert stringUtils.is_empty("") == True


def test_is_empty_with_spase_true():
    assert stringUtils.is_empty(" ") == True


def test_is_empty_false():
    assert stringUtils.is_empty("as") == False


def test_list_to_string_defolt():
    assert stringUtils.list_to_string([1, 2, 3]) == "1, 2, 3"


def test_list_to_string_with_sep():
    assert stringUtils.list_to_string(["Hel", "lo"], '') == "Hello"

