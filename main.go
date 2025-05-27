package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("test")

	router := gin.Default()

	router.GET("/", func(c *gin.Context) {
		c.JSON(200, 565)
	})

	router.Run(":6001")
}
