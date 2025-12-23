from turtle import Turtle, Screen
import random


def draw_line():
    timmy = Turtle()
    timmy.penup()
    timmy.hideturtle()
# # #     timmy.goto(x=250,y=-200)
# # #     timmy.left(90)
# # #     timmy.pendown()
# # #     timmy.pensize(10)
# # #     timmy.forward(400)


# # # is_race_on = False
# # # color = ["red", "orange", "yellow", "green", "blue", "indigo"]
# # # screen = Screen()
# # # screen.setup(width=550, height=400)
# # # user_guess = screen.textinput(title="Turtle Racing Game ", prompt="which turtle will win the race? Enter a color: ")
# # # all_turtle = []
# # # y_cor = -100
# # # for i in range(6):
# # #     new_turtle = Turtle()
# # #     all_turtle.append(new_turtle)
# # #     new_turtle.shape("turtle")
# # #     new_turtle.color(color[i])
# # #     new_turtle.penup()
# # #     new_turtle.goto(x=-230, y=y_cor)
# # #     y_cor += 50
# # # draw_line()

# # # if type(user_guess) == str:
# # #     is_race_on = True

# # # while is_race_on:
# # #     for turtle in all_turtle:
# # #         if turtle.xcor() > 230:
# # #             winning_color = turtle.pencolor()
# # #             if winning_color == user_guess:
# # #                 print(f"you've won ! the {winning_color} color turtle is the winner")
# # #             else:
# # #                 print(f"you've lost !! the {winning_color} color turtle is the winner")
# # #             is_race_on = False

# # #         random_distance = random.randint(0, 10)
# # #         turtle.forward(random_distance)

# # # screen.exitonclick()


# # from turtle import Turtle, Screen
# # import random
# # import time


# # def setup_screen():
# #     """Configure the racing screen with styling"""
# #     screen = Screen()
# #     screen.setup(width=800, height=600)
# #     screen.bgcolor("#87CEEB")  # Sky blue
# #     screen.title("🐢 Turtle Racing Championship 🏁")
# #     return screen


# # def draw_track():
# #     """Draw racing track with start and finish lines"""
# #     track = Turtle()
# #     track.speed(0)
# #     track.hideturtle()
# #     track.penup()
    
# #     # Draw grass (track background)
# #     track.goto(-350, -250)
# #     track.color("#90EE90")
# #     track.pendown()
# #     track.begin_fill()
# #     for _ in range(2):
# #         track.forward(700)
# #         track.left(90)
# #         track.forward(350)
# #         track.left(90)
# #     track.end_fill()
    
# #     # Draw start line
# #     track.penup()
# #     track.goto(-350, -250)
# #     track.setheading(90)
# #     track.pensize(5)
# #     track.color("white")
# #     track.pendown()
# #     for _ in range(18):
# #         track.forward(10)
# #         track.penup()
# #         track.forward(10)
# #         track.pendown()
    
# #     # Draw finish line (checkered pattern)
# #     track.penup()
# #     track.goto(320, -250)
# #     track.setheading(90)
# #     for i in range(35):
# #         track.pendown()
# #         track.color("black" if i % 2 == 0 else "white")
# #         track.begin_fill()
# #         for _ in range(2):
# #             track.forward(10)
# #             track.right(90)
# #             track.forward(10)
# #             track.right(90)
# #         track.end_fill()
# #         track.penup()
# #         track.forward(10)


# # def draw_title():
# #     """Draw title and instructions"""
# #     title = Turtle()
# #     title.hideturtle()
# #     title.penup()
# #     title.goto(0, 240)
# #     title.color("#2C3E50")
# #     title.write("🏆 TURTLE RACING CHAMPIONSHIP 🏆", 
# #                 align="center", font=("Arial", 24, "bold"))
    
# #     title.goto(0, 210)
# #     title.color("#34495E")
# #     title.write("Choose your champion wisely!", 
# #                 align="center", font=("Arial", 14, "italic"))


# # def create_turtles():
# #     """Create racing turtles with improved styling"""
# #     colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# #     turtles = []
# #     y_pos = -200
    
# #     for i, color in enumerate(colors):
# #         racer = Turtle()
# #         racer.shape("turtle")
# #         racer.color(color)
# #         racer.shapesize(1.5, 1.5)
# #         racer.penup()
# #         racer.goto(-320, y_pos)
# #         racer.setheading(0)
# #         turtles.append(racer)
        
# #         # Add lane numbers
# #         label = Turtle()
# #         label.hideturtle()
# #         label.penup()
# #         label.goto(-360, y_pos - 8)
# #         label.color("#2C3E50")
# #         label.write(f"{i+1}", font=("Arial", 12, "bold"))
        
# #         y_pos += 60
    
# #     return turtles, colors


# # def get_user_bet(colors):
# #     """Get user's bet with improved UI"""
# #     screen = Screen()
    
# #     # Create color options string
# #     options = "\n".join([f"{i+1}. {color.capitalize()}" for i, color in enumerate(colors)])
    
