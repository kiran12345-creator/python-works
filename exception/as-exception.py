# try:
#     num=int(input('enter a number'))
#     if num<=0:
#         raise ValueError('number must be positive')
#     else:
#         print(num)
# except ValueError as v:
#     print(v)
#
#------------------------------------------------------------------------------------------------------------
# class InvalidPasswordError(Exception):
#     pass
# try:
#     password=input('enter password')
#     if len(password)<=8:
#         raise InvalidPasswordError('password should be of 8 characters or more')
#     else:
#         print('password accepted')
# except InvalidPasswordError:
#   print(  'password invalid')
class InsufficentBalanceError(Exception):
    pass
try:
    balance=1000
    amount=int(input('enter amount to withdraw'))
    if amount>balance:
        raise InsufficentBalanceError('not enough balance')
    else:
        balance -= amount
        print('balance is ', balance)
except InsufficentBalanceError:
    print('not enough balance')


