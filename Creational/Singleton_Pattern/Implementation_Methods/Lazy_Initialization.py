class LazySingleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("creating instance")
            cls._instance = super().__new__(cls)
        return cls._instance

 
# This implementation is not thread-safe. If multiple threads call getInstance() simultaneously 
# when instance is null, it's possible to create multiple instances.

if __name__ == "__main__":
    s1 = LazySingleton()
    s2 = LazySingleton()

    print(s1 is s2)