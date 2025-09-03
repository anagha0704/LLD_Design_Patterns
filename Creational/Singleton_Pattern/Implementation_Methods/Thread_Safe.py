import threading

class ThreadSafeSingleton:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    s1 = ThreadSafeSingleton()
    s2 = ThreadSafeSingleton()

    print(s1 is s2)