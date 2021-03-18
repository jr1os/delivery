import click
from delivery.ext.db import db
from delivery.ext.site import models

def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    
    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """Adiciona novo usuario"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.secho(f"Usuario {email} creado com sucesso!", fg='green')
    
    @app.cli.command()
    def listar_pedidos():
        # TODO: usar tabulate
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuarios")