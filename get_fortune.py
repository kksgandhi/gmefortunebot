import requests

FORTUNE_URL  = 'https://helloacm.com/api/fortune'
NUM_FORTUNES = 5

api_responses = [requests.get(FORTUNE_URL) for _ in range(NUM_FORTUNES)]
fortunes      = map(lambda req: req.json(), api_responses)

for index, fortune in enumerate(fortunes):
    print(f"{index + 1}: {fortune}")
