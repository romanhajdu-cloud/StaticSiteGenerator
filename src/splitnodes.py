from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes:list, delimiter, text_type: TextType):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            split_texts = old_node.text.split(delimiter)
            if len(split_texts) % 2 == 0:
                raise Exception("In text symbols must be in middle")
            
            for i in range(len(split_texts)):
                if split_texts[i] == "":
                    continue
                if i % 2 != 0:
                    new_nodes.append(TextNode(split_texts[i], text_type))
                else:
                    new_nodes.append(TextNode(split_texts[i], TextType.TEXT))
           
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

