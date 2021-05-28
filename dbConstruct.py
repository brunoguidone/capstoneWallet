from wallet import app, db

print("Analyzing data base schema. Applying migrations.")

app.app_context().push()
db.create_all()