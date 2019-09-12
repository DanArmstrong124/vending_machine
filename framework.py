def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(num1, num2):
    assert num1 != num2, "{0} should not be equal to {1}".format(num1, num2)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} should not contain {1}".format(collection, item)
    
def test_is_between(lower, num, higher):
    assert lower < num < higher, "{0} should be lower than {1} which should be lower than {2}".format(lower, num, higher)
    
test_are_equal(2, 2)

test_not_equal(1, 2)

test_is_in([1,2,3,4,5], 5)

test_not_in([1,2,3,4,5], 6)

test_is_between(1, 2, 3)

print("ALL TESTS PASSED!!!")