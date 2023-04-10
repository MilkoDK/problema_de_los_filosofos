# Problema de los filosofos

Cinco filósofos se sientan alrededor de una mesa y pasan su vida cenando y pensando. Cada filósofo tiene un plato   
de fideos y un tenedor a la izquierda de su plato. Para comer los fideos son necesarios dos tenedores y cada filósofo   
sólo puede tomar los que están a su izquierda y derecha. Si cualquier filósofo toma un tenedor y el otro está ocupado,   
se quedará esperando, con el tenedor en la mano, hasta que pueda tomar el otro tenedor, para luego empezar a comer. 

Si dos filósofos adyacentes intentan tomar el mismo tenedor a una vez, se produce una condición de carrera: ambos compiten   
por tomar el mismo tenedor, y uno de ellos se queda sin comer. 

Si todos los filósofos toman el tenedor que está a su derecha al mismo tiempo, entonces todos se quedarán esperando eternamente,   
porque alguien debe liberar el tenedor que les falta. Nadie lo hará porque todos se encuentran en la misma situación (esperando   
que alguno deje sus tenedores). Entonces los filósofos se morirán de hambre. Este bloqueo mutuo se denomina interbloqueo o deadlock. 

## Codigo documentado

A continuación se detallan los componentes principales del código:

La variable N indica el número de filósofos (y tenedores) en la mesa.
La clase Philosopher representa un filósofo en el problema. Cada filósofo tiene un identificador (id) y dos tenedores (left_fork y right_fork)   
a su izquierda y derecha, respectivamente.
El método run() de la clase Philosopher contiene la lógica principal del problema. Primero, el filósofo piensa por un tiempo aleatorio utilizando   
la función sleep() de la biblioteca time. Luego, intenta tomar sus tenedores izquierdo y derecho. Para ello, adquiere el semáforo utilizando el   
método acquire() de la clase Semaphore de la biblioteca threading. Si ambos tenedores están disponibles, el filósofo los toma y come durante un   
tiempo aleatorio. Si no, el filósofo suelta el tenedor izquierdo y vuelve a intentarlo más tarde.
En el bloque if name == 'main', se crean los filósofos y se inician sus hilos utilizando el método start() de la clase Thread. Luego, se espera a   
que todos los hilos terminen utilizando el método join().

### codigo 
~~~
import threading
import time

# Número de filósofos (y tenedores)
N = 5

# Semáforo para controlar el acceso a los tenedores
semaphore = threading.Semaphore(N)
~~~
Importamos las librerías threading y time. Luego se define la constante N con el número de filósofos   
y tenedores, y se crea un semáforo con un contador inicial de N.

~~~
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

~~~
Se define la clase Philosopher, que hereda de Thread. El constructor inicializa el id del filósofo y los tenedores   
izquierdo y derecho que corresponden a su posición en la mesa. En el método run(), el filósofo piensa durante 2   
segundos, luego intenta tomar los tenedores. Si ambos están disponibles, los toma y comienza a comer durante 2 segundos.  
Si no, libera el tenedor izquierdo y vuelve a intentarlo más tarde.

~~~
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

~~~
Se comprueba si el script es el programa principal y, en caso afirmativo, se crean los filósofos y se inician sus hilos.   
Luego se espera a que todos los hilos terminen antes de salir del programa.





