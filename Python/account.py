class Account():
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

class User(Account):
    def __init__(self, id, name, email, password, payment_method):
        super().__init__(id, name, email, password)
        self.payment_method = payment_method

class Drive(Account):
    def __init__(self, id, name, email, password, identif_doc, license):
        super().__init__(id, name, email, password)
        self.identif_doc = identif_doc
        self.license = license
