from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str, mobile: str):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, mobile=mobile, status=status)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await  db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def select_user_by_mobile(mobile):
    user = await User.select('user_id').where(User.mobile == mobile).gino.first()
    return user

async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()

