from converters import B8


# Operation Code Mnemonic
# Load 10h LOD
# Store 11h STO
# Add 20h ADD
# Subtract 21h SUB
# Add with Carry 22h ADC
# Subtract with Borrow 23h SBB
# Jump 30h JMP
# Jump If Zero 31h JZ
# Jump If Carry 32h JC
# Jump If Not Zero 33h JNZ
# Jump If Not Carry 34h JNC
# Halt FFh HLT

# instruction destination source
# LOD A,[1003h]


# Operation Code
LOD = B8(0x10)  # Load
STO = B8(0x11)  # Store
ADD = B8(0x20)  # Add
SUB = B8(0x21)  # Subtract
ADC = B8(0x22)  # Add with Carry
SBB = B8(0x23)  # Subtract with Borrow
JMP = B8(0x30)  # Jump
JZ  = B8(0x31)  # Jump If Zero 31h
JC  = B8(0x32)  # Jump If Carry 32h
JNZ = B8(0x33)  # Jump If Not Zero 33h
JNC = B8(0x34)  # Jump If Not Carry 34h
HLT = B8(0xFF)  # Halt


assert LOD == (0, 0, 0, 1, 0, 0, 0, 0)
assert STO == (0, 0, 0, 1, 0, 0, 0, 1)
assert ADD == (0, 0, 1, 0, 0, 0, 0, 0)
assert SUB == (0, 0, 1, 0, 0, 0, 0, 1)
assert ADC == (0, 0, 1, 0, 0, 0, 1, 0)
assert SBB == (0, 0, 1, 0, 0, 0, 1, 1)
assert JMP == (0, 0, 1, 1, 0, 0, 0, 0)
assert JZ  == (0, 0, 1, 1, 0, 0, 0, 1)
assert JC  == (0, 0, 1, 1, 0, 0, 1, 0)
assert JNZ == (0, 0, 1, 1, 0, 0, 1, 1)
assert JNC == (0, 0, 1, 1, 0, 1, 0, 0)
assert HLT == (1, 1, 1, 1, 1, 1, 1, 1)


def unpack(b0, b1, b2, b3, b4, b5, b6, b7):
    return b0, b1, b2, b3, b4, b5, b6, b7

x = B8(0xFF)
assert unpack(*x) == (1, 1, 1, 1, 1, 1, 1, 1)
assert unpack(*x) == (1, 1, 1, 1, 1, 1, 1, 1)
assert unpack(*HLT) == (1, 1, 1, 1, 1, 1, 1, 1)
