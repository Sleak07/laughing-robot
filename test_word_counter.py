import pytest

from word_counter import CleanInput


@pytest.fixture
def clean_input():
    return CleanInput


class TestCleanInput:
    def test_take_input_string(self, clean_input):
        input_str = "Fox is in orange car"
        clean_input.take_input(input_str)

        assert clean_input.input_str == input_str


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Fox IS in a Orange car", "fox is in a orange car"),
        ("Hello", "hello"),
    ],
)
def test_clean_user(clean_input, input_str, expected):
    clean_input.take_input(input_str)
    result = clean_input.clean_user()
    assert result == expected
