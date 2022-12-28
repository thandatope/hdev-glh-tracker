from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import TimeRecord


def add_glh(sess: Session, name, date, duration):
    g = TimeRecord(session_name=name, session_date=date, session_duration=duration)
    sess.add(g)
    sess.commit()
    sess.refresh(g)
    return g


def get_glh_total(sess: Session):
    rows = sess.execute(select(TimeRecord.session_duration))
    total_glh = 0
    for row in rows:
        total_glh += row.session_duration
    return total_glh


def get_glh_records(sess: Session):
    rows = sess.query(TimeRecord).all()
    glh_list = []
    for row in rows:
        date_string = row.session_date.strftime("%d/%m/%Y")
        row_dict = {
                "id"              : row.id,
                "session_name"    : row.session_name,
                "session_date"    : date_string,
                "session_duration": row.session_duration
                }
        glh_list.append(row_dict)
    return glh_list


def update_glh_record(sess: Session, record_id, session_name, session_date, session_duration):
    record = sess.query(TimeRecord).where(TimeRecord.id == record_id).update(
            {"session_name": session_name, "session_date": session_date, "session_duration": session_duration},
            synchronize_session="fetch"
            )
    sess.commit()
    return record


def delete_glh_record(sess: Session, record_id):
    record = sess.query(TimeRecord).where(TimeRecord.id == record_id).delete(synchronize_session="fetch")
    sess.commit()
    return record
