from lib.check_grammar import check_grammar
import pytest

def test_sentence_starts_with_capital_ends_with_no_punctuation():
    result = check_grammar("Hello, I am Jesse")
    assert result == False

def test_sentence_starts_with_capital_ends_with_fullstop():
    result = check_grammar("Hello, I am Jesse.")
    assert result == True

def test_sentence_starts_with_capital_ends_with_question():
    result = check_grammar("Hello, are you James?")
    assert result == True

def test_sentence_starts_with_capital_ends_with_exclamation():
    result = check_grammar("Meowth, that's right!")
    assert result == True

def test_sentence_starts_with_capital_ends_with_comma():
    result = check_grammar("Hello, I am Jesse,")
    assert result == False

def test_sentence_starts_with_capital_ends_with_colon():
    result = check_grammar("Hello, I am Jesse:")
    assert result == False

def test_sentence_starts_with_lowercase_ends_with_fullstop():
    result = check_grammar("hello, I am Jesse.")
    assert result == False

def test_empty_string_raises_exception():
    with pytest.raises(Exception) as e:
        check_grammar("")
    assert str(e.value) == "I have nothing to check"