import pytest
import socket

def test_raises():
    with pytest.raises(TypeError) as e:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
        s.connect(('127.0.0.1', "6379"))
    exec_msg = e.value.args[0]
    print(e)
    assert exec_msg == 'an integer is required (got type str)'