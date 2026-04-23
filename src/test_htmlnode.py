import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_print_props(self):
        props_dict = {  "brand": "Toyota",
                        "model": "Prius",
                        "year": 2019}
        

        html_node = HTMLNode(props=props_dict)
        print(html_node.props_to_html())

    def test_represent(self):
        props_dict = {  "brand_1": "Toyota",
                        "brand_2": "Honda",
                        "brand_3": "Suzuki"}
        
        html_node = HTMLNode(props=props_dict)
        html_node.__repr__()

    def test_eq(self):
        html_node = HTMLNode(tag="test", value="test value")
        html_node2 = HTMLNode(tag="test", value="test value")
        self.assertEqual(html_node, html_node2)

    def test_propsIsNone(self):
        html_node = HTMLNode(tag="test", value="test value")
        self.assertIsNone(html_node.props)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()