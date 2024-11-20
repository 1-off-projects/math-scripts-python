package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

type Rates struct {
	USD float64 `json:"USD"`
}

type Response struct {
	Rates Rates `json:"rates"`
}

func getConversionRate() (float64, error) {
	url := "https://api.exchangerate-api.com/v4/latest/EUR"
	resp, err := http.Get(url)
	if err != nil {
		return 0, err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return 0, err
	}

	var response Response
	err = json.Unmarshal(body, &response)
	if err != nil {
		return 0, err
	}

	return response.Rates.USD, nil
}

func main() {
	var euros float64
	fmt.Print("Enter amount in Euros: ")
	fmt.Scanf("%f", &euros)

	rate, err := getConversionRate()
	if err != nil {
		log.Fatalf("Failed to get conversion rate: %v", err)
	}

	usd := euros * rate
	fmt.Printf("%.2f Euros = %.2f USD\n", euros, usd)
}
