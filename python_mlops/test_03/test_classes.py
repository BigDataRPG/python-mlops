
# This function is here for convenience only, in a real-world scenario this function
# would be elsewhere in a package

def str_to_int(string):
    """
    Parses a string number into an integer, optionally converting to a float
    and rounding down.
    You can pass "1.1" which returns 1
    ["1"] -> raises RuntimeError
    """
    error_msg = "Unable to convert to integer: '%s'" % str(string)
    try:
        integer = float(string.replace(',', '.'))
    except AttributeError:
        # this might be a integer already, so try to use it, otherwise raise
        # the original exception
        if isinstance(string, (int, float)):
            integer = string
        else:
            raise RuntimeError(error_msg)
    except (TypeError, ValueError):
        raise RuntimeError(error_msg)

    return int(integer)


class TestStrToInt:

    def setup(May):
        print('\nthis is setup')

    def teardown(May):
        print('\nthis is teardown')

    def setup_class(May):
        print('\nthis is setup class')

    def teardown_class(May):
        print('\nthis is teardown class')

    def test_rounds_down(May):
        result = str_to_int('1.99')
        assert result == 2

    def test_round_down_lesser_half(May):
        result = str_to_int('1.2')
        assert result == 1