# #     while True:
# #         choice = screen.textinput(
# #             "Place Your Bet! 🎲",
# #             f"Which turtle will win?\n\n{options}\n\nEnter color name or number:"
# #         )
        
# #         if choice is None:  # User cancelled
# #             return None
        
# #         choice = choice.lower().strip()
        
# #         # Check if it's a number
# #         if choice.isdigit() and 1 <= int(choice) <= len(colors):
# #             return colors[int(choice) - 1]
        
# #         # Check if it's a color name
# #         if choice in colors:
# #             return choice
        
# #         # Invalid input - ask again
# #         continue


# # def countdown():
# #     """Display animated countdown"""
# #     counter = Turtle()
# #     counter.hideturtle()
# #     counter.penup()
# #     counter.goto(0, 0)
# #     counter.color("#E74C3C")
    
# #     for i in range(3, 0, -1):
# #         counter.clear()
# #         counter.write(i, align="center", font=("Arial", 80, "bold"))
# #         time.sleep(0.8)
    
# #     counter.clear()
# #     counter.color("#27AE60")
# #     counter.write("GO!", align="center", font=("Arial", 80, "bold"))
# #     time.sleep(0.5)
# #     counter.clear()


# # def display_result(winner_color, user_bet):
# #     """Display race result with animation"""
# #     result = Turtle()
# #     result.hideturtle()
# #     result.penup()
# #     result.goto(0, 150)
    
# #     if winner_color == user_bet:
# #         result.color("#27AE60")
# #         result.write("🎉 YOU WON! 🎉", align="center", font=("Arial", 36, "bold"))
# #         result.goto(0, 110)
# #         result.write(f"The {winner_color.upper()} turtle wins!", 
# #                     align="center", font=("Arial", 18, "normal"))
# #     else:
# #         result.color("#E74C3C")
# #         result.write("😢 YOU LOST 😢", align="center", font=("Arial", 36, "bold"))
# #         result.goto(0, 110)
# #         result.write(f"The {winner_color.upper()} turtle wins!", 
# #                     align="center", font=("Arial", 18, "normal"))
# #         result.goto(0, 80)
# #         result.write(f"You bet on {user_bet.upper()}", 
# #                     align="center", font=("Arial", 14, "italic"))


# # def run_race(turtles, user_bet):
# #     """Run the race with improved mechanics"""
# #     is_race_on = True
    
# #     while is_race_on:
# #         for turtle in turtles:
# #             # Check if turtle crossed finish line
# #             if turtle.xcor() > 300:
# #                 winner = turtle.pencolor()
# #                 display_result(winner, user_bet)
# #                 is_race_on = False
# #                 break
            
# #             # Move turtle with slight randomness for excitement
# #             distance = random.randint(1, 15)
# #             turtle.forward(distance)
        
# #         time.sleep(0.05)  # Smooth animation


# # def main():
# #     """Main game function"""
# #     screen = setup_screen()
# #     draw_track()
# #     draw_title()
# #     turtles, colors = create_turtles()
    
# #     user_bet = get_user_bet(colors)
    
# #     if user_bet:
# #         countdown()
# #         run_race(turtles, user_bet)
        
# #         # Show replay option
# #         replay = Turtle()
# #         replay.hideturtle()
# #         replay.penup()
# #         replay.goto(0, 40)
# #         replay.color("#34495E")
# #         replay.write("Click anywhere to exit", 
# #                     align="center", font=("Arial", 12, "italic"))
    
# #     screen.exitonclick()


# # if __name__ == "__main__":
# #     main()


# import tkinter as tk
# from tkinter import messagebox
# import random

# class TurtleCrossingGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Turtle Road Crossing Game")
#         self.root.resizable(False, False)
        
#         # Game variables
#         self.difficulty = None
#         self.game_active = False
#         self.score = 0
#         self.level = 1
#         self.cars = []
        
#         # Difficulty settings (car speed)
#         self.speeds = {
#             'easy': 3,
#             'medium': 5,
#             'hard': 8
#         }
        
#         # Show menu
#         self.show_menu()
    
#     def show_menu(self):
#         # Clear any existing widgets
#         for widget in self.root.winfo_children():
#             widget.destroy()
        
#         # Menu frame
#         menu_frame = tk.Frame(self.root, bg='#2ecc71', width=600, height=600)
#         menu_frame.pack()
        
#         # Title
#         title = tk.Label(menu_frame, text="🐢 Turtle Road Crossing 🐢", 
#                         font=('Arial', 28, 'bold'), bg='#2ecc71', fg='white')
#         title.pack(pady=50)
        
#         # Instructions
#         instructions = tk.Label(menu_frame, 
#                               text="Help the turtle cross the road!\nUse Arrow Keys to move\nAvoid the cars!",
#                               font=('Arial', 14), bg='#2ecc71', fg='white', justify='center')
#         instructions.pack(pady=20)
        
#         # Difficulty buttons
#         tk.Label(menu_frame, text="Select Difficulty:", 
#                 font=('Arial', 18, 'bold'), bg='#2ecc71', fg='white').pack(pady=20)
        
#         btn_frame = tk.Frame(menu_frame, bg='#2ecc71')
#         btn_frame.pack(pady=20)
        
