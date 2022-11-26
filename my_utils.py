from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader
from json import load
import os



def create_article_html(md_article_path, config_path, article_layout_path):

    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template(article_layout_path)

    with open(md_article_path) as markdown_file:
        article = markdown(
            markdown_file.read(),
            extras=['fenced-code-blocks', 'code-friendly'])

    with open(config_path) as config_file:
        config = load(config_file)


    output_path = './blogs/'+ config['file_name'] + '.html'

    with open(output_path, 'w') as output_file:
        output_file.write(
            template.render(
                title=config['title'],
                author=config['author'],
                file_name=config['file_name'],
                article=article
            )
        )

def create_blog_home(home_path,home_layout_path):

    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template(home_layout_path)


    # folder path
    dir_path = r'./blogs'

    # list to store files
    articles_names = []
    blogs = []
    articles_names_stripped = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            articles_names.append(path)
            articles_names_stripped.append(path.replace('.html', ''))



    for article_name, article_name_stripped in zip(articles_names,articles_names_stripped):
        blog = f'<li class="article-item"><a href="/blogs/{article_name}" class="nav__link">{article_name_stripped}</a></li>'
        blogs.append(blog)

    blogs_string = ""
    for blog in blogs:
        blogs_string += " "+ blog


    with open(home_path, 'w') as output_file:
        output_file.write(
            template.render(
                blogs = blogs_string
            )
        )


