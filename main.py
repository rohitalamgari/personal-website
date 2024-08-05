import fasthtml.common as fh
from markdown import markdown
import fh_bootstrap as bs

app, rt = fh.fast_app()

#from fasthtml's page
md_exts='codehilite', 'smarty', 'extra', 'sane_lists'
def Markdown(s, exts=md_exts, **kw): return bs.Div(bs.NotStr(markdown(s, extensions=exts)), **kw)


main_section_txt = """
### Hi there!
My name is [Rohit Alamgari](https://www.linkedin.com/in/rohit-alamgari/)

I'm currently a junior at [UT studying CS](https://www.cs.utexas.edu/) who's interested in ML, Computer Vision, NLP, and Cloud Computing


Here's a link to my [Github](https://github.com/rohitalamgari) and my [Resume](https://drive.google.com/file/d/166uf9n7F6tm0T6XLSdyenrphcf7rUq1u/view?usp=sharing)

Thanks for visiting!
"""

@rt("/")
def get():
    return (
        fh.Div(Markdown(main_section_txt))
    )

fh.serve()
