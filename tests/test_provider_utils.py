from spotdl.providers.provider_utils import _parse_duration


def test_parse_duration():
    """
    Test the duration parsing
    """

    assert _parse_duration("3:16") == 196.0
    assert _parse_duration("20") == 20.0
    assert _parse_duration("25:59") == 1559.0
    assert _parse_duration("25:59:59") == 93599.0
    assert _parse_duration("likes") == 0.0
    assert _parse_duration("views") == 0.0
    assert _parse_duration([1, 2, 3]) == 0.0
    assert _parse_duration({"json": "data"}) == 0.0
