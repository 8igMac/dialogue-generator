import json
import os
from revChatGPT.ChatGPT import Chatbot


def fake_response() -> dict:
    response = {
        "message": """小美： 你好，我想問一下退貨的問題。

小王： 你好，小美。我很樂意為你解答退貨問題。你可以告訴我退貨的原因嗎？

小美： 我購買的商品是破損的。

小王： 對不起，這種情況下我們會為你提供退貨服務。請告訴我你的訂單號碼，我會為你處理退貨流程。

小美： 訂單號碼是12345678。

小王： 謝謝你提供訂單號碼。我會立即為你處理退貨流程。請注意，退貨的商品必須是未使用的，並且保持原來的包裝。你需要提供退貨的原因，並且附上原始的發票。你需要在14天內完成退貨。請問你有其他問題嗎？

小美： 沒有了，謝謝你的幫助。

小王： 不客氣，小美。我很高興能為你提供幫助。如果你有其他問題，歡迎隨時與我聯繫。""",
        "conversation_id": "...",
        "parent_id": "..."
    }
    return response


def parse_response(response: dict):
    """
    response is a dictionary;

    {
        "message": "...",
        "conversation_id": "...",
        "parent_id": "..."
    }
    """
    message = response["message"]
    dialog = {"log": []}

    for msg in message.splitlines():
        # ChatGPT will have newline at the eng of each turn.
        if msg != "":
            dialog["log"].append(msg)
    return dialog


def write_dialog_to_file(dialog: dict):
    """
    Output format:

    {
        "log": [
            {
                "text": "...",
                "metadata": {}
            },
            {
                "text": "...",
                "metadata": {}
            },
        ]
    }
    """
    if not os.path.exists("data"):
        os.makedirs("data")
    with open("data/data.json", "w") as f:
        json.dump(dialog, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    chatbot = Chatbot(config)
    msg = "你好幫我產生一個客服對話，請使用繁體中文，客戶的名子是小美，客服的名子是小王"
    response = chatbot.ask(msg)

    # Parse response.
    dialog = parse_response(response)

    # Write dialogue to file.
    write_dialog_to_file(dialog)
