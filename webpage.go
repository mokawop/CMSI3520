package main
import(
	"fmt"
	"io"
	"net/http"
	"os"
)

func main(){
	url := os.Args[1]
	resp, err := http.Get(url)

	if err != nil{
		fmt.Println("URL not found")
		os.Exit(1)
	}

	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
    if err != nil {
        fmt.Println("Error reading body:", err)
		return
    }
    bodyString := string(bodyBytes)
    fmt.Println(bodyString)
}