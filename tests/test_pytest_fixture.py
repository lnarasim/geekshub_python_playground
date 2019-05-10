import pytest

# The following snippet explains pytest.fixture with function scope
count = 0
@pytest.fixture
def test_function_fixture():
    global count
    count += 1
    msg = f"test_function_fixture is called - {count} times"
    print("calling test_function_fixture")
    return msg


def test_function_fixture_1(test_function_fixture):
    assert test_function_fixture == "test_function_fixture is called - 1 times"


def test_function_fixture_2(test_function_fixture):
    assert test_function_fixture == "test_function_fixture is called - 2 times"


def test_function_fixture_3(test_function_fixture):
    assert test_function_fixture == "test_function_fixture is called - 3 times"


# Let us do module fixture

# The following snippet explains pytest.fixture with function scope
module_count = 0
@pytest.fixture(scope='module')
def test_module_fixture():
    global module_count
    module_count += 1
    msg = f"test_module_fixture is called - {module_count} times"
    print("calling test_module_fixture")
    return msg


def test_module_fixture_1(test_module_fixture):
    assert test_module_fixture == "test_module_fixture is called - 1 times"
    assert module_count == 1


def test_module_fixture_2(test_module_fixture):
    assert test_module_fixture == "test_module_fixture is called - 1 times"
    assert module_count == 1


def test_module_fixture_3(test_module_fixture):
    assert test_module_fixture == "test_module_fixture is called - 1 times"
    assert module_count == 1