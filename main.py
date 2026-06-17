from graphics import Canvas
import random
import time


CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000
CIRCLE_SIZE = 20

N_CIRCLES = 20
INSIDE_BORDER = 70
SQUARE_SIZE = 20

BUILDING_WIDTH = 20
BUILDING_HEIGHT = 60
EXTRA_SPACE = 10 

DELAY = 0.01
NUM_STEPS = 50

def main():
    print('Tokio-cities')


    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    rect = canvas.create_rectangle(
    0, 
    0, 
    CANVAS_WIDTH, 
    CANVAS_HEIGHT,
    'black'
    )

    
    network_id = "Neo-Network-City #" + str(random.randint(1000, 9999))
    text_width = len(network_id) * 10

    network_text = canvas.create_text(
        (CANVAS_WIDTH / 2) - (text_width / 2),
        20,
        text=network_id,
        font='Arial',
        font_size=20,
        color= random_color()
    )

    for i in range(20):
        create_random_building(canvas)

    for i in range(10):
        create_network_line(canvas)   

def create_random_building(canvas):
    
    x = random.randint(0, CANVAS_WIDTH - INSIDE_BORDER)
    y = random.randint(0, CANVAS_HEIGHT - INSIDE_BORDER)

    color = random_color()
    building_name = random_building()

    building = canvas.create_rectangle(
    x, y,
    x + BUILDING_WIDTH,
    y + BUILDING_HEIGHT,
    "white"
    )

    obj = canvas.create_text(
        x,
        y + BUILDING_HEIGHT,
        building_name,
        font='Arial',
        font_size=15,
        color='black'
    )

    # Extrae el número del shape ID y crea el label
    shape_id = canvas.create_text(
        x,
        y + BUILDING_HEIGHT + EXTRA_SPACE,
        "Building " + obj.split("_")[1],
        font='Arial',
        font_size=12,
        color='crimson'
    )

def create_network_line(canvas):


    x = random.randint(0, CANVAS_WIDTH - INSIDE_BORDER)
    y = random.randint(0, CANVAS_HEIGHT - INSIDE_BORDER)

    x2 = random.randint(0, CANVAS_WIDTH - INSIDE_BORDER)
    y2 = random.randint(0, CANVAS_HEIGHT - INSIDE_BORDER)

    x3 = random.randint(0, CANVAS_WIDTH - INSIDE_BORDER)
    y3 = random.randint(0, CANVAS_HEIGHT - INSIDE_BORDER)

    x4 = random.randint(0, CANVAS_WIDTH - INSIDE_BORDER)
    y4 = random.randint(0, CANVAS_HEIGHT - INSIDE_BORDER)

    x5 = random.randint(0, CANVAS_WIDTH - INSIDE_BORDER)
    y5 = random.randint(0, CANVAS_HEIGHT - INSIDE_BORDER)

    color = random_color()
    stations = random_stations()

    # Guarda el ID de cada nodo
    node1 = canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, color)
    node2 = canvas.create_oval(x2, y2, x2 + CIRCLE_SIZE, y2 + CIRCLE_SIZE, color)
    node3 = canvas.create_oval(x3, y3, x3 + CIRCLE_SIZE, y3 + CIRCLE_SIZE, color)
    node4 = canvas.create_oval(x4, y4, x4 + CIRCLE_SIZE, y4 + CIRCLE_SIZE, color)
    node5 = canvas.create_oval(x5, y5, x5 + CIRCLE_SIZE, y5 + CIRCLE_SIZE, color)

    # Texto con ID único por nodo
    for node, nx, ny in [
        (node1, x, y), (node2, x2, y2), (node3, x3, y3),
        (node4, x4, y4), (node5, x5, y5)
    ]:
        node_label = "Node " + node.split("_")[1]
        canvas.create_text(nx, ny - 15, node_label, font='Arial', font_size=11, color='gold')
        canvas.create_text(nx, ny, stations, font='Arial', font_size=13, color='white')

    # Líneas igual que antes
    canvas.create_line(x  + CIRCLE_SIZE/2, y  + CIRCLE_SIZE/2, x2 + CIRCLE_SIZE/2, y2 + CIRCLE_SIZE/2, color)
    canvas.create_line(x2 + CIRCLE_SIZE/2, y2 + CIRCLE_SIZE/2, x3 + CIRCLE_SIZE/2, y3 + CIRCLE_SIZE/2, color)
    canvas.create_line(x3 + CIRCLE_SIZE/2, y3 + CIRCLE_SIZE/2, x4 + CIRCLE_SIZE/2, y4 + CIRCLE_SIZE/2, color)
    canvas.create_line(x4 + CIRCLE_SIZE/2, y4 + CIRCLE_SIZE/2, x5 + CIRCLE_SIZE/2, y5 + CIRCLE_SIZE/2, color)


    metro = canvas.create_rectangle(
        x, y,
        x + 50,
        y + SQUARE_SIZE,
        "darkorange"
        )
    
    

    # Animar por cada segmento de la ruta
    puntos = [
        (x, y), (x2, y2), (x3, y3), (x4, y4), (x5, y5)
    ]

    for i in range(len(puntos) - 1):
        fx, fy = puntos[i]
        tx, ty = puntos[i + 1]
        animate_to(canvas, metro, fx, fy, tx, ty)


def animate_to(canvas, obj, from_x, from_y, to_x, to_y, steps=NUM_STEPS, delay=DELAY):
  
    dx = (to_x - from_x) / steps
    dy = (to_y - from_y) / steps

    for _ in range(steps):
        canvas.move(obj, dx, dy)
        time.sleep(delay)
    


def random_color():
  
    colors = ['aqua', 'purple', 'salmon', 'lightblue', 'cyan', 'springgreen', 'red', 'gold', 'grey', 'greenyellow', 'violet', 'orange']
    return random.choice(colors)

def random_stations():

    stations = ['network_line A', 'network_line B', 'network_line C', 'network_line D', 'network_line E', 'network_line F', 'network_line G', 'network_line H', 'network_line I', 'network_line J', 'network_line K', 'network_line L', 'network_line M', 'network_line N', 'network_line O', 'network_line P', 'network_line Q', 'network_line R', 'network_line S', 'network_line T', 'network_line U', 'network_line V', 'network_line W', 'network_line X', 'network_line Y', 'network_line Z']
    return random.choice(stations)

def random_building():

    building = ['building A', 'building B', 'building C', 'building D', 'building E', 'building F', 'building G', 'building H', 'building I', 'building J', 'building K', 'building L', 'building M', 'building N', 'building O', 'building P', 'building Q', 'building R', 'building S', 'building T', 'building U', 'building V', 'building W', 'building X', 'building Y', 'building Z']
    return random.choice(building)
