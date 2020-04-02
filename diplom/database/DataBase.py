from threading import Thread
from threading import current_thread
import time
import _sqlite3 as sqlite


class Request:
    request = str
    response = callable
    _source_thread_name = str

    def __init__(self, request: str, response_wrapper: callable = None):
        self.request = request
        self.response = response_wrapper
        self._source_thread_name = current_thread().name

    def execute(self, cursor: sqlite.Cursor):
        cursor.execute(self.request)
        if self.response:
            self.response(cursor.fetchall())

    def __str__(self):
        return f'Request from "{self._source_thread_name}". Code:\n' + self.request


class DataBase(Thread):
    _sleep_time = 0.01
    _commit_ticks = 500
    _sign_out_ticks = 100

    cursor = sqlite.Cursor
    connection = sqlite.Connection
    queue = dict
    to_sign_out = list

    _is_working = bool

    def __init__(self, db_file: str, create_tables_request: str):
        Thread.__init__(self, name='DataBase')
        self.queue = {}
        self.to_sign_out = []
        self._is_working = False
        try:
            with open(db_file, 'r'):
                self.connection = sqlite.connect(db_file)
                self.cursor = self.connection.cursor()
        except FileNotFoundError:
            self.connection = sqlite.connect(db_file)
            self.cursor = self.connection.cursor()
            self.cursor.execute(create_tables_request)
            self.connection.commit()

    def sign_up_thread(self):
        assert current_thread() not in self.queue.keys, "Thread already signed"
        self.queue[current_thread()] = []

    def sign_out_thread(self):
        self.to_sign_out.append(current_thread())
        # del self.queue[current_thread()]

    def _sign_out_threads(self):
        empty = []
        for thread in self.to_sign_out:
            if len(self.queue[thread]) == 0:
                del self.queue[thread]
                empty.append(thread)
        for thread in empty:
            self.to_sign_out.remove(thread)

    def append_request(self, request: Request):
        self.queue[current_thread()].append(request)

    def close(self):
        self._is_working = False

    def _execute_requests(self):
        for key in self.queue:
            while len(self.queue[key]) > 0:
                req = self.queue[key].pop()
                try:
                    req.execute(self.cursor)
                except sqlite.Error:
                    print('Something wrong with request: ' + str(req))

    def run(self) -> None:
        self._is_working = True
        tick_timer = 0
        while self._is_working:
            self._execute_requests()

            if tick_timer % DataBase._commit_ticks == 0:
                self.connection.commit()
            if tick_timer % DataBase._sign_out_ticks == 0:
                self._sign_out_threads()

            tick_timer += 1
            time.sleep(DataBase._sleep_time)
        self._save_and_close()

    def _save_and_close(self):
        self._execute_requests()
        self.connection.commit()
        self.connection.close()

    def __del__(self):
        self._save_and_close()

