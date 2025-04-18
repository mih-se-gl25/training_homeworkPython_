import struct
def byte_1(type:str)-> bytes:  # Rq(1 bit) + D(1 bit)(0 ) + rsvd(1 bit)(0-to user 1 -from user ? ) + Instance ID (4 bit)
    if type == "response" or type == 0:
        return b'\x80'
    if type == "request" or type == 1:
        return bytes([0x80 | 0x40])
    
def byte_2()-> bytes: # Hdr Ver (2 bit) + PLDM Type (6 bit)
    return b'\x02' 
def byte_3()-> bytes:  #PLDM Command Code = 1byte - address for command ?
    return b'\x04'
def completion_code(code: str) -> bytes:
    dict = { "SUCCESS": b'\x00'
            ,"ERROR": b'\x01'
            ,"ERROR_INVALID_DATA": b'\x02'
            ,"ERROR_INVALID_LENGTH": b'\x03'
            ,"ERROR_NOT_READY": b'\x04'
            ,"ERROR_UNSUPPORTED_PLDM_CMD": b'\x05'
            ,"ERROR_INVALID_PLDM_TYPE": b'\x20'
            ,"COMMAND_SPECIFIC": b'\x80'
            }
    
    return bytes(dict.get(code)) # SUCCESS, if need may create dict with base command like error (0x01) etc..

def heder()-> bytes: 
    return byte_1(1) + byte_2() + byte_3()

def generate_pldm(quntity_packs = 1, body = 127) -> bytes: #mb body = 8byte int? it possible to be 16 bit or more, but not in current case
    output = b""
    for i in range(quntity_packs):
        output += heder() +struct.pack('b',body) + completion_code("SUCCESS")
    
    return output
print(generate_pldm(1, 1))

def iter_and_return_bodyes(raw_binary: bytes) -> list[int]:
    list_bynary = []
    temp_byte = raw_binary
    while len(temp_byte) >= 4:
        if temp_byte[4:5] == completion_code():
            list_bynary.append(struct.unpack('b',temp_byte[3:4])[0])
            temp_byte = temp_byte[5:]
    return list_bynary

def parse_pldm(raw_binary: bytes):
    return iter_and_return_bodyes(raw_binary)


# print(parse_pldm(b'\x80\x02\x04\x0b\x00\x80\x02\x04\x0b\x00\x80\x02\x04\x0b\x00'))
# print(byte_1(1))
# print(type(byte_1(1)))
print(type(completion_code("SUCCESS")))
# print(heder())
print(byte_1(1))