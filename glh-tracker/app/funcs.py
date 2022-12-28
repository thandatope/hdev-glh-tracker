import pandas
from sqlalchemy import create_engine
from io import BytesIO


def export_csv():
    csv_buffer = BytesIO()
    engine = create_engine("sqlite:///./glh.db")
    with engine.connect() as c:
        df = pandas.read_sql_table("time_record", c)
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        return csv_buffer
