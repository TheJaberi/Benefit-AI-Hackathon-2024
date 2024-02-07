package AFS

import (
	"context"
	"fmt"

	openai "github.com/sashabaranov/go-openai"
)

func OpenAI(str string) {
	client := openai.NewClient("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")
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: openai.GPT3Dot5Turbo,
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: str,
				},
			},
		},
	)
	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}
