package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/30Piraten/app/src/mirrors"
)

type response struct {
	FastestURL string        `json:"fastest_url"`
	Latency    time.Duration `json:"latency"`
}

func main() {
	http.HandleFunc("/fastest-mirror", func(w http.ResponseWriter, r *http.Request) {
		response := findFastest(mirrors.MirrorList[:])
		responseJSON, _ := json.Marshal(response)

		w.Header().Set("Content-Type", "application/json")
		w.Write(responseJSON)
	})

	port := ":1234"
	server := &http.Server{
		Addr:           port,
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}

	fmt.Printf("Server trekking on port %s\n", port)
	log.Fatal(server.ListenAndServe())
}

func findFastest(urls []string) response {
	urlChannel := make(chan string)
	latencyChannel := make(chan time.Duration)

	for _, url := range urls {
		mirrorURL := url
		go func() {
			start := time.Now()
			_, err := http.Get(mirrorURL + "/README")
			latency := time.Since(start) / time.Millisecond
			if err == nil {
				urlChannel <- mirrorURL
				latencyChannel <- latency
			}
		}()
	}
	return response{<-urlChannel, <-latencyChannel}
}
