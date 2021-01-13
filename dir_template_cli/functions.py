from shutil import copytree, ignore_patterns, rmtree
import pathlib
import  os

here = pathlib.Path(__file__).parent.absolute()
templates = os.path.join(here,"templates")


def init(dst, template= "template_dir"):
    # TODO : check if exists
    src = os.path.join(templates,template)
    copytree(src, dst, ignore=ignore_patterns('*.pyc', 'tmp*','__pycache__'))

def ls():
    # TODO : check if exists
    i = 1
    p = pathlib.Path(templates)
    for path in p.glob("*"):
        print (f"{i}-- {path.name}")
        i = i +1
    
def rm(template):
    # TODO : check if exists
    rmtree(os.path.join(templates, template ))
    
def add(src):
    # TODO : check if exists
    src = pathlib.Path(src)
    dst = os.path.join(templates, src.name )
    copytree(src, dst, ignore=ignore_patterns('*.pyc', 'tmp*','__pycache__'))
    
def update():
    # TODO : check if exists
    pass
    
def tree(template):
    # TODO : check if exists
    startpath = os.path.join(templates,template)

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))