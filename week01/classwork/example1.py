import threading
import time

class MyThread(threading.Thread):
    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        time.sleep(0.75)
        print(f'{self.message=}')

def dummy(message):
    time.sleep(0.5)
    print(f'{message=}')

def main():
    my_thread = MyThread("hello")
    my_thread.start()
    
    t1 = threading.Thread(target=dummy, args=("asdfjadskfa",))
    t1.start()
    
    print('next line')

main()