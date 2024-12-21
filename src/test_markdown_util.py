import unittest

from textnode import TextNode, TextType
from markdown_util import (split_nodes_delimiter,
                           split_nodes_image,
                           split_nodes_link,
                           extract_markdown_images,
                           extract_markdown_links)


class TestMarkDownUtils(unittest.TestCase):
    def test_split_nodes_code(self):
        code_node = TextNode("a block of `code` surrounded", TextType.TEXT)
        nodes = split_nodes_delimiter([code_node], "`", TextType.CODE)
        node_count = len(nodes)
        self.assertEqual(node_count, 3)

    def test_split_nodes_bold(self):
        code_node = TextNode("a block of **code** surrounded", TextType.TEXT)
        nodes = split_nodes_delimiter([code_node], "**", TextType.BOLD)
        node_count = len(nodes)
        self.assertEqual(node_count, 3)

        first = nodes[0].text
        self.assertEqual(first, "a block of ")
        first_type = nodes[0].text_type
        self.assertEqual(first_type, TextType.TEXT)

        second = nodes[1].text
        self.assertEqual(second, "code")
        second_type = nodes[1].text_type
        self.assertEqual(second_type, TextType.BOLD)

        third = nodes[2].text
        self.assertEqual(third, " surrounded")
        third_type = nodes[2].text_type
        self.assertEqual(third_type, TextType.TEXT)

    def test_split_nodes_italic(self):
        text_node = TextNode("a block of *italic*", TextType.TEXT)
        second_text_node = TextNode(
            "a second block of *italic*", TextType.TEXT)

        nodes = split_nodes_delimiter(
            [text_node, second_text_node], "*", TextType.ITALIC)
        node_count = len(nodes)
        self.assertEqual(node_count, 4)

    def test_extract_image_text(self):
        md_image = "![alt text](http://image.jpg) ![alt2 text](http://image2.jpg)"
        images = extract_markdown_images(md_image)
        self.assertEqual([('alt text', 'http://image.jpg'),
                         ('alt2 text', 'http://image2.jpg')], images)

    def test_extract_link_text(self):
        test = "[alt text](http://image.jpg) ![alt2 text](http://image2.jpg)"
        results = extract_markdown_links(test)
        self.assertEqual([('alt text', 'http://image.jpg')], results)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            len(new_nodes),
            4
        )

        self.assertEqual(
            "This is text with a link ",
            new_nodes[0].text
        )

        self.assertEqual(
            TextType.TEXT,
            new_nodes[0].text_type
        )

        self.assertEqual(
            TextType.LINK,
            new_nodes[1].text_type
        )

        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            len(new_nodes),
            5
        )

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with a image ![alt text](https://alt.jpg) post text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            len(new_nodes),
            3
        )

        self.assertEqual(
            "This is text with a image ",
            new_nodes[0].text
        )

        self.assertEqual(
            TextType.TEXT,
            new_nodes[0].text_type
        )

        self.assertEqual(
            TextType.IMAGE,
            new_nodes[1].text_type
        )


if __name__ == "__main__":
    unittest.main()
