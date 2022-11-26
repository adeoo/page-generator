
from my_utils import create_article_html, create_blog_home

#article page variables
md_article_path = 'page_generator/new_article/article.md'
config_path = 'page_generator/new_article/config.json'
article_layout_path = 'page_generator/layouts/article_layout.html'  #

#Blog home variables
home_path = './blog-home.html'
home_layout_path = 'page_generator/layouts/blog_home_layout.html'


def main():
     create_article_html(md_article_path, config_path, article_layout_path)
     create_blog_home(home_path,home_layout_path)


if __name__ == '__main__':
    main()