from mailtm import MailTM
import asyncio
from bs4 import BeautifulSoup


async def main() -> str:
    password = "HT9D24[n"
    email = "mojeidre1@hldrive.com"
    mailtm = MailTM()
    try:
        await mailtm.get_account(email, password)
    except:
        pass
    token = await mailtm.get_account_token(email, password)
    # account = await mailtm.get_account_by_id(token.id, token.token)
    messages = await mailtm.get_messages(token.token, page=1)
    # me = await mailtm.get_me(token.token)
    message = await mailtm.get_message_by_id(messages.hydra_member[0].id, token.token)

    soup = BeautifulSoup(message.html[0], 'html.parser')


    strong_tags = soup.find_all('strong')
    strong_text_list = [strong.get_text() for strong in strong_tags]

    return strong_text_list[1]


if __name__ == "__main__":
    asyncio.run(main())

