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
      # for index, odd_session in enumerate(account_group_sessions[1::2]):
      #   print index
      #   print odd_session.email
      #   print even_session.email
      #   link_code = odd_session.get_link_code()
      #   even_session = account_group_sessions[index * 2]
      #   even_session.link_account(link_code)

  # Register for e-waitlist.
  for account_group in xrange(config.NUM_ACCOUNT_GROUPS):
    # Sign in.
    for account in config.ACCOUNT_CONSTANTS:
        account.update({
            'account_group': account_group,
        })
        email = config.EMAIL_PATTERN % account
        # Log in.
        session = sundance_lib.WaitlistSession()
        if not session.login(email, account['password']):
          print "Could not login with '%s':'%s'." % (
              email, account['password'])
          continue
        for movie_id in config.MOVIE_IDS:
          session.waitlist(movie_id)


if __name__ == '__main__':
  main(sys.argv)
