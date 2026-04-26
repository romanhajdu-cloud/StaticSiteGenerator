from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, textType:TextType, url= None):
        self.text = text
        self.text_type = textType
        self.url = url
    
    def __eq__(self, textNode:TextType):
        return self.text == textNode.text and self.text_type == textNode.text_type and self.url == textNode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node:TextNode):
    node = text_node
    if node.text_type == TextType.TEXT:
        return LeafNode(None, node.text)
    if node.text_type == TextType.BOLD:
        return LeafNode("b", node.text)
    if node.text_type == TextType.ITALIC:
        return LeafNode("i", node.text)
    if node.text_type == TextType.CODE:
        return LeafNode("code", node.text)
    if node.text_type == TextType.LINK:
        return LeafNode("a", node.text, props= {"href": node.url})
    if node.text_type == TextType.IMAGE:
        return LeafNode("img", value="", props= {"src": node.url, "alt": node.text})
    else:
        raise Exception("Wrong TextType Enum")