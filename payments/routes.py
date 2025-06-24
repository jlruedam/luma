from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db, Payment, Sale
from payments.forms import PaymentForm

payments_bp = Blueprint("payments", __name__, template_folder="templates/payments")

@payments_bp.route("/payments")
def list_payments():
    payments = Payment.query.all()
    return render_template("payments/payments.html", payments=payments)


@payments_bp.route("/payments/new", methods=["GET", "POST"])
def create_payment():
    form = PaymentForm()
    form.id_sale.choices = [(s.id, f"Sale #{s.id}") for s in Sale.query.all()]

    if form.validate_on_submit():
        payment = Payment(
            id_sale=form.id_sale.data,
            value=form.value.data
        )
        db.session.add(payment)
        db.session.commit()
        flash("Payment successfully created", "success")
        return redirect(url_for("payments.list_payments"))
    
    return render_template("payments/payment_form.html", form=form)


@payments_bp.route("/payments/<int:id>/edit", methods=["GET", "POST"])
def edit_payment(id):
    payment = Payment.query.get_or_404(id)
    form = PaymentForm(obj=payment)
    form.id_sale.choices = [(s.id, f"Sale #{s.id}") for s in Sale.query.all()]

    if form.validate_on_submit():
        form.populate_obj(payment)
        db.session.commit()
        flash("Payment updated", "info")
        return redirect(url_for("payments.list_payments"))
    
    return render_template("payments/payment_form.html", form=form)

@payments_bp.route("/payments/<int:id>/delete", methods=["GET"])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    flash("Payment deleted", "warning")
    return redirect(url_for("payments.list_payments"))