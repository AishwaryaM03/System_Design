## Sysncronized Singleton implementation in Python

import threading

# Class implementing thread-safe Singleton
class Singleton:
    # Object declaration
    __instance = None

    # Lock for thread safety (similar to Java's 'synchronized')
    __lock = threading.Lock()

    # Private constructor simulation
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    # Thread-safe method to get the instance of class
    @staticmethod
    def getInstance():
        # Only one thread can enter this block at a time
        # This is equivalent to using 'synchronized' in Java
        with Singleton.__lock:  # Synchronized block
            if Singleton.__instance is None:
                Singleton()
        return Singleton.__instance

## ouble-checked locking pattern (DCLP) is a design pattern used to reduce the overhead of acquiring a lock by first testing the locking criterion (the "lock hint") without actually acquiring the lock. Only if the check indicates that locking is required does the actual locking logic proceed. This can improve performance in scenarios where the lock is frequently acquired and released, as it avoids unnecessary locking in cases where the resource is already initialized.
import threading

# Class implementing double-checked locking Singleton
class Singleton:
    # Object declaration
    __instance = None
    __lock = threading.Lock()

    # Private constructor simulation
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    # Thread-safe method using double-checked locking
    @staticmethod
    def getInstance():
        if Singleton.__instance is None:  # First check (no lock)
            with Singleton.__lock:
                if Singleton.__instance is None:  # Second check (with lock)
                    Singleton()
        return Singleton.__instance

##Bill Pugh Singleton implementation in Python

# Class implementing Singleton using holder-like lazy initialization
class Singleton:
    # Private constructor simulation
    def __init__(self):
        if hasattr(Singleton, "_created"):
            raise Exception("This class is a singleton!")
        Singleton._created = True

# Function acting like a static holder in Java
def getInstance():
    # This behaves like Java's Holder class:
    # - Singleton instance is not created until getInstance() is first called
    # - The attribute is only added once (lazy initialization)
    # - Thread-safety is not guaranteed unless protected externally
    if not hasattr(getInstance, "_instance"):
        getInstance._instance = Singleton()
    return getInstance._instance