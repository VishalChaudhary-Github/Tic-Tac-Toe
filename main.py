import pygame

pygame.init()

game_window = pygame.display.set_mode((500, 500))
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Tic-Tac-Toe')

cross = pygame.image.load('cross.png')
circle = pygame.image.load('circle.png')

clock = pygame.time.Clock()

surface = pygame.Surface((128, 128))
surface.fill((139, 223, 209))

area1 = (19, 19)
area2 = (185, 19)
area3 = (351, 19)
area4 = (19, 185)
area5 = (185, 185)
area6 = (351, 185)
area7 = (19, 351)
area8 = (185, 351)
area9 = (351, 351)

values_list = []
winning_values_dict = dict()

pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def winner():
    set1 = set()
    if 'area1' in winning_values_dict and 'area2' in winning_values_dict and 'area3' in winning_values_dict:
        set1.add(winning_values_dict['area1'])
        set1.add(winning_values_dict['area2'])
        set1.add(winning_values_dict['area3'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()

    if 'area4' in winning_values_dict and 'area5' in winning_values_dict and 'area6' in winning_values_dict:
        set1.add(winning_values_dict['area4'])
        set1.add(winning_values_dict['area5'])
        set1.add(winning_values_dict['area6'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if 'area7' in winning_values_dict and 'area8' in winning_values_dict and 'area9' in winning_values_dict:
        set1.add(winning_values_dict['area7'])
        set1.add(winning_values_dict['area8'])
        set1.add(winning_values_dict['area9'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if 'area1' in winning_values_dict and 'area4' in winning_values_dict and 'area7' in winning_values_dict:
        set1.add(winning_values_dict['area1'])
        set1.add(winning_values_dict['area4'])
        set1.add(winning_values_dict['area7'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if 'area2' in winning_values_dict and 'area5' in winning_values_dict and 'area8' in winning_values_dict:
        set1.add(winning_values_dict['area2'])
        set1.add(winning_values_dict['area5'])
        set1.add(winning_values_dict['area8'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if 'area3' in winning_values_dict and 'area6' in winning_values_dict and 'area9' in winning_values_dict:
        set1.add(winning_values_dict['area3'])
        set1.add(winning_values_dict['area6'])
        set1.add(winning_values_dict['area9'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if 'area1' in winning_values_dict and 'area5' in winning_values_dict and 'area9' in winning_values_dict:
        set1.add(winning_values_dict['area1'])
        set1.add(winning_values_dict['area5'])
        set1.add(winning_values_dict['area9'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if 'area3' in winning_values_dict and 'area5' in winning_values_dict and 'area7' in winning_values_dict:
        set1.add(winning_values_dict['area3'])
        set1.add(winning_values_dict['area5'])
        set1.add(winning_values_dict['area7'])
        if len(set1) == 1:
            if 'cross' in set1:
                return 'PLAYER 1'
            elif 'circle' in set1:
                return 'PLAYER 2'
        set1.clear()
    if len(winning_values_dict) == 9:
        return 'DRAW'


def calculate(pos, button):
    x_pos, y_pos = pos
    if (0 < x_pos < 166) and (0 < y_pos < 166):  # A1
        if button == 1:
            game_window.blit(surface, area1)
            game_window.blit(cross, area1)
            return 'area1', 'cross'
        elif button == 2:
            game_window.blit(surface, area1)
            return 'area1', None
        elif button == 3:
            game_window.blit(surface, area1)
            game_window.blit(circle, area1)
            return 'area1', 'circle'

    elif (166 < x_pos < 332) and (0 < y_pos < 166):  # A2
        if button == 1:
            game_window.blit(surface, area2)
            game_window.blit(cross, area2)
            return 'area2', 'cross'
        elif button == 2:
            game_window.blit(surface, area2)
            return 'area2', None
        elif button == 3:
            game_window.blit(surface, area2)
            game_window.blit(circle, area2)
            return 'area2', 'circle'

    elif (332 < x_pos < 500) and (0 < y_pos < 166):  # A3
        if button == 1:
            game_window.blit(surface, area3)
            game_window.blit(cross, area3)
            return 'area3', 'cross'
        elif button == 2:
            game_window.blit(surface, area3)
            return 'area3', None
        elif button == 3:
            game_window.blit(surface, area3)
            game_window.blit(circle, area3)
            return 'area3', 'circle'

    elif (0 < x_pos < 166) and (166 < y_pos < 332):  # A4
        if button == 1:
            game_window.blit(surface, area4)
            game_window.blit(cross, area4)
            return 'area4', 'cross'
        elif button == 2:
            game_window.blit(surface, area4)
            return 'area4', None
        elif button == 3:
            game_window.blit(surface, area4)
            game_window.blit(circle, area4)
            return 'area4', 'circle'

    elif (166 < x_pos < 332) and (166 < y_pos < 332):  # A5
        if button == 1:
            game_window.blit(surface, area5)
            game_window.blit(cross, area5)
            return 'area5', 'cross'
        elif button == 2:
            game_window.blit(surface, area5)
            return 'area5', None
        elif button == 3:
            game_window.blit(surface, area5)
            game_window.blit(circle, area5)
            return 'area5', 'circle'

    elif (332 < x_pos < 500) and (166 < y_pos < 332):  # A6
        if button == 1:
            game_window.blit(surface, area6)
            game_window.blit(cross, area6)
            return 'area6', 'cross'
        elif button == 2:
            game_window.blit(surface, area6)
            return 'area6', None
        elif button == 3:
            game_window.blit(surface, area6)
            game_window.blit(circle, area6)
            return 'area6', 'circle'

    elif (0 < x_pos < 166) and (332 < y_pos < 500):  # A7
        if button == 1:
            game_window.blit(surface, area7)
            game_window.blit(cross, area7)
            return 'area7', 'cross'
        elif button == 2:
            game_window.blit(surface, area7)
            return 'area7', None
        elif button == 3:
            game_window.blit(surface, area7)
            game_window.blit(circle, area7)
            return 'area7', 'circle'

    elif (166 < x_pos < 332) and (332 < y_pos < 500):  # A8
        if button == 1:
            game_window.blit(surface, area8)
            game_window.blit(cross, area8)
            return 'area8', 'cross'
        elif button == 2:
            game_window.blit(surface, area8)
            return 'area8', None
        elif button == 3:
            game_window.blit(surface, area8)
            game_window.blit(circle, area8)
            return 'area8', 'circle'

    elif (332 < x_pos < 500) and (332 < y_pos < 500):  # A9
        if button == 1:
            game_window.blit(surface, area9)
            game_window.blit(cross, area9)
            return 'area9', 'cross'
        elif button == 2:
            game_window.blit(surface, area9)
            return 'area9', None
        elif button == 3:
            game_window.blit(surface, area9)
            game_window.blit(circle, area9)
            return 'area9', 'circle'


def main():
    game_window.fill((139, 223, 209))

    # Game Loop 1

    running = True
    while running:
        clock.tick(60)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                values_list.append((event.pos, event.button))

        # Creating a Background lines
        pygame.draw.line(game_window, (255, 255, 255), (166, 0), (166, 500), 1)
        pygame.draw.line(game_window, (255, 255, 255), (332, 0), (332, 500), 1)
        pygame.draw.line(game_window, (255, 255, 255), (0, 166), (500, 166), 1)
        pygame.draw.line(game_window, (255, 255, 255), (0, 332), (500, 332), 1)

        # Drawing Cris-Cross
        for pos_, button_ in values_list:
            av = calculate(pos_, button_)
            area, value = av
            if value is None:
                winning_values_dict.pop(area, 'Not in the dict')
            else:
                winning_values_dict[area] = value
        values_list.clear()
        player = winner()
        if player is not None:
            return player

        # Updating the display
        pygame.display.flip()


winning_player = main()
game_window.fill((139, 223, 209))

font = pygame.font.SysFont('calibri', 22, bold=True, italic=True)
if winning_player == 'DRAW':
    text = font.render(f'MATCH {winning_player}', True, (255, 255, 255))
else:
    text = font.render(f'WINNER - {winning_player}', True, (255, 255, 255))

pygame.mixer.music.stop()

# Game Loop 2

running2 = True
while running2:
    clock.tick(30)

    # Event Handling
    for event2 in pygame.event.get():
        if event2.type == pygame.QUIT:
            running2 = False

    # Rendering the graphics
    game_window.blit(text, (180, 225))

    # updating the display
    pygame.display.flip()

pygame.quit()