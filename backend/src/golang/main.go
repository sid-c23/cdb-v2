package main

import (
	"database/sql"
	"fmt"
	"strconv"
	"strings"
	"unicode/utf8"

	_ "github.com/mattn/go-sqlite3"
)

type ClubData struct {
	Link        string `json:"link"`
	Name        string `json: "name"`
	Description string `json: "description"`
}

var indexMap map[string]map[int]ClubData

func main() {
	db, err := sql.Open("sqlite3", "../db.sqlite3")
	if err != nil {
		panic(err)
	}
	rows, err := db.Query("SELECT id, name, description FROM clubs_Club")
	if err != nil {
		panic(err)
	}
	indexMap = make(map[string]map[int]ClubData)
	defer rows.Close()
	var uid int
	var name string
	var description string
	for rows.Next() {
		err = rows.Scan(&uid, &name, &description)
		if err != nil {
			panic(err)
		}
		name = strings.ToLower(name)
		description = strings.ToLower(description)
		clubLink := "http://localhost:8000/api/clubs/" + strconv.Itoa(uid) + "/"
		nameNgrams := makeNGrams(name)
		descNgrams := makeNGrams(description)
		for _, nGram := range nameNgrams {
			if _, val := indexMap[nGram]; val {
				indexMap[nGram][uid] = ClubData{Link: clubLink, Name: name, Description: description}
			} else {
				indexMap[nGram] = make(map[int]ClubData)
				indexMap[nGram][uid] = ClubData{Link: clubLink, Name: name, Description: description}
			}
		}
		for _, nGram := range descNgrams {
			if _, val := indexMap[nGram]; val {
				indexMap[nGram][uid] = ClubData{Link: clubLink, Name: name, Description: description}
			} else {
				indexMap[nGram] = make(map[int]ClubData)
				indexMap[nGram][uid] = ClubData{Link: clubLink, Name: name, Description: description}
			}
		}
	}
	fmt.Println(search("Sci Oly"))
	fmt.Println(search("scienc olympia"))
}

func search(query string) map[int]ClubData {
	query = strings.ToLower(query)
	queryNgrams := makeNGrams(query)
	res := make(map[int]ClubData)
	for _, q := range queryNgrams {
		if _, val := indexMap[string(q)]; val {
			for id, club := range indexMap[string(q)] {
				res[id] = club
			}
		} else {
			fmt.Println("Error!")
		}
	}
	return res
}

func makeNGrams(sentence string) []string {
	words := strings.Split(strings.Trim(sentence, "!.,? "), " ")
	var Ngrams []string
	minLen := 3
	//maxLen := 6
	for _, word := range words {
		if _, ok := StopWordsMap[word]; ok {
			continue
		} else {
			// turn word into rune
			useWord := []rune(word)
			length := utf8.RuneCountInString(word)
			for i := minLen; i <= length; i++ {
				ngram := string(useWord[0:i])
				Ngrams = append(Ngrams, ngram)
			}
		}
	}
	return Ngrams
}
