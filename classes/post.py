class Post:

    def __init__(self, pic, content):
        self.pic = pic
        self.content = content

    def __repr__(self):
        return f"Ссылка на картинку {self.pic}\n" \
               f"Текст поста: {self.content}"
