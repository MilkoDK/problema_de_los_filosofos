import threading
import time

# Número de filósofos (y tenedores)
N = 5

# Semáforo para controlar el acceso a los tenedores
semaphore = threading.Semaphore(N)

class Philosopher(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.left_fork = id
        self.right_fork = (id + 1) % N

    def run(self):
        while True:
            # Pensar
            print(f"Filósofo {self.id} está pensando...")
            time.sleep(2)

            # Tomar los tenedores
            print(f"Filósofo {self.id} quiere tomar los tenedores...")
            semaphore.acquire()
            print(f"Filósofo {self.id} ha tomado el tenedor izquierdo ({self.left_fork})")
            time.sleep(1)
            if semaphore.acquire(blocking=False):
                print(f"Filósofo {self.id} ha tomado el tenedor derecho ({self.right_fork})")
                print(f"Filósofo {self.id} está comiendo...")
                time.sleep(2)
                semaphore.release()
                semaphore.release()
            else:
                print(f"Filósofo {self.id} no puede tomar el tenedor derecho ({self.right_fork})")
                semaphore.release()

if __name__ == '__main__':
    # Crear los filósofos
    philosophers = []
    for i in range(N):
        philosophers.append(Philosopher(i))

    # Iniciar los hilos
    for p in philosophers:
        p.start()

    # Esperar a que los hilos terminen
    for p in philosophers:
        p.join()