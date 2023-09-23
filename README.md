# Para criar as tabelas
## Python Console
    from project import app, db
    app.app_context().push()
    db.create_all()