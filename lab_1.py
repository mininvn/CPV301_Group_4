import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode( (1000, 800) )
pygame.display.set_caption("CPV_Lab_1")

gameExit = False
point_1 = 0
point_2 = 0
draw = False
down = False
rect = { "top": 0, "left": 0, "width": 0, "height": 0 }
points = { "a": 0, "b": 0, "c": 0, "d": 0}

gameDisplay.fill(white)
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = False
            down = True
            point_1 = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            point_2 = pygame.mouse.get_pos()
            draw = True
            down = False
        if event.type == pygame.MOUSEMOTION and down:
            pygame.transform.rotate(gameDisplay, 90)
            point_2 = pygame.mouse.get_pos()
            draw = True
        
    if (draw):
        gameDisplay.fill(white)
        rect["top"] = point_1[1]
        rect["left"] = point_1[0]
        rect["width"] = point_2[0] - point_1[0]
        rect["height"] = point_2[1] - point_1[1]
        if (rect["width"] < 0):
            rect["width"] *= -1
            rect["left"] = rect["left"] - rect["width"]
        if (rect["height"] < 0):
            rect["height"] *= -1
            rect["top"] = rect["top"] - rect["height"]
        points["a"] = (rect["left"], rect["top"])
        points["b"] = (rect["left"] + rect["width"], rect["top"])
        points["d"] = (rect["left"] + rect["width"], rect["top"] + rect["height"])
        points["c"] = (rect["left"], rect["top"] + rect["height"])

        pygame.draw.line(gameDisplay, red, points["a"], points["b"])
        pygame.draw.line(gameDisplay, red, points["b"], points["d"])
        pygame.draw.line(gameDisplay, red, points["d"], points["c"])
        pygame.draw.line(gameDisplay, red, points["c"], points["a"])

        draw = False


    pygame.display.update()