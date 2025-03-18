from guizero import App, Textbox, Drawing, Combo, Slider
def draw_meme():
    meme.clear()
    meme.image(0, 0, "MSG to Alex this is where the PNG image goes")
    meme.text(
        20, 20, top_text.value,
        color=color.value,
        size=size.value,
        font=font.value)
    meme.text(
        20, 320, bottom_text.value,
        color=color.value,
        size=size.value,
        font=font.value,
        )
app = App("meme")