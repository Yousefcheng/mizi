er = input()  # 二进制
ba = input()  # 八进制
shi = input()  # 十进制
shiliu = input()  # 十六进制

er = int(er, 2)
ba = int(ba, 8)
shi = int(shi, 10)
shiliu = int(shiliu, 16)

m = max(er, ba, shi, shiliu)
print(f"{m:#b},{m:#o},{m:#d},{m:#x}")
