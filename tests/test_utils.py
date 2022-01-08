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
