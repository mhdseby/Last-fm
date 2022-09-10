import json, requests, requests_cache, time
from IPython.display import clear_output

API_KEY = 'a1a1d92e3243c539fdd8b9e9bd6cf200'
USER_AGENT = 'mhdseby'

requests_cache.install_cache()

def lastfm_get(payload):
    headers = {
        'user-agent' : USER_AGENT
    }
    url = 'https://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = API_KEY
    payload['method'] = 'chart.gettopartists'
    payload['format'] = 'json'
    payload['method'] = 'chart.gettopartists'


    response = requests.get(url, headers=headers, params=payload)
    return response


payload = { }

r = lastfm_get(payload)
print(r.status_code)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



# -------------------

# initialize list for results
results = []

# set initial page and a high total number
page = 1
total_pages = 99999


while page <= total_pages:
    # simplified request code for this example
    payload["page"] = page
    payload["limit"] = 500

    print("Requesting page {}/{}.".format(page,total_pages))

    re = lastfm_get(payload)

    clear_output(True)

    # append results to list
    results.append(re.json())
    print(page)
    # increment page
    page += 1

    if not getattr(re, 'from_cache', False):
        time.sleep(0.25)

print(results)