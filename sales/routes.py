from flask import (request, render_template, redirect, url_for, Blueprint, flash, session)
from flask_login import (login_user,logout_user, login_required, current_user)
from werkzeug.security import check_password_hash, generate_password_hash
from sales.forms import SaleForm
from models import Tour, Client, Vendor, Sale, db
# from models import Sale

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/sales")
def list_sales():
    sales = Sale.query.all()
    return render_template("sales/sales_list.html", sales=sales)

@sales_bp.route("/sales/new", methods=["GET", "POST"])
def create_sale():
    form = SaleForm()

    form.tour_id.choices = [(t.id, t.name_tour) for t in Tour.query.all()]
    form.client_id.choices = [(c.id, c.name) for c in Client.query.all()]
    form.vendor1_id.choices = [(v.id, v.name) for v in Vendor.query.all()]
    form.vendor2_id.choices = form.vendor1_id.choices

    if form.validate_on_submit():
        sale = Sale(
            tour_id=form.tour_id.data,
            client_id=form.client_id.data,
            vendor1_id=form.vendor1_id.data,
            vendor2_id=form.vendor2_id.data,
            quantity=form.quantity.data,
            options_payment=form.options_payment.data,
            observations=form.observations.data
        )
        db.session.add(sale)
        db.session.commit()
        flash("Sale registered successfully", "success")
        return redirect(url_for("sales.list_sales"))  # Asegúrate de tener esta ruta
    return render_template("sales/sale_form.html", form=form)


@sales_bp.route('/sales/<int:id>/edit', methods=['GET', 'POST'])
def edit_sale(id):
    sale = Sale.query.get_or_404(id)
    form = SaleForm(obj=sale)

    form.tour_id.choices = [(t.id, t.name_tour) for t in Tour.query.all()]
    form.client_id.choices = [(c.id, c.name) for c in Client.query.all()]
    form.vendor1_id.choices = [(v.id, v.name) for v in Vendor.query.all()]
    form.vendor2_id.choices = form.vendor1_id.choices

    if form.validate_on_submit():
        sale.tour_id = form.tour_id.data
        sale.client_id = form.client_id.data
        sale.vendor1_id = form.vendor1_id.data
        sale.vendor2_id = form.vendor2_id.data
        sale.quantity = form.quantity.data
        sale.options_payment = form.options_payment.data
        sale.observations = form.observations.data
        db.session.commit()
        flash("Sale updated successfully", "info")
        return redirect(url_for("sales.list_sales"))
    
    return render_template("sales/sale_form.html", form=form)

@sales_bp.route('/sales/<int:id>/delete', methods=['GET'])
def delete_sale(id):
    sale = Sale.query.get_or_404(id)
    db.session.delete(sale)
    db.session.commit()
    flash("Sale deleted", "warning")
    return redirect(url_for('sales.list_sales'))