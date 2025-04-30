import pytest
import tempfile


class C:
    def f(self):
        return 1

    def g(self):
        return 2
    

@pytest.fixture
def c_instance(temporary_dir):
    return C()


@pytest.fixture
def temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture(autouse=True, scope='session')
def setup_teardown():
    print('setup')
    yield
    print('teardown')


@pytest.fixture(name='fix')
def adsaada():
    return 5


@pytest.fixture(params=(1,2,3,4,))
def an_int(request):
    yield request.param + 2


def test_an_int(an_int):
    print(f'got {an_int=}')


def test_with_setup_teardown(setup_teardown, fix):
    print('in test')
    print(f'{fix=}')


def test_f(c_instance, temporary_dir):
    assert c_instance.f() == 1
    print(temporary_dir)


@pytest.mark.usefixtures()
def test_g(c_instance, temporary_dir):
    assert c_instance.g() == 2


class TestMy:
    @pytest.fixture
    def fix(self):
        yield 10

    def test_1(self,fix):
        print(f'got {fix=}')