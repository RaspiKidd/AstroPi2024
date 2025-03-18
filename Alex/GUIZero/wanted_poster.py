from guizero import App, Text, Picture
app = App("Wanted!")
app.bg = "#FBFBD0"
wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text = Text(app, "REWARD £100B +")
wanted_text.text_size = 30
wanted_text = Text(app, "Renegade Raider Skin")
wanted_text.text_size = 30
wanted_text.font = "Times New Roman"
Peely = Picture(app, image="./images/image67930")
app.display()