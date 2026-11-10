import os
import random

import pytest
from sqlalchemy import MetaData, Table, create_engine

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:123456@localhost:5432/QA",
)


@pytest.fixture
def engine():
    engine = create_engine(DATABASE_URL)
    yield engine
    engine.dispose()


@pytest.fixture
def student_table(engine):
    """Отражаем таблицу student из реальной схемы БД."""
    meta = MetaData()
    return Table("student", meta, autoload_with=engine)


def _generate_free_user_id(engine, student_table) -> int:
    """Подбирает user_id в диапазоне integer, не занятый в базе."""
    for _ in range(10):
        user_id = random.randint(1_000_000_000, 2_100_000_000)
        with engine.connect() as conn:
            row = conn.execute(
                student_table.select().where(
                    student_table.c.user_id == user_id
                )
            ).fetchone()
        if row is None:
            return user_id
    raise RuntimeError("Не удалось подобрать свободный user_id")


@pytest.fixture
def created_student_id(engine, student_table):
    """Создаёт запись со свободным user_id и удаляет её после теста."""
    user_id = _generate_free_user_id(engine, student_table)

    with engine.begin() as conn:
        conn.execute(
            student_table.insert()
            .values(
                user_id=user_id,
                level="Pre-Intermediate",
                education_form="group",
                subject_id=1,
            )
        )

    yield user_id

    with engine.begin() as conn:
        conn.execute(
            student_table.delete().where(student_table.c.user_id == user_id)
        )
