# Block No 99997
# Block Bits 453281356
# Difficulty 14,484.16

_bits = input("* block's BITS ? : ");

hexBits = hex(int(_bits));
_hexHead = hexBits[:4];
_hexTail = '0x'+hexBits[4:];

print("- BITS in hexadecimal     : ", hexBits);
print("                            ", _hexHead);
print("                            ", _hexTail);

# print hex(int("0xAD4", 16) + int("0x200", 16)) # 0xcd4
max_difficulty = hex(0x00000000FFFF0000000000000000000000000000000000000000000000000000);
cur_difficulty = hex(int(_hexTail, 16)*2**(8*(int(_hexHead, 16)-3)));

print("- maximum difficulty      : ", max_difficulty);
print("- this block's difficulty : ", cur_difficulty);
print("- this block's NONCE      : ", (int(max_difficulty, 16)/int(cur_difficulty, 16))); 
