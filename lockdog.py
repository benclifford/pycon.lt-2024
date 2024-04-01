import pickle
import threading

class Dog:
    def __init__(self, name: str):
        self.name = name
        self.bones_buried = 0
        self.bones_eaten = 0
        self.modification_lock = threading.Lock()

    def give_bone(self):
        """Dog gets a bone and buries it"""
        with self.modification_lock:
            self.bones_buried += 1

    def deferred_eat_bone(self):
        """Dog unburies a bone and eats its"""
        with self.modification_lock:
            self.bones_buried -= 1
            self.bones_eaten += 1

fido = Dog("fido")
print(fido.bones_buried, fido.bones_eaten)
fido.give_bone()
print(fido.bones_buried, fido.bones_eaten)
fido.deferred_eat_bone()
print(fido.bones_buried, fido.bones_eaten)

with open("lockdog.pkl", "wb") as f:
    pickle.dump(fido, f)
