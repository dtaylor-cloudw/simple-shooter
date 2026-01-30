controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (sprites.allOfKind(SpriteKind.Projectile).length < 2) {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, SpaceShip, 0, -50)
        music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprites.destroy(sprite, effects.disintegrate, 500)
    sprites.destroy(otherSprite)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    sprites.destroy(otherSprite2, effects.fire, 500)
    scene.cameraShake(4, 500)
    info.changeLifeBy(-1)
})
let Asteroid: Sprite = null
let projectile: Sprite = null
let SpaceShip: Sprite = null
effects.starField.startScreenEffect()
SpaceShip = sprites.create(assets.image`Player Ship`, SpriteKind.Player)
SpaceShip.setPosition(78, 111)
game.onUpdate(function () {
    controller.moveSprite(SpaceShip, 100, 0)
    SpaceShip.setStayInScreen(true)
})
game.onUpdate(function () {
    game.setGameOverEffect(false, effects.melt)
    game.setGameOverMessage(false, "YOU LOSE!!!!")
})
game.onUpdateInterval(1000, function () {
    Asteroid = sprites.createProjectileFromSide(img`
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
        `, 0, 50)
    Asteroid.x = randint(0, scene.screenWidth())
    Asteroid.setKind(SpriteKind.Enemy)
})
