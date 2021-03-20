import click
from delivery.ext.db import db
from delivery.ext.auth.models import User


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """Adiciona novo usuario"""
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()

    click.secho(f"Usuario {email} creado com sucesso!", fg='green')

def list_users():
    users = User.query.all()
    click.secho(f"lista de usuarios {users}", fg="yellow")
