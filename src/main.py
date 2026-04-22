from textnode import TextNode, TextType

def main():
    test_node = TextNode(text="moj test", textType= TextType.LINK, url="www.mamdost.sk")
    print(test_node)

main()