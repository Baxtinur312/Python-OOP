class User2:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print("Foydalanuvchi faollashtirildi")

    def deactivate(self):
        self.is_active = False
        print("Foydalanuvchi bloklandi")

u = User2("john_doe", "john@example.com", False)
u.activate()
u.deactivate()