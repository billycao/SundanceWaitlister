import sys

import sundance_lib

def main(argv):
  # TODO: Create multiple accounts, store into local gitignored json file.
  # TODO: Do some error printing here.
  # print sundance_lib.sign_up(
  #     'test_first',
  #     'test_last',
  #     'my_sundance_email@mailinator.com',
  #     '91007',
  #     '123456')

  my_session = sundance_lib.WaitlistSession()
  if not my_session.login('my_sundance_email@mailinator.com', '123456'):
    print "Invalid Login."

if __name__ == '__main__':
  main(sys.argv)