#         easy_btn = tk.Button(btn_frame, text="Easy", font=('Arial', 16, 'bold'),
#                             bg='#3498db', fg='white', width=10, height=2,
#                             command=lambda: self.start_game('easy'))
#         easy_btn.grid(row=0, column=0, padx=10, pady=10)
        
#         medium_btn = tk.Button(btn_frame, text="Medium", font=('Arial', 16, 'bold'),
#                               bg='#f39c12', fg='white', width=10, height=2,
#                               command=lambda: self.start_game('medium'))
#         medium_btn.grid(row=0, column=1, padx=10, pady=10)
        
#         hard_btn = tk.Button(btn_frame, text="Hard", font=('Arial', 16, 'bold'),
#                             bg='#e74c3c', fg='white', width=10, height=2,
#                             command=lambda: self.start_game('hard'))
#         hard_btn.grid(row=0, column=2, padx=10, pady=10)
    
#     def start_game(self, difficulty):
#         self.difficulty = difficulty
#         self.game_active = True
#         self.score = 0
#         self.level = 1
#         self.cars = []
        
#         # Clear menu
#         for widget in self.root.winfo_children():
#             widget.destroy()
        
#         # Create game canvas
#         self.canvas = tk.Canvas(self.root, width=600, height=600, bg='#34495e')
#         self.canvas.pack()
        
#         # Draw road
#         self.draw_road()
        
#         # Create turtle (player)
#         self.turtle_x = 285
#         self.turtle_y = 550
#         self.turtle = self.canvas.create_oval(self.turtle_x, self.turtle_y,
#                                              self.turtle_x + 30, self.turtle_y + 30,
#                                              fill='#2ecc71', outline='#27ae60', width=3)
        
#         # Score and level display
#         self.score_text = self.canvas.create_text(100, 30, text=f"Score: {self.score}",
#                                                   font=('Arial', 16, 'bold'), fill='white')
#         self.level_text = self.canvas.create_text(500, 30, text=f"Level: {self.level}",
#                                                   font=('Arial', 16, 'bold'), fill='white')
#         self.diff_text = self.canvas.create_text(300, 30, text=f"Mode: {difficulty.upper()}",
#                                                  font=('Arial', 16, 'bold'), fill='yellow')
        
#         # Bind keys
#         self.root.bind('<Up>', lambda e: self.move_turtle(0, -20))
#         self.root.bind('<Down>', lambda e: self.move_turtle(0, 20))
#         self.root.bind('<Left>', lambda e: self.move_turtle(-20, 0))
#         self.root.bind('<Right>', lambda e: self.move_turtle(20, 0))
        
#         # Start game loop
#         self.spawn_cars()
#         self.game_loop()
    
#     def draw_road(self):
#         # Draw road stripes
#         for i in range(100, 550, 100):
#             self.canvas.create_rectangle(0, i, 600, i + 60, fill='#7f8c8d', outline='')
        
#         # Draw lane dividers
#         for y in range(100, 550, 100):
#             for x in range(0, 600, 40):
#                 self.canvas.create_rectangle(x, y + 28, x + 20, y + 32, fill='white')
    
#     def spawn_cars(self):
#         if not self.game_active:
#             return
        
#         # Spawn a car on a random lane
#         lane = random.choice([130, 230, 330, 430])
#         direction = random.choice([-1, 1])
#         x = 600 if direction == -1 else -80
        
#         colors = ['#e74c3c', '#3498db', '#f39c12', '#9b59b6', '#1abc9c']
#         color = random.choice(colors)
        
#         car = self.canvas.create_rectangle(x, lane - 20, x + 80, lane + 20,
#                                           fill=color, outline='black', width=2)
#         self.cars.append({'id': car, 'direction': direction, 'lane': lane})
        
#         # Spawn next car after random delay (adjusted by level)
#         delay = max(500 - (self.level * 50), 200)
#         self.root.after(random.randint(delay, delay + 500), self.spawn_cars)
    
#     def move_turtle(self, dx, dy):
#         if not self.game_active:
#             return
        
#         new_x = self.turtle_x + dx
#         new_y = self.turtle_y + dy
        
#         # Keep turtle in bounds
#         if 0 <= new_x <= 570 and 50 <= new_y <= 570:
#             self.turtle_x = new_x
#             self.turtle_y = new_y
#             self.canvas.coords(self.turtle, new_x, new_y, new_x + 30, new_y + 30)
            
#             # Check if reached top (goal)
#             if new_y <= 60:
#                 self.score += 10 * self.level
#                 self.level += 1
#                 self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
#                 self.canvas.itemconfig(self.level_text, text=f"Level: {self.level}")
#                 # Reset turtle position
#                 self.turtle_y = 550
#                 self.canvas.coords(self.turtle, self.turtle_x, 550, 
#                                  self.turtle_x + 30, 580)
    
#     def game_loop(self):
#         if not self.game_active:
#             return
        
#         speed = self.speeds[self.difficulty]
        
#         # Move all cars
#         for car in self.cars[:]:
#             coords = self.canvas.coords(car['id'])
#             if not coords:
#                 self.cars.remove(car)
#                 continue
            
