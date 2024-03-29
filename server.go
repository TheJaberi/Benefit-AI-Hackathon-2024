package main

import (
	"fmt"
	"log"
	"net/http"

	webart "AFS/server"
)

func main() {
	// webart.OpenAI("Hello, I'm a chatbot.")
	// with above code you can call the OpenAI function from the api.go file

	// Set up HTTP request handlers for different paths
	http.HandleFunc("/css/", webart.CSSHandler) // Handler for serving CSS files
	http.HandleFunc("/", webart.Handler)        // Handler for the root path ("/")
	// http.HandleFunc("/grader", webart.FormHandler) // Handler for the "/ascii-art" path

	// Start the HTTP server
	fmt.Println("Server listening on port http://localhost:8080 ...")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal(err)
	}
}
