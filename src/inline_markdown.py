from enums import BlockType
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            imgages = extract_markdown_images(node.text)
            if len(imgages) == 0:
                new_nodes.append(node)
            else:
                lasting_text = node.text
                for alt, url in imgages:
                    splited = lasting_text.split(f"![{alt}]({url})", 1)
                    if splited[0] != "":
                        new_nodes.append(TextNode(splited[0], TextType.TEXT)) 
                    new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                    lasting_text = splited[1]
                if lasting_text != "":
                    new_nodes.append(TextNode(lasting_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) == 0:
                new_nodes.append(node)
            else:
                lasting_text = node.text
                for alt, url in links:
                    splited = lasting_text.split(f"[{alt}]({url})", 1)
                    if splited[0] != "":
                        new_nodes.append(TextNode(splited[0], TextType.TEXT)) 
                    new_nodes.append(TextNode(alt, TextType.LINK, url))
                    lasting_text = splited[1]
                if lasting_text != "":
                    new_nodes.append(TextNode(lasting_text, TextType.TEXT))
    return new_nodes#

def text_to_textnodes(text):
    new_text = TextNode(text, TextType.TEXT)
    nodes = [new_text]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def markdown_to_blocks(markdown:str):
    bloks = []
    splited_markdowns = markdown.split("\n\n")
    for markdown in splited_markdowns:
        if markdown.strip() == "":
            continue
        bloks.append(markdown.strip())
    return bloks

def block_to_block_type(block):
    lines = block.split("\n")
    first_line = lines[0]
    
    count = 0
    for char in first_line:
        if char == "#":
            count += 1
        else:
            break
    
    if count >= 1 and count <= 6 and len(first_line) > count and first_line[count] == " ":
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break
    if is_unordered:
        return BlockType.UNORDERED_LIST
    
    is_ordered = True
    expected = 1
    for line in lines:
        if not line.startswith(f"{str(expected)}. "):
            is_ordered = False
            break
        else:
            expected += 1
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH