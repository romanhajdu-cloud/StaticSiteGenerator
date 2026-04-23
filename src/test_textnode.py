import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()