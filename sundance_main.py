import sys

import config
import sundance_lib

def main(argv):
  # Create accounts.
  if config.CREATE_ACCOUNTS:
    for account_group in xrange(config.NUM_ACCOUNT_GROUPS):
      account_group_sessions = []
      for account in config.ACCOUNT_CONSTANTS:
        # Create accounts.
        account.update({
            'account_group': account_group,
        })
        email = config.EMAIL_PATTERN % account
        sundance_lib.sign_up(
            account['first_name'],
            account['last_name'],
            email,
            account['zip_code'],
            account['password'])
        # Click mailinator confirmation email.
        if not sundance_lib.confirm_mailinator_email(email):
          print 'Error confirming email %s' % email
        else:
          print 'Created account: %s' % email
        # Sign in and save session.
        session = sundance_lib.WaitlistSession()
        session.login(email, account['password'])
        account_group_sessions.append(session)
      # Link odd accounts with even accounts.
      for index, odd_session in enumerate(account_group_sessions[1::2]):
        link_code = odd_session.get_link_code()
        even_session = account_group_sessions[index * 2]
        even_session.link_account(link_code)

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
