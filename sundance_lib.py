import re
import requests
import time

def sign_up(first_name,
            last_name,
            email,
            zip_code,
            password):
  # Create POST request.
  payload = {
    'data[User][first_name]': first_name,
    'data[User][last_name]': last_name,
    'data[User][username]': email,
    'data[User][postal]': zip_code,
    'data[User][password]': password,
    'data[User][confirm_password]': password,
    'data[User][agree]': 1,
  }
  r = requests.post(
      'https://ewaitlist.sundance.org/register', data=payload)
  # TODO(billycao): Add error handling here.
  return r.text


def confirm_mailinator_email(email):
  email_username = email[0:email.index('@')]
  # Get email ID, with retries.
  num_retries = 15
  for retry_num in xrange(num_retries):
    inbox_response = requests.get(
        'http://mailinator.com/api/webinbox?to=%s' % email_username)
    try:
      if len(inbox_response.json()['messages']) > 0:
        break
      else:
        if retry_num == num_retries - 1:
          return False
    except ValueError as e:
      pass
    time.sleep(2)
  # Get email contents.
  email_id = inbox_response.json()['messages'][0]['id']
  email_response = requests.get(
      'http://mailinator.com/rendermail.jsp?msgid=%s' % email_id)
  # Search for Sundance confirm link.
  match = re.search(
      '(http://ewaitlist.sundance.org/account/confirm/[a-z0-9]+)',
      email_response.text)
  # Visit confirmation email.
  if match:
    requests.get(match.groups()[0])
    return True
  else:
    return False


class WaitlistSession(object):
  def __init__(self):
    self.session = requests.Session()
    self.email = ''
      
  def login(self, email, password):
    payload = {
      'data[User][username]': email,
      'data[User][password]': password,
    }
    response = (
        self.session.post(
          'https://ewaitlist.sundance.org/login', data=payload))
    if "Invalid email or password" in response.text:
      return False
    self.email = email
    return True

  def get_link_code(self):
    headers = {
      'X-Requested-With': 'XMLHttpRequest',
    }
    response = self.session.post(
        'https://ewaitlist.sundance.org/account/code', headers=headers)
    return response.text

  def link_account(self, link_code):
    payload = {
      'data[code]': link_code,
    }
    response = self.session.post(
        'https://ewaitlist.sundance.org/account/link', data=payload)

  # TODO: Implement linked accounts functionality. 
  def waitlist(self, movie_id):
    state = 'join'
    while True:
      print "Waitlisting for movie %d with email %s." % (
          movie_id, self.email)
      response = self.session.get(
          'https://ewaitlist.sundance.org/api/waitlist/%d/%s' % (
              movie_id, state),
          allow_redirects=False)
      if 'queued' in response.text:
        print "Queued, retrying with new state" 
        state = 'check'
      elif ('overload' in response.text or
          'pending' in response.text or
          'join_invalid' in response.text):
        print "Received %s, retrying..." % response.text
        state = 'join'
        time.sleep(1)
      else:
        print "Successfully waitlisted for movie %d with email %s: %s." % (
            movie_id, self.email, response.text)
        return True
