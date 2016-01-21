import sys

import sundance_lib

def main(argv):
  # TODO: Create multiple accounts, store into local gitignored json file.
  # TODO: Do some error printing here.
  email = 'email_3@mailinator.com'
  sundance_lib.sign_up(
      'test_first',
      'test_last',
      email,
      '91007',
      '123456')

  # sundance_lib.confirm_mailinator_email(email)

  # Create an account group

  # my_session = sundance_lib.WaitlistSession()
  # if not my_session.login('my_sundance_email@mailinator.com', '123456'):
  #   print "Invalid Login."
  # link_code = my_session.get_link_code()

  # my_session_2 = sundance_lib.WaitlistSession()
  # if not my_session_2.login('my_sundance_email_2@mailinator.com', '123456'):
  #   print "Invalid Login."
  # my_session_2.link_account(link_code)

if __name__ == '__main__':
  main(sys.argv)
