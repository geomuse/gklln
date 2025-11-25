import pygame
import random

pygame.init()

# 画面尺寸
WIDTH, HEIGHT = 900, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump")

clock = pygame.time.Clock()


# =========== 游戏参数 ===========
GRAVITY = 1
GROUND_Y = 300
DINO_X = 80


# =========== 恐龙类 ===========
class Dino:
    def __init__(self):
        self.x = DINO_X
        self.y = GROUND_Y
        self.width = 40
        self.height = 50

        self.vel_y = 0
        self.is_jumping = False

        # 跑步动画
        self.run_frame = 0

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -15        # 跳跃力度
            self.is_jumping = True

    def update(self):
        # 奔跑动画（简单两帧）
        self.run_frame = (self.run_frame + 1) % 20

        # 处理跳跃
        self.y += self.vel_y
        self.vel_y += GRAVITY

        if self.y >= GROUND_Y:
            self.y = GROUND_Y
            self.is_jumping = False
            self.vel_y = 0

    def draw(self, sc):
        color = (255, 255, 255)
        pygame.draw.rect(sc, color, (self.x, self.y - self.height, self.width, self.height))


# =========== 障碍物类 ===========
class Cactus:
    def __init__(self):
        self.width = 30
        self.height = random.choice([40, 60])
        self.x = WIDTH
        self.y = GROUND_Y

        self.speed = 8

    def update(self):
        self.x -= self.speed

    def draw(self, sc):
        pygame.draw.rect(sc, (0, 255, 0), (self.x, self.y - self.height, self.width, self.height))

    def off_screen(self):
        return self.x < -self.width

    def rect(self):
        return pygame.Rect(
            self.x, self.y - self.height, self.width, self.height
        )


# =========== 主游戏循环 ===========
def main():
    dino = Dino()
    obstacles = []
    spawn_timer = 0
    score = 0
    running = True

    font = pygame.font.SysFont(None, 40)

    while running:
        clock.tick(60)
        score += 0.1

        # ====== 事件处理 ======
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 按键跳跃
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        # ====== 更新恐龙 ======
        dino.update()

        # ====== 障碍物生成 ======
        spawn_timer += 1
        if spawn_timer > random.randint(60, 120):  # 每 ~1-2 秒生成一个障碍
            obstacles.append(Cactus())
            spawn_timer = 0

        # ====== 更新障碍物 ======
        for cactus in obstacles:
            cactus.update()

        # 移除超出画面的障碍物
        obstacles = [c for c in obstacles if not c.off_screen()]

        # ====== 碰撞检测 ======
        dino_rect = pygame.Rect(
            dino.x, dino.y - dino.height, dino.width, dino.height
        )

        for cactus in obstacles:
            if dino_rect.colliderect(cactus.rect()):
                print("Game Over! Score:", int(score))
                running = False

        # ====== 画面渲染 ======
        screen.fill((30, 30, 30))  # 黑色背景

        # 地面
        pygame.draw.line(screen, (255, 255, 255), (0, GROUND_Y + 1), (WIDTH, GROUND_Y + 1), 3)

        # 恐龙与障碍物
        dino.draw(screen)

        for cactus in obstacles:
            cactus.draw(screen)

        # 分数显示
        score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_text, (650, 20))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
