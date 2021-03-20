import click

def init_app(app):
    @app.before_first_request
    def init_everything():
        click.secho("Isto roda sempre antes do primeiro request!!", fg="red")