#             new_x = coords[0] + (speed * car['direction'])
            
#             # Remove cars that are off screen
#             if new_x < -100 or new_x > 700:
#                 self.canvas.delete(car['id'])
#                 self.cars.remove(car)
#             else:
#                 self.canvas.move(car['id'], speed * car['direction'], 0)
                
#                 # Check collision with turtle
#                 if self.check_collision(car['id']):
#                     self.game_over()
#                     return
        
#         self.root.after(30, self.game_loop)
    
#     def check_collision(self, car_id):
#         car_coords = self.canvas.coords(car_id)
#         turtle_coords = self.canvas.coords(self.turtle)
        
#         if not car_coords or not turtle_coords:
#             return False
        
#         # Simple bounding box collision
#         return (turtle_coords[0] < car_coords[2] and
#                 turtle_coords[2] > car_coords[0] and
#                 turtle_coords[1] < car_coords[3] and
#                 turtle_coords[3] > car_coords[1])
    
#     def game_over(self):
#         self.game_active = False
        
#         # Show game over message
#         self.canvas.create_rectangle(100, 200, 500, 400, fill='black', outline='white', width=3)
#         self.canvas.create_text(300, 250, text="GAME OVER!", 
#                                font=('Arial', 32, 'bold'), fill='red')
#         self.canvas.create_text(300, 300, text=f"Final Score: {self.score}",
#                                font=('Arial', 20), fill='white')
#         self.canvas.create_text(300, 340, text="Press any key to return to menu",
#                                font=('Arial', 14), fill='white')
        
#         self.root.bind('<Key>', lambda e: self.show_menu())

# # Create and run the game
# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TurtleCrossingGame(root)
#     root.mainloop()




import tkinter as tk
from tkinter import messagebox
import random

class ArcadeGameHub:
    def __init__(self, root):
        self.root = root
        self.root.title("5-in-1 Arcade Game Hub")
        self.root.resizable(False, False)
        self.show_main_menu()
    
    def show_main_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main menu frame
        menu_frame = tk.Frame(self.root, bg='#2c3e50', width=700, height=700)
        menu_frame.pack()
        
        # Title
        title = tk.Label(menu_frame, text="🎮 ARCADE GAME HUB 🎮", 
                        font=('Arial', 32, 'bold'), bg='#2c3e50', fg='#ecf0f1')
        title.pack(pady=30)
        
        subtitle = tk.Label(menu_frame, text="Choose Your Game!", 
                           font=('Arial', 18), bg='#2c3e50', fg='#95a5a6')
        subtitle.pack(pady=10)
        
        # Game buttons
        games = [
            ("🐢 Turtle Road Crossing", self.start_turtle_game, '#27ae60'),
            ("🐍 Snake Classic", self.start_snake_game, '#e67e22'),
            ("🎯 Brick Breaker", self.start_brick_breaker, '#3498db'),
            ("🚀 Space Invaders", self.start_space_invaders, '#9b59b6'),
            ("🍎 Catch the Falling", self.start_catch_game, '#e74c3c')
        ]
        
        for i, (name, command, color) in enumerate(games):
            btn = tk.Button(menu_frame, text=name, font=('Arial', 16, 'bold'),
                          bg=color, fg='white', width=25, height=2,
                          command=command, cursor='hand2')
            btn.pack(pady=12)
        
        # Exit button
        exit_btn = tk.Button(menu_frame, text="Exit", font=('Arial', 14),
                           bg='#34495e', fg='white', width=15,
                           command=self.root.quit)
        exit_btn.pack(pady=20)

    # ==================== GAME 1: TURTLE ROAD CROSSING ====================
    def start_turtle_game(self):
        self.turtle_game = TurtleCrossingGame(self.root, self.show_main_menu)

    # ==================== GAME 2: SNAKE CLASSIC ====================
    def start_snake_game(self):
        self.snake_game = SnakeGame(self.root, self.show_main_menu)

    # ==================== GAME 3: BRICK BREAKER ====================
    def start_brick_breaker(self):
        self.brick_game = BrickBreakerGame(self.root, self.show_main_menu)

    # ==================== GAME 4: SPACE INVADERS ====================
    def start_space_invaders(self):
        self.space_game = SpaceInvadersGame(self.root, self.show_main_menu)

    # ==================== GAME 5: CATCH THE FALLING ====================
    def start_catch_game(self):
        self.catch_game = CatchFallingGame(self.root, self.show_main_menu)


