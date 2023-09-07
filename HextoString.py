src = 0x534C43444E
hex_str = hex(src)  # 转换成十六进制字符串
hex_str = hex_str[2:] if hex_str.startswith('0x') else hex_str  # 去掉前缀 0x
bytes_data = bytes.fromhex(hex_str)  # 转换成字节串
str_data = ''.join(chr(byte) for byte in bytes_data)  # 将字节串转换成字符串
print(str_data)  # 输出 hello world


方法二：
src = "534C43444E"
str_data = bytes.fromhex(src).decode()
