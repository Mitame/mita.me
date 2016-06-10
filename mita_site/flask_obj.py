from flask import Flask as oldFlask

class Flask(oldFlask):
    def __init__(self, *args, **kwargs):
        oldFlask.__init__(self, *args, **kwargs)
        self.navbar_links = []
        self.add_template_filter(self.navbar_links, "navbar_links")

    def route(self, *args, **kwargs):
        # print(args)
        try:
            if kwargs["navbar_title"]:
                self.navbar_links.append({
                    "text": kwargs,
                    "href": args[0],
                })
                self.add_template_filter(self.navbar_links, "navbar_links")
                del(kwargs["navbar_title"])
        except KeyError:
            pass
        return oldFlask.route(self, *args, **kwargs)
