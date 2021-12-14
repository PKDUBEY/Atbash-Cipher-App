import pytest

from atbash_cipher import AtbashCipher


def test_encrypt_dycrypt():
    output = AtbashCipher().encrypt_dycrypt('Hello world!')
    assert output == 'Svool dliow!'

def test2_encrypt_dycrypt():
    output = AtbashCipher().encrypt_dycrypt('Christmas is the 25th of December')
    assert output == 'Xsirhgnzh rh gsv 25gs lu Wvxvnyvi'