# ==================== TURTLE ROAD CROSSING GAME ====================
class TurtleCrossingGame:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.difficulty = None
        self.game_active = False
        self.score = 0
        self.level = 1
        self.cars = []
        self.speeds = {'easy': 3, 'medium': 5, 'hard': 8}
        self.show_difficulty_menu()
    
    def show_difficulty_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        menu_frame = tk.Frame(self.root, bg='#2ecc71', width=700, height=700)
        menu_frame.pack()
        
        tk.Label(menu_frame, text="🐢 Turtle Road Crossing", 
                font=('Arial', 28, 'bold'), bg='#2ecc71', fg='white').pack(pady=30)
        
        tk.Label(menu_frame, text="Select Difficulty:", 
                font=('Arial', 18, 'bold'), bg='#2ecc71', fg='white').pack(pady=20)
        
        for diff, color in [('easy', '#3498db'), ('medium', '#f39c12'), ('hard', '#e74c3c')]:
            tk.Button(menu_frame, text=diff.upper(), font=('Arial', 16, 'bold'),
                     bg=color, fg='white', width=15, height=2,
                     command=lambda d=diff: self.start_game(d)).pack(pady=10)
        
        tk.Button(menu_frame, text="Back to Menu", font=('Arial', 12),
                 bg='#34495e', fg='white', width=15,
                 command=self.return_callback).pack(pady=20)
    
    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.game_active = True
        self.score = 0
        self.level = 1
        self.cars = []
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.canvas = tk.Canvas(self.root, width=700, height=700, bg='#34495e')
        self.canvas.pack()
        
        self.draw_road()
        
        self.turtle_x = 335
        self.turtle_y = 650
        self.turtle = self.canvas.create_oval(self.turtle_x, self.turtle_y,
                                             self.turtle_x + 30, self.turtle_y + 30,
                                             fill='#2ecc71', outline='#27ae60', width=3)
        
        self.score_text = self.canvas.create_text(100, 30, text=f"Score: {self.score}",
                                                  font=('Arial', 16, 'bold'), fill='white')
        self.level_text = self.canvas.create_text(600, 30, text=f"Level: {self.level}",
                                                  font=('Arial', 16, 'bold'), fill='white')
        
        self.root.bind('<Up>', lambda e: self.move_turtle(0, -20))
        self.root.bind('<Down>', lambda e: self.move_turtle(0, 20))
        self.root.bind('<Left>', lambda e: self.move_turtle(-20, 0))
        self.root.bind('<Right>', lambda e: self.move_turtle(20, 0))
        
        self.spawn_cars()
        self.game_loop()
    
    def draw_road(self):
        for i in range(100, 650, 100):
            self.canvas.create_rectangle(0, i, 700, i + 60, fill='#7f8c8d', outline='')
        for y in range(100, 650, 100):
            for x in range(0, 700, 40):
                self.canvas.create_rectangle(x, y + 28, x + 20, y + 32, fill='white')
    
    def spawn_cars(self):
        if not self.game_active:
            return
        lane = random.choice([130, 230, 330, 430, 530])
        direction = random.choice([-1, 1])
        x = 700 if direction == -1 else -80
        colors = ['#e74c3c', '#3498db', '#f39c12', '#9b59b6', '#1abc9c']
        car = self.canvas.create_rectangle(x, lane - 20, x + 80, lane + 20,
                                          fill=random.choice(colors), outline='black', width=2)
        self.cars.append({'id': car, 'direction': direction})
        delay = max(500 - (self.level * 50), 200)
        self.root.after(random.randint(delay, delay + 500), self.spawn_cars)
    
    def move_turtle(self, dx, dy):
        if not self.game_active:
            return
        new_x = self.turtle_x + dx
        new_y = self.turtle_y + dy
        if 0 <= new_x <= 670 and 50 <= new_y <= 670:
            self.turtle_x = new_x
            self.turtle_y = new_y
            self.canvas.coords(self.turtle, new_x, new_y, new_x + 30, new_y + 30)
            if new_y <= 60:
                self.score += 10 * self.level
                self.level += 1
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                self.canvas.itemconfig(self.level_text, text=f"Level: {self.level}")
                self.turtle_y = 650
                self.canvas.coords(self.turtle, self.turtle_x, 650, self.turtle_x + 30, 680)
    
    def game_loop(self):
        if not self.game_active:
            return
        speed = self.speeds[self.difficulty]
        for car in self.cars[:]:
            coords = self.canvas.coords(car['id'])
            if not coords:
                self.cars.remove(car)
                continue
            new_x = coords[0] + (speed * car['direction'])
            if new_x < -100 or new_x > 800:
                self.canvas.delete(car['id'])
                self.cars.remove(car)
            else:
                self.canvas.move(car['id'], speed * car['direction'], 0)
                if self.check_collision(car['id']):
                    self.game_over()
                    return
        self.root.after(30, self.game_loop)
    
    def check_collision(self, car_id):
        car_coords = self.canvas.coords(car_id)
        turtle_coords = self.canvas.coords(self.turtle)
        if not car_coords or not turtle_coords:
            return False
        return (turtle_coords[0] < car_coords[2] and turtle_coords[2] > car_coords[0] and
                turtle_coords[1] < car_coords[3] and turtle_coords[3] > car_coords[1])
    
    def game_over(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="GAME OVER!", font=('Arial', 32, 'bold'), fill='red')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())


