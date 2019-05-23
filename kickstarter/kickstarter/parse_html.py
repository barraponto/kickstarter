import html2text

parser = html2text.HTML2Text()
parser.ignore_links = True
parser.ignore_images = False
parser.ignore_emphasis = True
parser.ignore_tables = False
