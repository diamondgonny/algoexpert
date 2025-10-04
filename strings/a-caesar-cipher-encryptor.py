def caesarCipherEncryptor(string, key):
    new_string = ""
    for c in string:
        n = 97 + (((ord(c) + key) - 97) % 26)
        new_string += chr(n)
    return new_string

# a: 97, z: 122(ascii)
# 파이썬의 문자열은 변경 불가능(immutable)한 객체이므로,
# c의 값을 변경하더라도 원본 문자열에는 영향을 주지 않습니다.
# 만약 문자열을 변경하려면 새로운 문자열을 생성해야 합니다.