# ==================== SNAKE CLASSIC GAME ====================
class SnakeGame:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.game_active = True
        self.score = 0
        self.snake = [(350, 350), (330, 350), (310, 350)]
        self.direction = 'Right'
        self.food = None
        self.size = 20
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.canvas = tk.Canvas(self.root, width=700, height=700, bg='#1a1a1a')
        self.canvas.pack()
        
        self.canvas.create_text(350, 30, text="🐍 SNAKE GAME", font=('Arial', 24, 'bold'), fill='#2ecc71')
        self.score_text = self.canvas.create_text(350, 60, text=f"Score: {self.score}",
                                                  font=('Arial', 16), fill='white')
        
        self.root.bind('<Up>', lambda e: self.change_direction('Up'))
        self.root.bind('<Down>', lambda e: self.change_direction('Down'))
        self.root.bind('<Left>', lambda e: self.change_direction('Left'))
        self.root.bind('<Right>', lambda e: self.change_direction('Right'))
        
        self.spawn_food()
        self.game_loop()
    
    def spawn_food(self):
        while True:
            x = random.randint(0, 33) * 20 + 10
            y = random.randint(5, 33) * 20 + 10
            if (x, y) not in self.snake:
                self.food = (x, y)
                break
    
    def change_direction(self, new_dir):
        opposites = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if new_dir != opposites.get(self.direction):
            self.direction = new_dir
    
    def game_loop(self):
        if not self.game_active:
            return
        
        head = self.snake[0]
        if self.direction == 'Up':
            new_head = (head[0], head[1] - self.size)
        elif self.direction == 'Down':
            new_head = (head[0], head[1] + self.size)
        elif self.direction == 'Left':
            new_head = (head[0] - self.size, head[1])
        else:
            new_head = (head[0] + self.size, head[1])
        
        # Check collisions
        if (new_head[0] < 0 or new_head[0] >= 700 or new_head[1] < 100 or 
            new_head[1] >= 700 or new_head in self.snake):
            self.game_over()
            return
        
        self.snake.insert(0, new_head)
        
        # Check food
        if new_head == self.food:
            self.score += 10
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.spawn_food()
        else:
            self.snake.pop()
        
        self.draw()
        self.root.after(100, self.game_loop)
    
    def draw(self):
        self.canvas.delete('snake', 'food')
        for i, (x, y) in enumerate(self.snake):
            color = '#2ecc71' if i == 0 else '#27ae60'
            self.canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10,
                                        fill=color, outline='white', tags='snake')
        self.canvas.create_oval(self.food[0] - 10, self.food[1] - 10,
                               self.food[0] + 10, self.food[1] + 10,
                               fill='red', tags='food')
    
    def game_over(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="GAME OVER!", font=('Arial', 32, 'bold'), fill='red')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())


# ==================== BRICK BREAKER GAME ====================
class BrickBreakerGame:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.game_active = True
        self.score = 0
        self.lives = 3
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.canvas = tk.Canvas(self.root, width=700, height=700, bg='#2c3e50')
        self.canvas.pack()
        
        self.canvas.create_text(350, 30, text="🎯 BRICK BREAKER", font=('Arial', 24, 'bold'), fill='white')
        self.score_text = self.canvas.create_text(150, 60, text=f"Score: {self.score}",
                                                  font=('Arial', 16), fill='white')
        self.lives_text = self.canvas.create_text(550, 60, text=f"Lives: {self.lives}",
                                                  font=('Arial', 16), fill='white')
        
        # Paddle
        self.paddle_x = 300
        self.paddle_y = 650
        self.paddle_width = 100
        self.paddle_height = 15
        self.paddle = self.canvas.create_rectangle(self.paddle_x, self.paddle_y,
                                                   self.paddle_x + self.paddle_width,
                                                   self.paddle_y + self.paddle_height,
                                                   fill='#3498db', outline='white', width=2)
        
        # Ball
        self.ball_x = 350
        self.ball_y = 620
        self.ball_dx = 3
        self.ball_dy = -3
        self.ball = self.canvas.create_oval(self.ball_x - 10, self.ball_y - 10,
                                           self.ball_x + 10, self.ball_y + 10,
                                           fill='white')
        
        # Bricks
        self.bricks = []
        colors = ['#e74c3c', '#e67e22', '#f39c12', '#2ecc71', '#3498db', '#9b59b6']
        for row in range(6):
            for col in range(10):
                x1 = col * 70 + 5
                y1 = row * 30 + 100
                brick = self.canvas.create_rectangle(x1, y1, x1 + 65, y1 + 25,
                                                    fill=colors[row], outline='white', width=2)
                self.bricks.append(brick)
        
        self.canvas.bind('<Motion>', self.move_paddle)
        self.game_loop()
    
    def move_paddle(self, event):
        self.paddle_x = max(0, min(event.x - self.paddle_width // 2, 700 - self.paddle_width))
        self.canvas.coords(self.paddle, self.paddle_x, self.paddle_y,
                          self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)
    
    def game_loop(self):
        if not self.game_active:
            return
        
        self.ball_x += self.ball_dx
        self.ball_y += self.ball_dy
        
        # Wall collisions
        if self.ball_x <= 10 or self.ball_x >= 690:
            self.ball_dx *= -1
        if self.ball_y <= 90:
            self.ball_dy *= -1
        
        # Paddle collision
        if (self.paddle_x <= self.ball_x <= self.paddle_x + self.paddle_width and
            self.paddle_y <= self.ball_y + 10 <= self.paddle_y + self.paddle_height):
            self.ball_dy = -abs(self.ball_dy)
            offset = (self.ball_x - (self.paddle_x + self.paddle_width / 2)) / (self.paddle_width / 2)
            self.ball_dx = offset * 5
        
        # Brick collisions
        for brick in self.bricks[:]:
            coords = self.canvas.coords(brick)
            if (coords[0] <= self.ball_x <= coords[2] and coords[1] <= self.ball_y <= coords[3]):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy *= -1
                self.score += 10
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                break
        
        # Ball out of bounds
        if self.ball_y >= 700:
            self.lives -= 1
            self.canvas.itemconfig(self.lives_text, text=f"Lives: {self.lives}")
            if self.lives <= 0:
                self.game_over()
                return
            self.ball_x = 350
            self.ball_y = 620
            self.ball_dx = 3
            self.ball_dy = -3
        
        # Win condition
        if not self.bricks:
            self.win_game()
            return
        
        self.canvas.coords(self.ball, self.ball_x - 10, self.ball_y - 10,
                          self.ball_x + 10, self.ball_y + 10)
        self.root.after(20, self.game_loop)
    
    def win_game(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="YOU WIN!", font=('Arial', 32, 'bold'), fill='#2ecc71')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())
    
    def game_over(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="GAME OVER!", font=('Arial', 32, 'bold'), fill='red')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())


