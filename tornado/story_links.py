import tornado.ioloop
from tornado.web import RequestHandler, Application, url


class MainHandler(RequestHandler):
    def get(self):
        for i in range(1, 4):
            self.write('<a href="{}">link to story {}</a><br>'.format(
                    self.reverse_url("story", str(i)), i))


class StoryHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)

if __name__ == "__main__":
    db = 'dummy db. work nothing'
    app = Application([  # ncluding the routing table that maps requests to handlers.
        # routing table is a list of URLSpec objects (or tuples)
        url(r"/", MainHandler),  # at least a regular expression and a handler class
        url(r"/story/([0-9]+)",  # the regular expression contains capturing groups, these groups are the path arguments and will be passed to the handler’s HTTP method
            StoryHandler,
            dict(db=db),  # If a dictionary is passed as the third element of the URLSpec, it supplies the initialization arguments which will be passed to RequestHandler.initialize.
            name="story")  # the URLSpec may have a name, which will allow it to be used with RequestHandler.reverse_url.
        ])
    # dict 関数の keyword args が辞書の中身になる
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
