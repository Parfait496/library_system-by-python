from datetime import datetime

def track_access(func):
    def wrapper(*args, **kwargs):
        print("------LOG------")
        print("Function:", func.__name__)
        print("Time:", datetime.now())
        return func(*args, **kwargs)
    return wrapper

#closures remembers required role
def permission_check(required_role):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if self.user_role != required_role:
                print("permission denied.")
                return None
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def borrow_item(item):
    print("Borrowing:", item.title)