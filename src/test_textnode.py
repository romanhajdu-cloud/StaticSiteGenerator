import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different text node with URL", TextType.ITALIC, "www.nieco.com")
        self.assertNotEqual(node, node2)

    def test_isUrl(self):
        node = TextNode("This is different text node with URL", TextType.ITALIC, "www.nieco.com")
        self.assertIsNotNone(node.url)
    
    def test_isNotUrl(self):
        node = TextNode("This is different text node with URL", TextType.ITALIC)
        self.assertIsNone(node.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")

    def test_image(self):
        node = TextNode("picture alt text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "picture alt text")

if __name__ == "__main__":
    unittest.main()