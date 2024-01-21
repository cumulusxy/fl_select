import os
import pyvips

class image:
    def __init__(self, path, tile_width=False, tile_height=False, name=False):
        self.im_obj = pyvips.Image.new_from_file(path)
        self.tiles = []
        if name:
            self.name = name
        else:
            self.name = path
        if tile_width or tile_height:
            self.segment_and_save_image(tile_width, tile_height,f"temp_tiles_{self.name}")
        else:
            self.segment_and_save_image(self.im_obj.width, self.im_obj.height, f"temp_tiles_{self.name}")


    def segment_and_save_image(self, tile_width, tile_height, output_directory="temp_tiles"):
        # Load the image
        # Calculate the number of tiles in each dimension
        n_tiles_x = (self.im_obj.width + tile_width - 1) // tile_width
        n_tiles_y = (self.im_obj.height + tile_height - 1) // tile_height
        os.mkdir(output_directory)
        # Segment and save each tile
        for x in range(n_tiles_x):
            for y in range(n_tiles_y):
                # Calculate the dimensions of the tile
                left = x * tile_width
                top = y * tile_height
                width = min(tile_width, self.im_obj.width - left)
                height = min(tile_height, self.im_obj.height - top)

                # Crop the image to create the tile
                tile_im = self.im_obj.crop(left, top, width, height)

                # Save the tile
                path=f"{output_directory}/tile_{x}_{y}.png"
                tile_im.write_to_file(path)
                self.tiles.append(tile(path, (x,y)))

class tile:
    def __init__(self,  path, coordinate):
        self.path=path
        self.x,self.y=coordinate

    def get_relative_coordinate(self,image_size):
        width,height=image_size
        self.relative_coordinate= self.x/width, self.y/height


