import pytest

from atbash_cipher import AtbashCipher


def test_encrypt_dycrypt():
    output = AtbashCipher().encrypt_dycrypt('Hello world!')
    assert output == 'Svool dliow!'

def test2_encrypt_dycrypt():
    output = AtbashCipher().encrypt_dycrypt('World!')
    assert output == 'Dliow!'