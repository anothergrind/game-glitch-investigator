from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_range_for_hard_is_harder_than_normal():
    # Regression: Hard used to be narrower than Normal.
    assert get_range_for_difficulty("Hard") == (1, 200)


def test_range_defaults_to_normal_when_unknown():
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_parse_guess_rejects_none_and_blank():
    assert parse_guess(None) == (False, None, "Enter a guess.")
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_parse_guess_rejects_decimal_input():
    # Regression: decimal strings used to be truncated by int conversion.
    assert parse_guess("3.7") == (False, None, "That is not a whole number.")


def test_parse_guess_rejects_non_numeric_input():
    assert parse_guess("hello") == (False, None, "That is not a number.")


def test_parse_guess_accepts_whole_number():
    assert parse_guess("42") == (True, 42, None)


def test_winning_guess_returns_win_outcome_and_message():
    assert check_guess(50, 50) == ("Win", "🎉 Correct!")


def test_guess_too_high_has_correct_directional_hint():
    # Regression: high/low hints were previously swapped.
    assert check_guess(60, 50) == ("Too High", "📉 Go LOWER!")


def test_guess_too_low_has_correct_directional_hint():
    # Regression: high/low hints were previously swapped.
    assert check_guess(40, 50) == ("Too Low", "📈 Go HIGHER!")


def test_update_score_deducts_five_for_too_high_and_too_low_symmetrically():
    # Regression: Too High used to be rewarded in some attempts.
    assert update_score(100, "Too High", 2) == 95
    assert update_score(100, "Too Low", 2) == 95


def test_update_score_applies_win_points_with_floor():
    assert update_score(0, "Win", 1) == 80
    assert update_score(0, "Win", 20) == 10


def test_update_score_unknown_outcome_leaves_score_unchanged():
    assert update_score(77, "Invalid", 3) == 77
