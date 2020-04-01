from threading import Thread
from threading import current_thread
import time
import _sqlite3 as sqlite


class Request:
    request = str
    response = callable

    def __init__(self, request: str, response_wrapper: callable):
        self.request = request
        self.response = response_wrapper

    def execute(self, cursor: sqlite.Cursor):
        pass


class DataBase(Thread):
    cursor = sqlite.Cursor
    connection = sqlite.Connection
    queue = dict

    def __init__(self, db_file: str, create_tables_request: str):
        Thread.__init__(self, name='DataBase')
        pass

    def sign_up_thread(self):
        assert current_thread() not in self.queue.keys, "Thread already signed"
        self.queue[current_thread()] = []

    def sign_out_thread(self):
        del self.queue[current_thread()]

    def append_request(self, request: Request):
        self.queue[current_thread()].append(request)

    def run(self) -> None:
        pass

    def __del__(self):
        pass



