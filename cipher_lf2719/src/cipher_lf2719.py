import pandas as pd
import numpy as np

def cipher(text, shift, encrypt=True):
    """
        Takes user's text input and encrypts it by shifting the letters by defined shift.

        Parameters
        ----------
        text: pandas.Series.str
            TEXT pandas character string.
        shift: numpy.int64
            SHIFT numpy integer that defines by how much will the letter shift from their position in the alphabet.

        Returns
        -------
        pandas.Series.str
            Encrypted string is pandas string.

        Examples
        --------
        >>> from cipher_lf2719 import cipher_lf2719
        >>> text = "hello world"
        >>> shift = 5
        >>> cipher("hello world", 5)
        
        'mjqqt Btwqi'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
