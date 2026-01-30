def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            . . . . . . . 7 7 . . . . . . .
            """),
        mySprite,
        0,
        -50)
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite, effects.disintegrate, 500)
    sprites.destroy(otherSprite)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Asteroid: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . c d . . . . . . .
        . . . . . . . c d . . . . . . .
        . . . . . . . c d . . . . . . .
        . . . . . . . c b . . . . . . .
        . . . . . . . f f . . . . . . .
        . . . . . . . c 3 . . . . . . .
        . . . . . . . f f . . . . . . .
        . . . . . . . 8 3 . . . . . . .
        . . . . . . 8 8 1 a . . . . . .
        . . . . . . 8 3 1 a . . . . . .
        . . . . . c c c a a a . . . . .
        . . . . 8 8 3 3 3 1 a a . . . .
        . . 8 f f f c c a a f f a a . .
        . 8 8 8 8 a a 3 3 3 3 1 3 a a .
        8 8 8 8 8 8 a a 3 3 3 1 3 3 a a
        8 8 8 8 8 8 a a 3 3 3 3 1 3 a a
        """),
    SpriteKind.player)
mySprite.set_position(78, 111)
controller.move_sprite(mySprite, 100, 0)
mySprite.set_stay_in_screen(True)

def on_update_interval():
    global Asteroid
    Asteroid = sprites.create_projectile_from_side(img("""
            . . . . . c c b b b . . . . . .
            . . . . c b d d d d b . . . . .
            . . . . c d d d d d d b b . . .
            . . . . c d d d d d d d d b . .
            . . . c b b d d d d d d d b . .
            . . . c b b d d d d d d d b . .
            . c c c c b b b b d d d b b b .
            . c d d b c b b b b b b b b d b
            c b b d d d b b b b b d d b d b
            c c b b d d d d d d d b b b d c
            c b c c c b b b b b b b d d c c
            c c b b c c c c b d d d b c c b
            . c c c c c c c c c c c b b b b
            . . c c c c c b b b b b b b c .
            . . . . . . c c b b b b c c . .
            . . . . . . . . c c c c . . . .
            """),
        0,
        50)
    Asteroid.x = randint(0, scene.screen_width())
    Asteroid.set_kind(SpriteKind.enemy)
game.on_update_interval(1000, on_update_interval)
