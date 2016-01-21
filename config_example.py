# EXAMPLE CONFIGURATION. RENAME TO config.py TO USE.

# This file defines configuration values for the Sundance Waitlister.

# If True, create the accounts. (This only needs to be done once)
CREATE_ACCOUNTS = False

# Number of account groups to manage.
NUM_ACCOUNT_GROUPS = 5

# Constant account parameters for each linked account.
# len(ACCOUNT_CONSTANTS) must equal NUM_LINKED_ACCOUNTS.
ACCOUNT_CONSTANTS = [
    {
      'first_name': 'Bob',
      'last_name': 'Smith',
      'zip_code': '12345',
      'password': 'password'
    }, {
      'first_name': 'Jane',
      'last_name': 'Doe',
      'zip_code': '12345',
      'password': 'password'
    }
]

# Email pattern to use to generate multiple accounts.
# Parameters from ACCOUNT_CONSTANTS can be used as well as
# %(account_group)d to indicate the account group number.
EMAIL_PATTERN = "%(first_name)s_sundance_%(account_group)d@mailinator.com"
