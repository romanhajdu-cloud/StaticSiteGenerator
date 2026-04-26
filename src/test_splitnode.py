import unittest

from splitnodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("Toto je text s `kódom` vnútri", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Toto je text s ", TextType.TEXT),
            TextNode("kódom", TextType.CODE),
            TextNode(" vnútri", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_(self):
        node = TextNode("Toto je text s kódom a vo vnútri mam aj **bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Toto je text s kódom a vo vnútri mam aj ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
            

if __name__ == "__main__":
    unittest.main()