import pygame
import sys
import random

def show_start_screen():
    screen.fill((255, 248, 220))  # Fill the screen with white

    # Load and display the start screen image
    start_image = pygame.image.load('The Animal Name Game/Animal_pics/rada.jpg')
    start_image_rect = start_image.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
    screen.blit(start_image, start_image_rect)

    # Display some explanation text
    font = pygame.font.Font(None, 40)
    text_lines = [
        "Здравей Рада!",
        "Натисни 'Enter' за да започнеш играта!"
    ]
    for i, line in enumerate(text_lines):
        text = font.render(line, True, (0, 0, 0))  # Black text
        text_rect = text.get_rect(center=(screen_width // 2, screen_height - 100 + i * 50))
        screen.blit(text, text_rect)

    pygame.display.flip()

    # Wait for user to press the Enter key to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def handle_animal_display(pressed_key):
    animal_names = animals_multilingual[pressed_key]
    color = random.choice(list(colors.values()))
    font = pygame.font.Font(None, 64)

    # Load the corresponding animal image in WebP format
    try:
        animal_image = pygame.image.load(image_path + animal_names['English'] + '.webp')
    except FileNotFoundError:
        animal_image = default_image

    # Display the first letter large
    letter_font = pygame.font.Font(None, 200)
    letter_text = letter_font.render(pressed_key.upper(), True, color)
    letter_rect = letter_text.get_rect(center=(screen_width / 2 - 300, screen_height / 2))
    screen.blit(letter_text, letter_rect)

    # Display the image
    screen.blit(pygame.transform.scale(animal_image, (400, 400)), (screen_width / 2 - 200, screen_height / 2 - 200))

    # Display animal names
    start_y = 50
    for i, (language, name) in enumerate(animal_names.items(), start=1):
        text = font.render(f"{language}: {name}", True, color)
        text_rect = text.get_rect(center=(screen_width / 2, start_y + (i - 1) * (64 + 10)))
        screen.blit(text, text_rect)

def handle_default_display():
    # Display a default message and image if the key is not an animal letter
    default_font = pygame.font.Font(None, 64)
    default_text = default_font.render("Е няма такова животно!", True, colors['red'])
    default_text_rect = default_text.get_rect(center=(screen_width / 2, 100))
    screen.blit(default_text, default_text_rect)
    screen.blit(pygame.transform.scale(default_image, (400, 400)), (screen_width / 2 - 200, screen_height / 2 - 200))

# Initialize pygame
pygame.init()

# Retrieve and set the display information
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Animal Name Game')

# Define colors
colors = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'purple': (128, 0, 128)
}

# Check path to the images directory to use "Animal_pics" subfolder!
image_path = 'The Animal Name Game/Animal_pics/'

# Load a default image for non-animal-key presses in WebP format
default_image = pygame.image.load(image_path + 'default.webp')

# Animal names by letter in DE/EN/BG
animals_multilingual = {    
    'a': {'Deutsch': 'Ameisenbär', 'English': 'Anteater', 'Български': 'Мравояд'},
    'b': {'Deutsch': 'Biber', 'English': 'Beaver', 'Български': 'Бобър'},
    'c': {'Deutsch': 'Chamäleon', 'English': 'Chameleon', 'Български': 'Хамелеон'},
    'd': {'Deutsch': 'Delfin', 'English': 'Dolphin', 'Български': 'Делфин'},
    'e': {'Deutsch': 'Elefant', 'English': 'Elephant', 'Български': 'Слон'},
    'f': {'Deutsch': 'Fuchs', 'English': 'Fox', 'Български': 'Лисица'},
    'g': {'Deutsch': 'Giraffe', 'English': 'Giraffe', 'Български': 'Жираф'},
    'h': {'Deutsch': 'Hai', 'English': 'Shark', 'Български': 'Акула'},
    'i': {'Deutsch': 'Igel', 'English': 'Hedgehog', 'Български': 'Таралеж'},
    'j': {'Deutsch': 'Jaguar', 'English': 'Jaguar', 'Български': 'Ягуар'},
    'k': {'Deutsch': 'Koala', 'English': 'Koala', 'Български': 'Коала'},
    'l': {'Deutsch': 'Löwe', 'English': 'Lion', 'Български': 'Лъв'},
    'm': {'Deutsch': 'Murmeltier', 'English': 'Marmot', 'Български': 'Мармот'},
    'n': {'Deutsch': 'Nashorn', 'English': 'Rhinoceros', 'Български': 'Носорог'},
    'o': {'Deutsch': 'Otter', 'English': 'Otter', 'Български': 'Видра'},
    'p': {'Deutsch': 'Pinguin', 'English': 'Penguin', 'Български': 'Пингвин'},
    'q': {'Deutsch': 'Qualle', 'English': 'Jellyfish', 'Български': 'Медуза'},
    'r': {'Deutsch': 'Reh', 'English': 'Deer', 'Български': 'Елен'},
    's': {'Deutsch': 'Schlange', 'English': 'Snake', 'Български': 'Змия'},
    't': {'Deutsch': 'Tiger', 'English': 'Tiger', 'Български': 'Тигър'},
    'u': {'Deutsch': 'Uhu', 'English': 'Eagle Owl', 'Български': 'Бухал'},
    'v': {'Deutsch': 'Vogelstrauß', 'English': 'Common ostrich', 'Български': 'Щраус'},
    'w': {'Deutsch': 'Wal', 'English': 'Whale', 'Български': 'Кит'},
    'x': {'Deutsch': 'Xiphias', 'English': 'Swordfish', 'Български': 'Риба меч'},
    'y': {'Deutsch': 'Yak', 'English': 'Yak', 'Български': 'Як'},  # not a lot of choice for animal with Y
    'z': {'Deutsch': 'Zebra', 'English': 'Zebra', 'Български': 'Зебра'}
}

show_start_screen()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                screen.fill((255, 248, 220))
                pressed_key = pygame.key.name(event.key)
                
                if pressed_key in animals_multilingual:
                    handle_animal_display(pressed_key)
                else:
                    handle_default_display()

    pygame.display.flip()

pygame.quit()
sys.exit()
