from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db, Client
from clients.forms import ClientForm

clients_bp = Blueprint("clients", __name__)


@clients_bp.route("/clients")
def list_clients():
    clients = Client.query.all()
    return render_template("clients/clients.html", clients=clients)


@clients_bp.route("/clients/new", methods=["GET", "POST"])
def create_client():
    form = ClientForm()
    if form.validate_on_submit():
        client = Client(
            tipo_doc=form.tipo_doc.data,
            num_doc=form.num_doc.data,
            name=form.name.data,
            email=form.email.data,
            tel=form.tel.data,
            hotel=form.hotel.data
        )
        db.session.add(client)
        db.session.commit()
        flash("Client created successfully", "success")
        return redirect(url_for("clients.list_clients"))
    return render_template("clients/client_form.html", form=form)

@clients_bp.route("/clients/<int:id>/edit", methods=["GET", "POST"])
def edit_client(id):
    client = Client.query.get_or_404(id)
    form = ClientForm(obj=client)
    if form.validate_on_submit():
        form.populate_obj(client)
        db.session.commit()
        flash("Client updated successfully", "info")
        return redirect(url_for("clients.list_clients"))
    return render_template("clients/client_form.html", form=form)

@clients_bp.route("/clients/<int:id>/delete", methods=["GET"])
def delete_client(id):
    client = Client.query.get_or_404(id)
    db.session.delete(client)
    db.session.commit()
    flash("Client deleted", "warning")
    return redirect(url_for("clients.list_clients"))