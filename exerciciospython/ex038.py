num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
if num1 > num2:
    print('O \033[34mPRIMEIRO\033[m valor é maior')
elif num2 > num1:
    print('O \033[34mSEGUNDO\033[m valor é maior')
else:
    print('Os valores são \033[34mIGUAIS\033[m!')
