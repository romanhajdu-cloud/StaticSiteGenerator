from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, textType: TextType, url= None):
        self.text = text
        self.text_type = textType
        self.url = url
    
    def __eq__(self, textNode: TextType):
        return self.text == textNode.text and self.text_type == textNode.text_type and self.url == textNode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"