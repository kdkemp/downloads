''' This script calls the Neocities API and retrieves your website viewcount then generates a HTML string that you can paste onto your page. Unfortunately, this is one of the only working options for a stable website view counter that does not rely on an external server or service like Cloudflare. The number images reference a folder structure noted below, so be sure to use the same structure or update the URL path. The images are linked in this repository. Please do not hotlink! '''

import urllib.request
import json
import ssl
 
username = "YOUR_NEOCITIES_USERNAME" # Update with your Neocities username
url = f"https://neocities.org/api/info?sitename={username}"
 
certificate = ssl.create_default_context()
try:
    certificate.load_verify_locations("/etc/ssl/cert.pem")  # Mac
except (FileNotFoundError, ssl.SSLError):
    try:
        import certifi
        certificate.load_verify_locations(certifi.where())  # Windows (requires: pip install certifi)
    except ImportError:
        certificate = ssl._create_unverified_context()
 
with urllib.request.urlopen(url, context=certificate) as r:
    data = json.loads(r.read())
 
view_count = list(str(data['info']['views']))
number_string = ""
for i, digit in enumerate(view_count):
    number_string += f'<img src="./../img/counter/c{digit}.gif"/>' # Update this URL path for your counter images
    if (len(view_count) - 1 - i) % 3 == 0 and (len(view_count) - 1 - i) != 0:
        number_string += ","
 
print(f'<p>You are visitor # {number_string}</p>')
