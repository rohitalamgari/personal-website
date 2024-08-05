import fasthtml.common as fh

app, rt = fh.fast_app()


@rt("/")
def get():
    return (
        fh.Titled('Welcome!',
                  fh.P(
                      'My name is Rohit Alamgari'
                  ))
    )


fh.serve()
