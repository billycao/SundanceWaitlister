import sys

import sundance_lib

def main(argv):
  print sundance_lib.SignUp(
      'test_first',
      'test_last',
      'my_sundance_email@mailinator.com',
      '91007',
      '123456')

if __name__ == '__main__':
  main(sys.argv)
