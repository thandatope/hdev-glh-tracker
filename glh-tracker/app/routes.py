from flask import current_app as app
from flask import render_template, g, request, redirect, url_for, flash, send_file
import datetime
from .database import get_db
from .crud import get_glh_total, add_glh, get_glh_records, update_glh_record, delete_glh_record
from .funcs import export_csv


@app.route("/", methods=["GET"])
def index():
    with get_db() as c:
        current_minutes = get_glh_total(c)
        h, m = int(current_minutes / 60), current_minutes % 60
        table_data = get_glh_records(c)
        return render_template(
                "main.html",
                current_hours=h,
                current_minutes=m,
                table_data=table_data
                )


@app.route("/add", methods=["POST"])
def add_record():
    with get_db() as c:
        glh_dict = request.form.to_dict()
        session_date = datetime.datetime.strptime(glh_dict["session-date"], "%Y-%m-%d").date()
        add_glh(sess=c, name=glh_dict["session-name"], date=session_date, duration=glh_dict["session-duration"])
        flash({"title": "", "message": "Session added!"}, "success")
        return redirect(url_for("index"))


@app.route("/edit", methods=["POST"])
def edit_record():
    with get_db() as c:
        glh_dict = request.form.to_dict()
        session_date = datetime.datetime.strptime(glh_dict["session-date"], "%Y-%m-%d").date()
        num_updated = update_glh_record(
            c, glh_dict["record-id"], glh_dict["session-name"], session_date,
            glh_dict["session-duration"]
            )
        flash({"title": "", "message": f"{num_updated} record updated!"}, "success")
        return redirect(url_for("index"))


@app.route("/delete", methods=["POST"])
def delete_record():
    with get_db() as c:
        glh_dict = request.form.to_dict()
        num_deleted = delete_glh_record(c, glh_dict["item-id"])
        flash({"title": "", "message": f"{num_deleted} record deleted!"}, "success")
        return redirect(url_for("index"))


@app.route("/export/csv")
def get_csv():
    csv_file = export_csv()
    flash({"title": "", "message": "glh.xlsx exported!"}, "success")
    return send_file(csv_file, as_attachment=True, download_name="glh.csv")


@app.template_filter("jsdateformat")
def js_date_format(value):
    in_format = "%d/%m/%Y"
    out_format = "%Y-%m-%d"

    if value is None:
        return ""
    else:
        d = datetime.datetime.strptime(value, in_format)
    return d.strftime(out_format)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_db", None)
    if db is not None:
        db.close()
