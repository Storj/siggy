# This file is part of Heartbeat: https://github.com/Storj/heartbeat
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Will James <jameswt@gmail.com>
#
# Pieces of this code were derived from pybitcointools by Vitalik Buterin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pycoin.ecdsa import *  # NOQA
from pycoin.encoding import *  # NOQA
import math
import base64

BIN_SIGNATURE_LENGTH = 65
SIGNATURE_LENGTH = 4 * math.ceil(BIN_SIGNATURE_LENGTH / 3.0)


def int_to_var_bytes(x):
    """Converts an integer to a bitcoin variable length integer as a bytearray

    :param x: the integer to convert
    """
    if x < 253:
        return intbytes.to_bytes(x, 1)
    elif x < 65536:
        return bytearray([253]) + intbytes.to_bytes(x, 2)[::-1]
    elif x < 4294967296:
        return bytearray([254]) + intbytes.to_bytes(x, 4)[::-1]
    else:
        return bytearray([255]) + intbytes.to_bytes(x, 8)[::-1]


def bitcoin_sig_hash(message):
    """Bitcoin has a special format for hashing messages for signing.

    :param message: the encoded message to hash in preparation for verifying
    """
    padded = b'\x18Bitcoin Signed Message:\n' +\
        int_to_var_bytes(len(message)) +\
        message
    return double_sha256(padded)


def verify_signature(message, signature, address):
    """This function verifies a bitcoin signed message.

    :param message: the plain text of the message to verify
    :param signature: the signature in base64 format
    :param address: the signing address
    """
    if (len(signature) != SIGNATURE_LENGTH):
        return False

    try:
        binsig = base64.b64decode(signature)
    except:
        return False

    r = intbytes.from_bytes(binsig[1:33])

    s = intbytes.from_bytes(binsig[33:65])

    val = intbytes.from_bytes(bitcoin_sig_hash(message.encode()))

    pubpairs = possible_public_pairs_for_signature(
        generator_secp256k1,
        val,
        (r, s))

    addr_hash160 = bitcoin_address_to_hash160_sec(address)

    for pair in pubpairs:
        if (public_pair_to_hash160_sec(pair, True) == addr_hash160):
            return True
        if (public_pair_to_hash160_sec(pair, False) == addr_hash160):
            return True

    return False
