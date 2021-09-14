import pygame

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
bg = pygame.transform.scale(pygame.image.load("Paint_UI.png"), (800, 500))
win.blit(bg, (0,0))

def check_clear(pos):
    x,y = pos[0], pos[1]
    if 23 < x < 173 and 477 > y > 427:
        win.blit(bg, (0,0))

def check_color(pos, color):
    x,y = pos[0], pos[1]
    if 691 < x < 777 and 495 > y > 409:
        return bg.get_at((x,y))
    return color

def main():
    current_color = (0,0,0)
    run = True
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # checking for if user is holding down mouse
            is_down = True
            while event.type == pygame.MOUSEBUTTONDOWN and is_down:
                pos = pygame.mouse.get_pos()
                win.set_at((pos), current_color[:3])
                for ev in pygame.event.get():
                    if ev.type == pygame.MOUSEBUTTONUP:
                        is_down = False

            # when button is lifted up, check it's position for special click.
            if is_down == False:
                pos = pygame.mouse.get_pos()
                check_clear(pos)
                current_color = check_color(pos, current_color)

main()