# ==================== SPACE INVADERS GAME ====================
class SpaceInvadersGame:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.game_active = True
        self.score = 0
        self.aliens = []
        self.bullets = []
        self.alien_bullets = []
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.canvas = tk.Canvas(self.root, width=700, height=700, bg='#0a0a0a')
        self.canvas.pack()
        
        self.canvas.create_text(350, 30, text="🚀 SPACE INVADERS", font=('Arial', 24, 'bold'), fill='white')
        self.score_text = self.canvas.create_text(350, 60, text=f"Score: {self.score}",
                                                  font=('Arial', 16), fill='white')
        
        # Player ship
        self.ship_x = 335
        self.ship_y = 650
        self.ship = self.canvas.create_polygon(self.ship_x, self.ship_y - 20,
                                              self.ship_x - 15, self.ship_y + 20,
                                              self.ship_x + 15, self.ship_y + 20,
                                              fill='#2ecc71', outline='white', width=2)
        
        # Create aliens
        for row in range(4):
            for col in range(8):
                x = col * 70 + 80
                y = row * 50 + 120
                alien = self.canvas.create_rectangle(x, y, x + 40, y + 30,
                                                    fill='#e74c3c', outline='white', width=2)
                self.aliens.append({'id': alien, 'x': x, 'y': y})
        
        self.alien_direction = 1
        
        self.root.bind('<Left>', lambda e: self.move_ship(-20))
        self.root.bind('<Right>', lambda e: self.move_ship(20))
        self.root.bind('<space>', lambda e: self.shoot())
        
        self.game_loop()
        self.alien_loop()
    
    def move_ship(self, dx):
        self.ship_x = max(15, min(self.ship_x + dx, 685))
        self.canvas.coords(self.ship, self.ship_x, self.ship_y - 20,
                          self.ship_x - 15, self.ship_y + 20,
                          self.ship_x + 15, self.ship_y + 20)
    
    def shoot(self):
        bullet = self.canvas.create_rectangle(self.ship_x - 2, self.ship_y - 25,
                                             self.ship_x + 2, self.ship_y - 15,
                                             fill='yellow')
        self.bullets.append({'id': bullet, 'y': self.ship_y - 25})
    
    def alien_loop(self):
        if not self.game_active:
            return
        
        # Move aliens
        move_down = False
        for alien in self.aliens:
            alien['x'] += self.alien_direction * 10
            if alien['x'] <= 0 or alien['x'] >= 660:
                move_down = True
        
        if move_down:
            self.alien_direction *= -1
            for alien in self.aliens:
                alien['y'] += 20
                if alien['y'] >= 600:
                    self.game_over()
                    return
        
        for alien in self.aliens:
            self.canvas.coords(alien['id'], alien['x'], alien['y'],
                             alien['x'] + 40, alien['y'] + 30)
        
        # Random alien shooting
        if self.aliens and random.random() < 0.05:
            alien = random.choice(self.aliens)
            bullet = self.canvas.create_rectangle(alien['x'] + 18, alien['y'] + 30,
                                                 alien['x'] + 22, alien['y'] + 40,
                                                 fill='red')
            self.alien_bullets.append({'id': bullet, 'y': alien['y'] + 40})
        
        self.root.after(200, self.alien_loop)
    
    def game_loop(self):
        if not self.game_active:
            return
        
        # Move player bullets
        for bullet in self.bullets[:]:
            bullet['y'] -= 10
            if bullet['y'] < 0:
                self.canvas.delete(bullet['id'])
                self.bullets.remove(bullet)
            else:
                self.canvas.coords(bullet['id'], self.ship_x - 2, bullet['y'],
                                 self.ship_x + 2, bullet['y'] + 10)
                
                # Check alien hit
                for alien in self.aliens[:]:
                    if (alien['x'] <= self.ship_x <= alien['x'] + 40 and
                        alien['y'] <= bullet['y'] <= alien['y'] + 30):
                        self.canvas.delete(bullet['id'])
                        self.canvas.delete(alien['id'])
                        self.bullets.remove(bullet)
                        self.aliens.remove(alien)
                        self.score += 10
                        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                        break
        
        # Move alien bullets
        for bullet in self.alien_bullets[:]:
            bullet['y'] += 8
            if bullet['y'] > 700:
                self.canvas.delete(bullet['id'])
                self.alien_bullets.remove(bullet)
            else:
                coords = self.canvas.coords(bullet['id'])
                self.canvas.move(bullet['id'], 0, 8)
                
                # Check player hit
                if (self.ship_x - 15 <= coords[0] <= self.ship_x + 15 and
                    self.ship_y - 20 <= bullet['y'] <= self.ship_y + 20):
                    self.game_over()
                    return
        
        # Win condition
        if not self.aliens:
            self.win_game()
            return
        
        self.root.after(30, self.game_loop)
    
    def win_game(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="YOU WIN!", font=('Arial', 32, 'bold'), fill='#2ecc71')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())
    
    def game_over(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="GAME OVER!", font=('Arial', 32, 'bold'), fill='red')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())


