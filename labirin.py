import pygame
import random
import sys
import time

# Ukuran & warna
TILE_SIZE = 24
GRID_WIDTH = 31
GRID_HEIGHT = 31
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 135, 245)
GREEN = (0, 200, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (173, 216, 230)

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maze = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def in_bounds(x, y):
    return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT

def generate_maze(x, y):
    maze[y][x] = 0
    directions = DIRS[:]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if in_bounds(nx, ny) and maze[ny][nx] == 1:
            maze[y + dy][x + dx] = 0
            generate_maze(nx, ny)

generate_maze(1, 1)
start = (1, 1)
end = (GRID_WIDTH - 2, GRID_HEIGHT - 2)

# Gabungan semua pertanyaan (lama + baru)
door_questions = {
    (5, 5): {
        "question": "Apa kepanjangan dari CPU?",
        "options": ["Central Processing Unit", "Control Program Unit", "Computer Personal Unit", "Computer Unit Processing"],
        "answer": "Central Processing Unit"
    },
    (11, 7): {
        "question": "Apa fungsi utama RAM?",
        "options": ["Menyimpan sementara", "Menyimpan permanen", "Menjalankan harddisk", "Menyimpan data internet"],
        "answer": "Menyimpan sementara"
    },
    (3, 15): {
        "question": "Bahasa pemrograman paling umum untuk AI?",
        "options": ["Java", "Python", "C++", "JavaScript"],
        "answer": "Python"
    },
    (13, 13): {
        "question": "Singkatan dari HTML?",
        "options": ["HyperText Markup Language", "HighText Machine Language", "HyperTool Modern Language", "Hyperlink Text Markup Language"],
        "answer": "HyperText Markup Language"
    },
    (7, 2): {
        "question": "Apa yang dimaksud dengan 'debugging' dalam pemrograman?",
        "options": ["Menemukan dan memperbaiki kesalahan dalam kode", "Menyusun kode", "Mencetak hasil program", "Mempercepat program"],
        "answer": "Menemukan dan memperbaiki kesalahan dalam kode"
    },
    (15, 10): {
        "question": "Apa kepanjangan dari CSS?",
        "options": ["Cascading Style Sheets", "Central Styling Sheets", "Code Style Syntax", "Computer Style Sheets"],
        "answer": "Cascading Style Sheets"
    },
    (18, 16): {
        "question": "Apa itu Git?",
        "options": ["Sistem version control", "Bahasa pemrograman", "Editor teks", "Platform pengembangan aplikasi"],
        "answer": "Sistem version control"
    },
    (9, 9): {
        "question": "Apa yang dimaksud dengan 'cloud computing'?",
        "options": ["Pengolahan data di internet", "Penyimpanan data di server lokal", "Komunikasi dengan server melalui aplikasi", "Pemrograman perangkat keras"],
        "answer": "Pengolahan data di internet"
    },
    (20, 20): {
        "question": "Protokol utama transfer halaman web?",
        "options": ["FTP", "HTTP", "IP", "SMTP"],
        "answer": "HTTP"
    },
    # Tambahan pertanyaan
    (23, 5): {
        "question": "Apa itu IP Address?",
        "options": ["Alamat perangkat di jaringan", "Nama pengguna internet", "Kata sandi WiFi", "Kode sistem operasi"],
        "answer": "Alamat perangkat di jaringan"
    },
    (25, 7): {
        "question": "Apa kepanjangan dari URL?",
        "options": ["Uniform Resource Locator", "Unified Resource Link", "Universal Routing Language", "Universal Resource Load"],
        "answer": "Uniform Resource Locator"
    },
    (17, 3): {
        "question": "Apa itu sistem operasi (OS)?",
        "options": ["Pengelola perangkat keras & lunak", "Program desain grafis", "Perangkat keras komputer", "Bahasa pemrograman"],
        "answer": "Pengelola perangkat keras & lunak"
    },
    (6, 20): {
        "question": "Apa itu browser?",
        "options": ["Aplikasi untuk menjelajahi internet", "Alat pemrograman", "Perangkat keras jaringan", "Program antivirus"],
        "answer": "Aplikasi untuk menjelajahi internet"
    },
    (10, 25): {
        "question": "Contoh bahasa markup adalah?",
        "options": ["HTML", "Python", "C++", "Java"],
        "answer": "HTML"
    },
    (14, 22): {
        "question": "Apa fungsi dari compiler?",
        "options": ["Menerjemahkan kode ke bahasa mesin", "Menjalankan server", "Menyimpan database", "Menggambar UI"],
        "answer": "Menerjemahkan kode ke bahasa mesin"
    },
    (22, 17): {
        "question": "Apa itu firewall?",
        "options": ["Perlindungan terhadap akses tidak sah", "Perangkat keras penyimpan data", "Jenis antivirus", "Jaringan lokal"],
        "answer": "Perlindungan terhadap akses tidak sah"
    },
    (26, 10): {
        "question": "Apa itu database?",
        "options": ["Kumpulan data yang terorganisir", "Bahasa pemrograman", "Sistem operasi", "Program game"],
        "answer": "Kumpulan data yang terorganisir"
    },
    (27, 15): {
        "question": "Bahasa pemrograman untuk web frontend?",
        "options": ["JavaScript", "Python", "PHP", "C#"],
        "answer": "JavaScript"
    },
    (20, 27): {
        "question": "Apa itu API?",
        "options": ["Antarmuka pemrograman aplikasi", "Aplikasi pemutar internet", "Algoritma penyimpanan informasi", "Alamat proxy internal"],
        "answer": "Antarmuka pemrograman aplikasi"
    }
}

# Tambahkan pintu ke maze
doors = list(door_questions.keys())
for dx, dy in doors:
    maze[dy][dx] = 2

# Inisialisasi pygame
pygame.init()
WIDTH = GRID_WIDTH * TILE_SIZE
HEIGHT = GRID_HEIGHT * TILE_SIZE + 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Edu Maze")
font = pygame.font.SysFont("Arial", 18)

# Ganti dengan file gambar sprite kamu
player_sprite = pygame.image.load("aaa.png")
player_sprite = pygame.transform.scale(player_sprite, (TILE_SIZE, TILE_SIZE))

player_pos = list(start)
clock = pygame.time.Clock()
start_time = time.time()
TIME_LIMIT = 60

show_question = False
current_question = None
selected_pos = None
incorrect_answers = 0

def draw_maze():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if maze[y][x] == 0:
                pygame.draw.rect(screen, WHITE, rect)
            elif maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            elif maze[y][x] == 2:
                pygame.draw.rect(screen, ORANGE, rect)

def draw_player():
    screen.blit(player_sprite, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

def draw_goal():
    pygame.draw.rect(screen, GREEN, pygame.Rect(end[0] * TILE_SIZE, end[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_timer():
    elapsed = int(time.time() - start_time)
    remaining = max(0, TIME_LIMIT - elapsed)
    text = font.render(f"Time Left: {remaining}s", True, RED)
    screen.blit(text, (10, HEIGHT - 50))
    return remaining

def draw_question_box():
    if current_question:
        q = door_questions[current_question]
        box = pygame.Rect(0, GRID_HEIGHT * TILE_SIZE, WIDTH, 60)
        pygame.draw.rect(screen, LIGHT_BLUE, box)
        screen.blit(font.render(f"{q['question']}", True, BLACK), (10, GRID_HEIGHT * TILE_SIZE + 5))
        for i, opt in enumerate(q['options']):
            screen.blit(font.render(f"{i + 1}. {opt}", True, BLACK), (10, GRID_HEIGHT * TILE_SIZE + 25 + i * 15))

# Game loop
running = True
while running:
    clock.tick(15)
    remaining_time = draw_timer()
    if remaining_time <= 0:
        print("\n⏰ Waktu habis! Game Over.")
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if show_question and event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                jawaban = int(event.unicode) - 1
                correct = door_questions[current_question]['answer']
                if door_questions[current_question]['options'][jawaban] == correct:
                    maze[selected_pos[1]][selected_pos[0]] = 0
                    print("✅ Benar!")
                else:
                    incorrect_answers += 1
                    print(f"❌ Salah! Salah {incorrect_answers} kali.")
                show_question = False
                current_question = None

    if incorrect_answers >= 3:
        print("❌ Kamu telah salah menjawab 3 kali. Game Over!")
        pygame.quit()
        sys.exit()

    keys = pygame.key.get_pressed()
    if not show_question:
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]: dx = -1
        elif keys[pygame.K_RIGHT]: dx = 1
        elif keys[pygame.K_UP]: dy = -1
        elif keys[pygame.K_DOWN]: dy = 1

        x, y = player_pos
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny):
            if maze[ny][nx] == 0:
                player_pos = [nx, ny]
            elif maze[ny][nx] == 2:
                show_question = True
                current_question = (nx, ny)
                selected_pos = (nx, ny)

    if tuple(player_pos) == end and maze[end[1]][end[0]] == 0:
        print("🏁 Selamat! Kamu menyelesaikan labirin!")
        pygame.quit()
        sys.exit()

    screen.fill(WHITE)
    draw_maze()
    draw_goal()
    draw_player()
    draw_timer()
    draw_question_box()
    pygame.display.flip()
