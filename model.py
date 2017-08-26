from example1 import Role, User, db 


db.drop_all()
db.create_all()
admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susuan', role=user_role)


db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan])
db.session.commit()

print(admin_role.id, mod_role.id, user_role.id)
