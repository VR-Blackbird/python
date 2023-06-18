class Connection:
    def __init__(self):
        self._new_state(ClosedConnState)

    def _new_state(self, state):
        self._current_state = state

    def open(self):
        self._current_state.open(self)

    def read(self):
        self._current_state.read(self)

    def write(self):
        self._current_state.write(self)

    def close(self):
        self._current_state.close(self)



class ClosedConnState:
    @staticmethod
    def read(conn):
        raise NotImplementedError

    @staticmethod
    def write(conn):
        raise NotImplementedError

    @staticmethod
    def open(conn):
        conn._new_state(OpenConnState)

    @staticmethod
    def close(conn):
        print("Already closed")
        raise NotImplementedError



class OpenConnState:
    @staticmethod
    def read(conn):
        print("Reading")


    @staticmethod
    def write(conn):
        print("Writing")


    @staticmethod
    def close(conn):
        print("Closing")
        conn._new_state(ClosedConnState)


    @staticmethod
    def open(conn):
        print("Already open")
        raise NotImplementedError

c = Connection()
c.open()
c.read()
c.close()
c.write()
