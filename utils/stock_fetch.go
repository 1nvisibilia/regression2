package stock_fetch

import (
	"encoding/json"
	"log"
	"net/http"
	"net/url"

	"github.com/1nvisibilia/regression2/types"
)

const BASE_URL = "https://query1.finance.yahoo.com/v7/finance/spark?"

func fetch_stock(symbols string, time_range string, interval string) {
	client := &http.Client{}

	u, err := url.Parse(BASE_URL)

	if err != nil {
		log.Fatal(err)
	}

	q := u.Query()
	q.Set("symbols", symbols)
	q.Set("range", time_range)
	q.Set("interval", interval)
	u.RawQuery = q.Encode()

	req, err := http.NewRequest("GET", u.String(), nil)

	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("User-Agent", "...")
	req.Header.Set("Accept", "application/json")

	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}

	defer resp.Body.Close()

	var stockData types.YahooStockData

	if err := json.NewDecoder(resp.Body).Decode(&stockData); err != nil {
		log.Fatal("Error decoding JSON:", err)
	}
}
