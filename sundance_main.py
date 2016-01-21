import sys

import sundance_lib

def main(argv):
  # TODO: Create multiple accounts, store into local gitignored json file.
  # TODO: Do some error printing here.
  # print sundance_lib.sign_up(
  #     'test_first',
  #     'test_last',
  #     'my_sundance_email_2@mailinator.com',
  #     '91007',
  #     '123456')

  my_session = sundance_lib.WaitlistSession()
  if not my_session.login('my_sundance_email@mailinator.com', '123456'):
    print "Invalid Login."
  link_code = my_session.get_link_code()

  my_session_2 = sundance_lib.WaitlistSession()
  if not my_session_2.login('my_sundance_email_2@mailinator.com', '123456'):
    print "Invalid Login."
  my_session_2.link_account(link_code)


if __name__ == '__main__':
  main(sys.argv)
