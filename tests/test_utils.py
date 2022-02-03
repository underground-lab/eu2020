from unittest.mock import patch

import pytest

from eu2020.app import main
from eu2020.common.utils import auto_set_option_keys


def test_auto_set_option_keys():
    event = {"options": [{"description": "ano"}, {"description": "ne"}]}
    auto_set_option_keys(event)
    assert event["options"][0]["key"] == "a"
    assert event["options"][1]["key"] == "n"


def test_auto_set_option_keys_no_change():
    event = {
        "options": [
            {"key": "n", "description": "ano"},
            {"key": "e", "description": "ne"},
        ],
    }
    auto_set_option_keys(event)
    assert event["options"][0]["key"] == "n"
    assert event["options"][1]["key"] == "e"


@pytest.mark.parametrize(
    "user_input",
    (
        pytest.param([EOFError(), "A"], id="^D setup"),
        pytest.param(["Jan", EOFError(), "A"], id="^D input_with_options"),
        pytest.param(["Jan", "m", EOFError(), "A"], id="^D proceed"),
    )
)
def test_exit_confirmed(user_input, capsys):
    with patch("builtins.input", side_effect=user_input):
        try:
            main()
        except SystemExit:
            pass
    assert "Na shledanou." in capsys.readouterr().out
    assert not capsys.readouterr().err


@pytest.mark.parametrize(
    "user_input",
    (
        pytest.param([EOFError(), "n", "Jan"], id="^D setup"),
        pytest.param(["Jan", EOFError(), "n", "m"], id="^D input_with_options"),
        pytest.param(["Jan", "m", EOFError(), "n", ""], id="^D proceed"),
    )
)
def test_exit_cancelled(user_input, capsys):
    with patch("builtins.input", side_effect=user_input):
        try:
            main()
        except StopIteration:
            pass
    assert "Na shledanou." not in capsys.readouterr().out
    assert not capsys.readouterr().err
