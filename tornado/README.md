# 概要
tornadoを使ってみる
www.tornadoweb.org/en/stable/guide.html

# やったこと
## 読んでみた
- ch.3
    - tornado.web は NOT WSGI できなくはないけど、tornado らしさが制限される
    - IOLoop.add_callback NEED BLock Special IOLoop.run.in_excutor
    - Python3.6 にして、async, await を使っていく？
- ch.4
    - installing
    - twisted をつかっている
    - pycares NON-block DNS resolver
- ch.5.1
    - 4parts で構成されている
        - Request Handler: web framework
        - HTTPServer, AsyncHTTPClient: library for HTTP
        - IOLoop, IOStream: HTTP Component の Task Mangaer?
        - tornado.gen: asynchronous corutine library
    - HTTP のアプリはほとんど IDLE -> one user, one thread はもったいなすぎる。
        - single thread event loop 内 自分で context switch
    - Asyncronous のやりたかた
        - CALLBACK arg
        - return PLACE_HOLDER
        - deliver to A QUEUE
        - CALLBACK_REGISTRY? e.g. posix signals