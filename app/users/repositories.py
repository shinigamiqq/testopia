from sqlalchemy import select

from app.db.repository import AlchemyRepository
from app.users.models import UserOrm
from app.users.schemas import UserRead


class UserRepository(AlchemyRepository[UserOrm, UserRead]):
    model_type = UserOrm
    schema_type = UserRead

    async def get_by_telegram_id(self, telegram_id: int) -> UserRead | None:
        stmt = select(UserOrm).where(UserOrm.telegram_id == telegram_id)  # noqa
        result = await self.session.scalar(stmt)
        if result is None:
            return None
        return self.schema_type.model_validate(result)
