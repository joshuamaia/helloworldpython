class User:
  def __init__(self, name = "", age = 0, email = ""):
    self.name = name
    self.age = age
    self.email = email

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}"
  
user = User("Joshua", 47, "teste@teste.com")
print(user)

lista = ["Azul", "Vermelho", "Verde", "Amarelo"]
listaUpper = [x.upper() for x in lista]
print(listaUpper)