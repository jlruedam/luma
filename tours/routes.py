from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db, Tour, Agency
from tours.forms import TourForm

tours_bp = Blueprint("tours", __name__, template_folder="templates/tours")

# LIST
@tours_bp.route("/tours")
def list_tours():
    tours = Tour.query.all()
    return render_template("tours/tours.html", tours=tours)

# CREATE
@tours_bp.route("/tours/new", methods=["GET", "POST"])
def create_tour():
    form = TourForm()
    form.agency_id.choices = [(a.id, a.name_agency) for a in Agency.query.all()]

    if form.validate_on_submit():
        tour = Tour(
            name_tour=form.name_tour.data,
            description=form.description.data,
            price_sale=form.price_sale.data,
            price_total=form.price_total.data,
            image_path=form.image_path.data,
            agency_id=form.agency_id.data
        )
        db.session.add(tour)
        db.session.commit()
        flash("Tour created successfully", "success")
        return redirect(url_for("tours.list_tours"))
    return render_template("tours/tour_form.html", form=form)

# EDIT
@tours_bp.route("/tours/<int:id>/edit", methods=["GET", "POST"])
def edit_tour(id):
    tour = Tour.query.get_or_404(id)
    form = TourForm(obj=tour)
    form.agency_id.choices = [(a.id, a.name_agency) for a in Agency.query.all()]

    if form.validate_on_submit():
        form.populate_obj(tour)
        db.session.commit()
        flash("Tour updated successfully", "info")
        return redirect(url_for("tours.list_tours"))
    return render_template("tours/tour_form.html", form=form)

# DELETE
@tours_bp.route("/tours/<int:id>/delete", methods=["GET"])
def delete_tour(id):
    tour = Tour.query.get_or_404(id)
    db.session.delete(tour)
    db.session.commit()
    flash("Tour deleted", "warning")
    return redirect(url_for("tours.list_tours"))