from conftest import _generate_free_user_id


def _get_student_by_id(engine, student_table, user_id):
    with engine.connect() as conn:
        row = conn.execute(
            student_table.select().where(
                student_table.c.user_id == user_id
            )
        ).fetchone()
    return row


def test_add_student(engine, student_table):
    """Позитивный: запись добавляется и читается обратно."""
    user_id = _generate_free_user_id(engine, student_table)
    level = "Elementary"
    education_form = "personal"
    subject_id = 1

    with engine.begin() as conn:
        conn.execute(
            student_table.insert()
            .values(
                user_id=user_id,
                level=level,
                education_form=education_form,
                subject_id=subject_id,
            )
        )

    try:
        row = _get_student_by_id(engine, student_table, user_id)
        assert row is not None, "Запись не найдена после добавления"
        assert row.level == level
        assert row.education_form == education_form
        assert row.subject_id == subject_id
    finally:
        with engine.begin() as conn:
            conn.execute(
                student_table.delete().where(
                    student_table.c.user_id == user_id
                )
            )


def test_update_student(engine, student_table, created_student_id):
    """Позитивный: уровень и форма обучения обновляются и читаются обратно."""
    new_level = "Advanced"
    new_education_form = "group"

    with engine.begin() as conn:
        conn.execute(
            student_table.update()
            .where(student_table.c.user_id == created_student_id)
            .values(
                level=new_level,
                education_form=new_education_form,
            )
        )

    row = _get_student_by_id(engine, student_table, created_student_id)
    assert row is not None, "Запись пропала после обновления"
    assert row.level == new_level
    assert row.education_form == new_education_form


def test_delete_student(engine, student_table, created_student_id):
    """Позитивный: запись удаляется и больше не читается."""
    row_before = _get_student_by_id(
        engine, student_table, created_student_id
    )
    assert row_before is not None, "Фикстура не создала запись"

    with engine.begin() as conn:
        conn.execute(
            student_table.delete().where(
                student_table.c.user_id == created_student_id
            )
        )

    row_after = _get_student_by_id(engine, student_table, created_student_id)
    assert row_after is None, "Запись всё ещё в базе после удаления"
