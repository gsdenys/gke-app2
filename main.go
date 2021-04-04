package main

import (
	"fmt"
	"net/http"
)

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "C'est l'application 2 - kustomize")
}

func setupRoutes() {
	http.HandleFunc("/", homePage)
}

func main() {
	fmt.Println("Application Web démarrée sur le port 3000")
	setupRoutes()
	http.ListenAndServe(":3000", nil)
}
