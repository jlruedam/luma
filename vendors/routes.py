from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db, Vendor
from vendors.forms import VendorForm

vendors_bp = Blueprint("vendors", __name__, template_folder="templates/vendors")

@vendors_bp.route("/vendors")
def list_vendors():
    vendors = Vendor.query.all()
    return render_template("vendors/vendors.html", vendors=vendors)


@vendors_bp.route("/vendors/new", methods=["GET", "POST"])
def create_vendor():
    form = VendorForm()
    if form.validate_on_submit():
        vendor = Vendor(
            type_doc=form.type_doc.data,
            num_doc=form.num_doc.data,
            name=form.name.data,
            tel=form.tel.data,
            email=form.email.data
        )
        db.session.add(vendor)
        db.session.commit()
        flash("Vendor created successfully", "success")
        return redirect(url_for("vendors.list_vendors"))
    return render_template("vendors/vendor_form.html", form=form)


@vendors_bp.route("/vendors/<int:id>/edit", methods=["GET", "POST"])
def edit_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    form = VendorForm(obj=vendor)
    if form.validate_on_submit():
        form.populate_obj(vendor)
        db.session.commit()
        flash("Vendor updated successfully", "info")
        return redirect(url_for("vendors.list_vendors"))
    return render_template("vendors/vendor_form.html", form=form)

@vendors_bp.route("/vendors/<int:id>/delete", methods=["GET"])
def delete_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    db.session.delete(vendor)
    db.session.commit()
    flash("Vendor deleted", "warning")
    return redirect(url_for("vendors.list_vendors"))