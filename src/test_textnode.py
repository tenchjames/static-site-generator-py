import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_image(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node that is not equal", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_neq_text_type(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text_to_html_bold(self):
        node = TextNode("textnode", TextType.BOLD)
        leaf = text_node_to_html_node(node)
        leaf_html = leaf.to_html()
        expected = "<b>textnode</b>"
        self.assertEqual(leaf_html, expected)

    def test_text_to_html_italic(self):
        node = TextNode("textnode", TextType.ITALIC)
        leaf = text_node_to_html_node(node)
        leaf_html = leaf.to_html()
        expected = "<i>textnode</i>"
        self.assertEqual(leaf_html, expected)

    def test_text_to_html_text(self):
        node = TextNode("textnode", TextType.TEXT)
        leaf = text_node_to_html_node(node)
        leaf_html = leaf.to_html()
        expected = "textnode"
        self.assertEqual(leaf_html, expected)

    def test_text_to_html_code(self):
        node = TextNode("textnode", TextType.CODE)
        leaf = text_node_to_html_node(node)
        leaf_html = leaf.to_html()
        expected = "<code>textnode</code>"
        self.assertEqual(leaf_html, expected)

    def test_text_to_html_image(self):
        node = TextNode("textnode", TextType.IMAGE, "http://image.png")
        leaf = text_node_to_html_node(node)
        leaf_html = leaf.to_html()
        expected = '<img src="http://image.png" alt="textnode"></img>'
        self.assertEqual(leaf_html, expected)

    def test_text_to_html_link(self):
        node = TextNode("textnode", TextType.LINK, "http://google.com")
        leaf = text_node_to_html_node(node)
        leaf_html = leaf.to_html()
        expected = '<a href="http://google.com">textnode</a>'
        self.assertEqual(leaf_html, expected)


if __name__ == "__main__":
    unittest.main()
