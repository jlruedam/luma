from flask import render_template, redirect, url_for, flash, Blueprint
from agencies.forms import AgencyForm
from models import db, Agency

agencies_bp = Blueprint("agencies", __name__)


# List agencies
@agencies_bp.route('/agencies')
def list_agencies():
    agencies = Agency.query.all()
    return render_template('agencies/agencies.html', agencies=agencies)

# Create agency
@agencies_bp.route('/agencies/new', methods=['GET', 'POST'])
def create_agency():
    form = AgencyForm()
    if form.validate_on_submit():
        agency = Agency(
            nit=form.nit.data,
            name_agency=form.name_agency.data,
            email_agency=form.email_agency.data,
            tel_agency=form.tel_agency.data,
            contact=form.contact.data
        )
        db.session.add(agency)
        db.session.commit()
        flash('Agency created successfully', 'success')
        return redirect(url_for('agencies.list_agencies'))
    return render_template('agencies/agency_form.html', form=form)

# Edit agency
@agencies_bp.route('/agencies/<int:id>/edit', methods=['GET', 'POST'])
def edit_agency(id):
    agency = Agency.query.get_or_404(id)
    form = AgencyForm(obj=agency)
    if form.validate_on_submit():
        agency.nit = form.nit.data
        agency.name_agency = form.name_agency.data
        agency.email_agency = form.email_agency.data
        agency.tel_agency = form.tel_agency.data
        agency.contact = form.contact.data
        db.session.commit()
        flash('Agency updated successfully', 'info')
        return redirect(url_for('agencies.list_agencies'))
    return render_template('agencies/agency_form.html', form=form)

# Delete agency
@agencies_bp.route('/agencies/<int:id>/delete')
def delete_agency(id):
    agency = Agency.query.get_or_404(id)
    db.session.delete(agency)
    db.session.commit()
    flash('Agency deleted', 'warning')
    return redirect(url_for('agencies.list_agencies'))