import siggy
import os
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_int_to_var_bytes_8(self):
        self.assertEqual(siggy.int_to_var_bytes(TestVectors.bytes_8_vector[0]),TestVectors.bytes_8_vector[1])
        
    def test_int_to_var_bytes_16(self):
        self.assertEqual(siggy.int_to_var_bytes(TestVectors.bytes_16_vector[0]),TestVectors.bytes_16_vector[1])
    
    def test_int_to_var_bytes_32(self):
        self.assertEqual(siggy.int_to_var_bytes(TestVectors.bytes_32_vector[0]),TestVectors.bytes_32_vector[1])
        
    def test_int_to_var_bytes_64(self):
        self.assertEqual(siggy.int_to_var_bytes(TestVectors.bytes_64_vector[0]),TestVectors.bytes_64_vector[1])
    
    def test_bitcoin_sig_hash(self):
        self.assertEqual(siggy.bitcoin_sig_hash(TestVectors.sig_hash_vector[0]),TestVectors.sig_hash_vector[1])
    
    def test_verify_signature_valid(self):
        self.assertEqual(siggy.verify_signature(*TestVectors.sig_valid_vector1[0]),TestVectors.sig_valid_vector1[1])
        self.assertEqual(siggy.verify_signature(*TestVectors.sig_valid_vector2[0]),TestVectors.sig_valid_vector2[1])
        
    def test_verify_signature_invalid(self):
        self.assertEqual(siggy.verify_signature(*TestVectors.sig_invalid_vector1[0]),TestVectors.sig_invalid_vector1[1])
        self.assertEqual(siggy.verify_signature(*TestVectors.sig_invalid_vector2[0]),TestVectors.sig_invalid_vector2[1])
        self.assertEqual(siggy.verify_signature(*TestVectors.sig_invalid_vector3[0]),TestVectors.sig_invalid_vector3[1])

class TestVectors(object):    
    bytes_8_vector = (77, bytearray([77]))
    bytes_16_vector = (777, bytearray([253,9,3]))
    bytes_32_vector = (77777, bytearray([254,209,47,1,0]))
    bytes_64_vector = (7777777777, bytearray([255,113,120,151,207,1,0,0,0]))
    sig_hash_vector = (b'test message', b'\x12&\x17\x9d\xdfc\x83\xfb\xcfQ\x02\xc9I%8\xb7 ls\x9a\xe7\x9e\xb0d@\x8c*\xbdg\xd3\x9b\xed')
    sig_valid_vector1 = (('test message','HyzVUenXXo4pa+kgm1vS8PNJM83eIXFC5r0q86FGbqFcdla6rcw72/ciXiEPfjli3ENfwWuESHhv6K9esI0dl5I=','19qVgG8C6eXwKMMyvVegsi3xCsKyk3Z3jV'),True)
    sig_valid_vector2 = (('test message','GyCcIuqP9WaQ7fGeqTdRpnD1eNXu6P/rMxR0eR65YaZy+wmG0F+ClUQrZEkI1tyugE3tBGkdkaLdKTq5bwEYeto=','1BFcFimfkLQjuTV6vjQ7nd66MGQ5zcT6ty'),True)
    sig_invalid_vector1 = (('test message','HyzVUenXXo4pa+kgm1vS8PNJM83eIXF','19qVgG8C6eXwKMMyvVegsi3xCsKyk3Z3jV'),False)
    sig_invalid_vector2 = (('test message','HyzVUenXXo4pa+kgm1vS8PNJM83eIXF+','19qVgG8C6eXwKMMyvVegsi3xCsKyk3Z3jV'),False)
    sig_invalid_vector3 = (('test message1','HyzVUenXXo4pa+kgm1vS8PNJM83eIXFC5r0q86FGbqFcdla6rcw72/ciXiEPfjli3ENfwWuESHhv6K9esI0dl5I=','19qVgG8C6eXwKMMyvVegsi3xCsKyk3Z3jV'),False)