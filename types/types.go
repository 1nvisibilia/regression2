package types

type YahooStockData struct {
	Spark YahooSpark `json:"spark"`
}

type YahooSpark struct {
	Results []YahooResult `json:"results"`
}

type YahooResult struct {
	Response YahooResponse `json:"response"`
}

type YahooResponse struct {
	Timestamp []int          `json:"timestamp"`
	Indicator YahooIndicator `json:"indicators"`
}

type YahooIndicator struct {
	Quote []YahooQuote `json:"quote"`
}

type YahooQuote struct {
	Close []int `json:"close"`
}
