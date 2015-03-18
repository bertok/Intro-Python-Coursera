# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
current_count = 0
width = 300
height = 200
score = 0
tries = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global current_time
    tenth_sec = (t) % 10
    secs = int(t / 10) % 10
    min_ones = int(t / 600) % 600
    min_tens = int(t / 100) % 6
    current_time = str(min_ones)+":"+str(min_tens)+str(secs)+"."+str(tenth_sec)
    return current_time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global start
    global running
    timer.start()
    running = True
        
def stop_timer():
    global tries
    global score
    global start
    global current_count
    global running
    timer.stop()    
    
    if running == True:
        tries += 1
        if (int(current_count) % 10) == 0 and int(current_count) != 0:
            score += 1
    running = False
     
def reset_timer():
    timer.stop()
    global current_count
    global score
    global tries
    global running
    current_count = 0
    score = 0
    tries = 0
    running = False

def quit_game():
    frame.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global current_count
    current_count = (int(current_count) + 1)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(current_count)), [100,125], 50, "Blue")
    canvas.draw_text((str(score)+" / "+str(tries)), [220,35], 35, "Black")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
frame.set_canvas_background("Yellow")

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start_timer, 50)
frame.add_button("Stop", stop_timer, 50)
frame.add_button("Reset", reset_timer, 50)
frame.add_button("Quit", quit_game, 50)

# start frame
frame.start()

# Please remember to review the grading rubric
