import unittest
import inline_markdown
from enums import BlockType
from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_code(self):
        node = TextNode("Toto je text s `kódom` vnútri", TextType.TEXT)
        new_nodes = inline_markdown.split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Toto je text s ", TextType.TEXT),
            TextNode("kódom", TextType.CODE),
            TextNode(" vnútri", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_(self):
        node = TextNode("Toto je text s kódom a vo vnútri mam aj **bold**", TextType.TEXT)
        new_nodes = inline_markdown.split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("Toto je text s kódom a vo vnútri mam aj ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected)

    def test_extract_markdown_images(self):
        matches = inline_markdown.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = inline_markdown.extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
 

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = inline_markdown.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_to_textnodes(self):
        node = "This is **text** with an ![image](https://i.imgur.com/zjjcJKZ.png) with link [to boot dev](https://www.boot.dev) for _italic_"
        new_nodes = inline_markdown.text_to_textnodes(node)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" with link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" for ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )    

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = inline_markdown.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )    


    def test_block_to_block_type_heading(self):
        block = "# Toto je nadpis"
        result = inline_markdown.block_to_block_type(block)
        assert result == BlockType.HEADING

if __name__ == "__main__":
    unittest.main()