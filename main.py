import arcade

#variabler
BREDDE = 800
HOEJDE = 600

CHARACTER_SCALING = 0.3

TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.5
PLAYER_JUMP_SPEED = 20

#Class til kreationen af cirklerne
class Cirkel:
    def __init__(self, centrumx,centrumy, radius, farve, tyk):
        self.centrumx = centrumx
        self.centrumy = centrumy
        self.radius = radius
        self.farve = farve
        self.tyk = tyk
    def tegn(self):
        arcade.draw_circle_outline(BREDDE / 2-50, HOEJDE / 2+50, 50, arcade.csscolor.SADDLE_BROWN, 3)
        arcade.draw_circle_filled(BREDDE / 2-50, HOEJDE / 2+50, 49, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(BREDDE / 2-50, HOEJDE / 2+50, 5, arcade.csscolor.DARK_GREEN)



#Dette er skitsen jeg begyndte med at lave, for at have en ide om, hvor mine sprites skulle befindes sig.

#class Firkant:
 #   def __init__(self,platx, platy, platb,plath,farve):
  #      self.platx = platx
   #     self.platy = platy
    #    self.platb = platb
     #   self.plath = plath
      #  self.farve = farve
    #def tegn(self):
     #   arcade.draw_rectangle_filled(800,250,600,25,arcade.csscolor.SADDLE_BROWN)
      #  arcade.draw_rectangle_filled(85, 400, 200, 25, arcade.csscolor.SADDLE_BROWN)


#En class til størstedelen af spillet
class Vindue(arcade.Window):
    def __init__(self,width, height, title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
        self.background = arcade.load_texture("detailed-jungle-background_23-2148953379_11zon.jpeg")
        self.wall_list = None
        self.player_list = None

        self.scene = None

        self.physics_engine = None

    def setup(self):
#        self.firkant = Firkant(400,400,400,400,arcade.csscolor.RED)
        self.cirkel = Cirkel(BREDDE / 2, HOEJDE / 2, 50, arcade.csscolor.SADDLE_BROWN, 3)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)


        self.scene = arcade.Scene()

        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)


        image_source = "e7e3dcd6f5d7068.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 465
        self.scene.add_sprite("Player", self.player_sprite)




        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 200, 64):
            wall = arcade.Sprite(":resources:images/tiles/bridgeA.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)
            self.scene.add_sprite("Walls", wall)

        for x in range(500, 800, 64):
            wall = arcade.Sprite(":resources:images/tiles/bridgeA.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
            self.scene.add_sprite("Walls", wall)

            self.physics_engine = arcade.PhysicsEngineSimple(
                self.player_sprite, self.scene.get_sprite_list("Walls")
            )

            self.physics_engine = arcade.PhysicsEnginePlatformer(
                self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
            )



    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(BREDDE/2, HOEJDE/2, BREDDE, HOEJDE, self.background)
        self.cirkel.tegn()
#        self.firkant.tegn()

        self.wall_list.draw()
        self.player_list.draw()

        self.scene.draw()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y= PLAYER_JUMP_SPEED
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        self.physics_engine.update()

def main():
    vindue = Vindue(BREDDE,HOEJDE,"WORD")
    vindue.setup()
    arcade.run()

main()