# ==================== CATCH THE FALLING GAME ====================
class CatchFallingGame:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.game_active = True
        self.score = 0
        self.missed = 0
        self.falling_items = []
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.canvas = tk.Canvas(self.root, width=700, height=700, bg='#3498db')
        self.canvas.pack()
        
        self.canvas.create_text(350, 30, text="🍎 CATCH THE FALLING", font=('Arial', 24, 'bold'), fill='white')
        self.score_text = self.canvas.create_text(150, 60, text=f"Score: {self.score}",
                                                  font=('Arial', 16), fill='white')
        self.missed_text = self.canvas.create_text(550, 60, text=f"Missed: {self.missed}",
                                                   font=('Arial', 16), fill='white')
        
        # Basket
        self.basket_x = 320
        self.basket_y = 650
        self.basket_width = 80
        self.basket = self.canvas.create_rectangle(self.basket_x, self.basket_y,
                                                   self.basket_x + self.basket_width,
                                                   self.basket_y + 30,
                                                   fill='#e67e22', outline='white', width=3)
        
        self.canvas.bind('<Motion>', self.move_basket)
        self.spawn_item()
        self.game_loop()
    
    def move_basket(self, event):
        self.basket_x = max(0, min(event.x - self.basket_width // 2, 700 - self.basket_width))
        self.canvas.coords(self.basket, self.basket_x, self.basket_y,
                          self.basket_x + self.basket_width, self.basket_y + 30)
    
    def spawn_item(self):
        if not self.game_active:
            return
        x = random.randint(30, 670)
        items = ['🍎', '🍊', '🍌', '🍇', '🍓', '⭐', '💎']
        colors = ['#e74c3c', '#e67e22', '#f1c40f', '#9b59b6', '#e91e63', '#ffd700', '#00bcd4']
        idx = random.randint(0, len(items) - 1)
        
        item = self.canvas.create_text(x, 100, text=items[idx], font=('Arial', 32))
        self.falling_items.append({'id': item, 'x': x, 'y': 100, 'speed': random.randint(3, 6)})
        
        self.root.after(random.randint(800, 1500), self.spawn_item)
    
    def game_loop(self):
        if not self.game_active:
            return
        
        for item in self.falling_items[:]:
            item['y'] += item['speed']
            self.canvas.coords(item['id'], item['x'], item['y'])
            
            # Check catch
            if (self.basket_x <= item['x'] <= self.basket_x + self.basket_width and
                self.basket_y <= item['y'] <= self.basket_y + 30):
                self.canvas.delete(item['id'])
                self.falling_items.remove(item)
                self.score += 10
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            
            # Check missed
            elif item['y'] > 700:
                self.canvas.delete(item['id'])
                self.falling_items.remove(item)
                self.missed += 1
                self.canvas.itemconfig(self.missed_text, text=f"Missed: {self.missed}")
                
                if self.missed >= 10:
                    self.game_over()
                    return
        
        self.root.after(30, self.game_loop)
    
    def game_over(self):
        self.game_active = False
        self.canvas.create_rectangle(150, 250, 550, 450, fill='black', outline='white', width=3)
        self.canvas.create_text(350, 300, text="GAME OVER!", font=('Arial', 32, 'bold'), fill='red')
        self.canvas.create_text(350, 350, text=f"Final Score: {self.score}", font=('Arial', 20), fill='white')
        self.canvas.create_text(350, 400, text="Press any key for menu", font=('Arial', 14), fill='white')
        self.root.bind('<Key>', lambda e: self.return_callback())


# Run the game hub
if __name__ == "__main__":
    root = tk.Tk()
    hub = ArcadeGameHub(root)
    root.mainloop()

