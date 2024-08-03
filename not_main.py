import requests
import configuration


TOKEN = configuration.TELEGRAM_API_TOKEN

def main():
    params = {}
    r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe")
    print(r.json())

    update = requests.get("https://api.telegram.org/bot{TOKEN}/getUpdates")
    print(update.json())

    # msg = requests.post(
    #     url=f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    #     params="chat_id=@ArnasBot&text=Labas%20Arnai"
    # )
    # print(msg.json())
    return 0



if __name__ == "__main__":
    main()