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
        for request in self.request.split(';'):
            cursor.execute(request)
        if self.response:
            self.response(cursor.fetchall())

    def __str__(self):
        return f'Request from "{self._source_thread_name}". Code:\n' + self.request


class RequestMany(Request):
    values = list

    def __init__(self, request: str, values: list, response_wrapper: callable = None):
        Request.__init__(self, request, response_wrapper)
        self.values = values

    def execute(self, cursor: sqlite.Cursor):
        cursor.executemany(self.request, self.values)
        if self.response:
            self.response(cursor.fetchall())

    def __str__(self):
        return f'Request from "{self._source_thread_name}". Code:\n' + self.request + '\nValues:\n' + str(self.values)


class DataBase(Thread):
    _sleep_time = 0.01
    _commit_ticks = 500
    _sign_out_ticks = 100

    cursor = sqlite.Cursor
    connection = sqlite.Connection
    queue = dict
    to_sign_up = list
    to_sign_out = list

    _db_file = str
    _tables_req = str

    _is_working = bool

    _is_a_lib = bool

    def __init__(self, db_file: str, create_tables_request: str):
        Thread.__init__(self, name='DataBase')
        self.queue = {}
        self.to_sign_out = []
        self.to_sign_up = []
        self._is_working = False
        self._db_file = db_file
        self._tables_req = create_tables_request
        self._is_a_lib = False

    @staticmethod
    def database_as_wrapper(db_file: str, create_tables_request: str):
        db = DataBase(db_file, create_tables_request)
        db._is_a_lib = True
        db._initialize()
        return db

    def wrp_execute_request(self, request: Request):
        request.execute(self.cursor)

    def sign_up_thread(self, thread: Thread = None):
        if not thread:
            thread = current_thread()
        assert (thread not in self.queue), "Thread already signed"
        self.to_sign_up.append(thread)

    def sign_out_thread(self):
        self.to_sign_out.append(current_thread())

    def _sign_up_threads(self):
        while len(self.to_sign_up) > 0:
            thread = self.to_sign_up.pop()
            self.queue[thread] = []
            print(str(thread) + ' is signed up.')

    def _sign_out_threads(self):
        skipped = 0
        while len(self.to_sign_out) > skipped:
            thread = self.to_sign_out.pop()
            if len(self.queue[thread]) > 0:
                self.to_sign_out.append(thread)
                skipped += 1
            else:
                del self.queue[thread]
                print(str(thread) + ' is signed out.')

    def append_request(self, request: Request):
        while (current_thread() not in self.queue) and (current_thread() in self.to_sign_up):
            time.sleep(0.01)
        self.queue[current_thread()].append(request)

    def execute_request(self, str_request: str):
        done = []
        request = Request(str_request, response_wrapper=(lambda data: done.append(data)))
        self.append_request(request)
        while len(done) != 1:
            time.sleep(0.001)
        return done[0]

    def close(self):
        self._is_working = False

    def _execute_requests(self):
        for key in self.queue:
            while len(self.queue[key]) > 0:
                req = self.queue[key].pop()
                try:
                    req.execute(self.cursor)
                except sqlite.DatabaseError:
                    print('Something wrong with request: ' + str(req))

    def _initialize(self):
        try:
            with open(self._db_file, 'r'):
                self.connection = sqlite.connect(self._db_file)
                self.cursor = self.connection.cursor()
        except FileNotFoundError:
            self.connection = sqlite.connect(self._db_file)
            self.cursor = self.connection.cursor()
            for req in self._tables_req.split(';'):
                self.cursor.execute(req)
            self.connection.commit()
        except Exception:
            raise Exception(f"Maybe I can't get an access to directory '{self._db_file}' or it does not exist? Who knows.")

    def run(self) -> None:
        if self._is_a_lib:
            raise Exception('This thread is prohibited to run. Use default __init__ statement.')
        self._initialize()

        self._is_working = True
        tick_timer = 0
        while self._is_working:
            self._sign_up_threads()
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
        print('Database committed. Ending operations...')
        self.connection.close()

    def __del__(self):
        self._save_and_close()

