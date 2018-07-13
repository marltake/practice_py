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
    app = Application([
        url(r"/", MainHandler),
        url(r"/story/([0-9]+)", StoryHandler, dict(db=db), name="story")
        ])
    # dict 関数の keyword args が辞書の中身になる
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
