import os
import shutil
from markdown_block import markdown_to_html_node
from title_markdown import extract_title


def main():
    copy_directory('static', 'public')
    generate_page_recursive('content', 'template.html', 'public')


def copy_directory(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        src = os.path.join(source, item)
        dst = os.path.join(destination, item)
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            if os.path.exists(dst):
                shutil.rmtree(dst)
            os.mkdir(dst)
            copy_directory(src, dst)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")
    with open(from_path, "r") as file:
        source = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    html_node = markdown_to_html_node(source)

    title = extract_title(source)
    content = html_node.to_html()

    output = template.replace("{{ Title }}", title)
    output = output.replace("{{ Content }}", content)

    print(dest_path)

    with open(dest_path, "w") as file:
        file.write(output)


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, item)):
            if item.endswith(".md"):
                html = item.split(".")[0] + ".html"
                generate_page(os.path.join(dir_path_content, item),
                              template_path, os.path.join(dest_dir_path, html))
        else:
            generate_page_recursive(os.path.join(
                dir_path_content, item), template_path, os.path.join(dest_dir_path, item))


if __name__ == "__main__":
    main()
