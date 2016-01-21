import requests

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
  r = requests.post('https://ewaitlist.sundance.org/register', data=payload)
  # TODO(billycao): Add error handling here.
  return r.text


class WaitlistSession(object):
  def __init__(self):
    self.session = requests.Session()
      
  def login(self, email, password):
    payload = {
      'data[User][username]': email,
      'data[User][password]': password,
    }
    response = (
        self.session.post('https://ewaitlist.sundance.org/login', data=payload))
    if "Invalid email or password" in response.text:
      return False
    return True

  def get_link_code(self):
    headers = {
      'X-Requested-With': 'XMLHttpRequest',
    }
    response = self.session.post('https://ewaitlist.sundance.org/account/code', headers=headers)
    return response.text

  def link_account(self, link_code):
    payload = {
      'data[code]': link_code,
    }
    response = self.session.post('https://ewaitlist.sundance.org/account/link', data=payload)
