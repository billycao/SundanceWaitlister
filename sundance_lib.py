import requests

def SignUp(first_name,
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
  return r.text
