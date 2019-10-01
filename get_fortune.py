import requests
from config import *

api_responses = [requests.get(FORTUNE_URL) for _ in range(NUM_FORTUNES)]
fortunes      = list(map(lambda req: req.json(), api_responses))

for index, fortune in enumerate(fortunes):
    print(f"{index + 1}: {fortune}")

choice = int(input()) - 1

print(fortunes[choice])
