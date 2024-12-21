import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimeter: str, text_type: TextType):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
            text = node.text

            left = text.find(delimeter)
            right = text.rfind(delimeter)

            if left > -1 and right > left:
                if text[:left] != '':
                    nodes.append(TextNode(text[:left], TextType.TEXT))
                nodes.append(
                    TextNode(text[left+len(delimeter):right], text_type))
                if text[right+len(delimeter):] != '':
                    nodes.append(
                        TextNode(text[right+len(delimeter):], TextType.TEXT))
            else:
                nodes.append(node)
    return nodes


def extract_markdown_images(text):
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(image_regex, text)


def extract_markdown_links(text):
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(link_regex, text)


def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            nodes.append(node)
        else:
            for link in links:
                left = text.find("[" + link[0] + "]")
                pre = text[0:left]
                if pre != '':
                    nodes.append(TextNode(pre, TextType.TEXT))
                nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                chars = len(pre) + len(link[0]) + len(link[1]) + 4
                text = text[chars:]
            if len(text) > 0:
                nodes.append(TextNode(text, TextType.TEXT))

    return nodes


def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            nodes.append(node)
        else:
            for link in images:
                left = text.find("![" + link[0] + "]")
                pre = text[0:left]
                if pre != '':
                    nodes.append(TextNode(pre, TextType.TEXT))
                nodes.append(TextNode(link[0], TextType.IMAGE, link[1]))
                chars = len(pre) + len(link[0]) + len(link[1]) + 5
                text = text[chars:]
            if len(text) > 0:
                nodes.append(TextNode(text, TextType.TEXT))

    return nodes
