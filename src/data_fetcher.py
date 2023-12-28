import requests

headers = {
    "User-Agent": "..."
}

base_url = "https://query1.finance.yahoo.com/v7/finance/spark?"

def generateUrl(options: dict):
    params = ""
    for key in options:
        params += (key + "=" + options[key] + "&")
    return base_url + params

def fetch_stock(abbr: str, range: str, interval: str = "2m"):
    options = {
        "symbols": abbr,
        "range": range,
        "interval": interval
    }

    data = requests.get(generateUrl(options), headers=headers).json()

    timestamps: str = data["spark"]["result"][0]["response"][0]["timestamp"]
    prices: str = data["spark"]["result"][0]["response"][0]["indicators"]["quote"][0]["close"]

    # the scaling by 1000 is needed since yahoo API returns the official timestamps/1000.
    return list(map(lambda x: { "ts": x[0] * 1000, "price": x[1] }, (zip(timestamps, prices))))
