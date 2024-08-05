import fasthtml.common as fh

app, rt = fh.fast_app()

@rt("/")
def get():
    return (
        fh.Title('Rohit Alamgari'),
        fh.Header('Hello! My name is Rohit Alamgari'),        
        fh.P(fh.A('Learn more about me', href='/about-me')),
        fh.P(fh.A('See my professional experience', href='/experience')),
        fh.P(fh.A('See what I\'ve learnt', href='/education')),
    )

@rt('/about-me')
def get():   
    return(
        fh.P('WIP'),
        fh.P(fh.A('Return to home page', href='/'))
    )
@rt('/experience')
def get():
    return(
        fh.P('WIP'),
        fh.P(fh.A('Return to home page', href='/'))
    )
@rt('/education')
def get():
    return(
        fh.P('WIP'),
        fh.P(fh.A('Return to home page', href='/'))
    )

fh.serve()
