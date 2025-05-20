from flask import Blueprint, render_template, Response

from io import StringIO
import csv

from .models import Household

household_bp = Blueprint('household', __name__)


@household_bp.route('/households')
def list_households():
    households = Household.query.all()
    return render_template('household_list.html', households=households)


@household_bp.route('/households/export')
def export_households_csv():
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['head_name', 'contact_phone', 'address', 'eligibility_status', 'member_count'])
    for h in Household.query.all():
        writer.writerow([h.head_name, h.contact_phone, h.address, h.eligibility_status, h.member_count])
    output = si.getvalue()
    return Response(
        output,
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=households.csv'}
    )
