# 测试文件名，以test_ 开头，或以 _test结尾
# 测试函数名，以test_ 开头
import pytest

@pytest.mark.pass0
@pytest.mark.pass1
def test_pass1_p0():
    assert (1, 2, 3) == (1, 2, 3)

@pytest.mark.pass1
def test_pass2_p0():
    assert (1, 2, 3) == (1, 2, 3)
    if 2>1:
        print(2)
    elif 2==1:
        print(0)
    else:
        print(1)
    if 2==1:
        print(2)
    else:
        print(1)

@pytest.mark.failed
def test_fail1():
    assert (1, 2, 3) == (3, 2, 1)
    