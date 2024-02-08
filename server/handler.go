package AFS

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os/exec"
)

// PageData represents the data used in the template for rendering the page.
type PageData struct {
	ShowOutput bool
	Output     string
	Str        string
	// keyStr     string
}

// Handler handles the HTTP requests for the root path ("/").
func Handler(w http.ResponseWriter, r *http.Request) {
	// Check if the request path is not the root path
	if r.URL.Path != "/" {
		NotFoundHandler(w, r)
		return
	}

	// Handle GET requests
	if r.Method == "GET" {
		tmpl, err := template.ParseFiles("template/index.html")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		err = tmpl.Execute(w, nil)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
	}
	if r.Method == "POST" {
		// The stock ticker to pass to the Python script
		temp := r.PostFormValue("Email")
		var ticker string
		if temp != "" {
			ticker = temp
		} else {
			ticker = "TSLA"
		}
		// Define the command to run the Python script with the ticker as an argument
		cmd := exec.Command("python3", "python/get_data.py", ticker)

		// Execute the command
		output, err := cmd.CombinedOutput()
		if err != nil {
			log.Fatalf("Failed to execute command: %s\n", err, output)
		}
		tmpl, err := template.ParseFiles("template/index.html")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		err = tmpl.Execute(w, nil)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		fmt.Print("made stock call")
	}
}
