import threading

class DoubleCheckedSingleton:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:                       # first checl (no locking)
            with cls._lock:
                if cls._instance is None:               # second check (with locking)
                    cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    s1 = DoubleCheckedSingleton()
    s2 = DoubleCheckedSingleton()

    print(s1 is s2)