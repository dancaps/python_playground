# Messing around with chatGPT

import openai
import keys


def main():
    openai.api_key = keys.key # Put you api key in a file. Not your code. 
    print("What would you like to ask ChatGPT? Enter [q] to quit.")
    while True:
        chat = input("<== You:     ")
        if chat.lower() == 'q':
            break
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=[{"role": "user", "content": chat}])
        print("==> ChatGPT: " + completion.choices[0].message.content)


if __name__ == '__main__':
    main()
