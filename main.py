from fastapi import FastAPI
from utils.db_api.db_gino import db
from data import config
from handlers import send_verify_code
import phonenumbers

from utils.db_api import quick_commands as commands

app = FastAPI(
    title="my app"
)


@app.post("/api/v01/code")
async def change_user_name(mobile: str, verify_code: int):
    await db.set_bind(config.POSTGRES_URI)

    # привеодим телефончик, который пришел от Blitz, к виду, в котором он записан в БД нашего приложения
    my_number = phonenumbers.parse(mobile, "RU")
    mobile = phonenumbers.format_number(my_number, phonenumbers.PhoneNumberFormat.E164)

    user = await commands.select_user_by_mobile(mobile)
    if user is not None:
        msg = "Используйте код на login.mos.ru, не передавайте никому: " + str(verify_code)
        if await send_verify_code.ss(user[0], msg) == 200:
            return {"status": 200, "data": "OK"}
        else:
            return {"status": 200, "data": "Failed. Something goes wrong"}
    else:
        return {"status": 404, "data": "Failed. User not found"}



