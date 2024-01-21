from image_and_tile import image, tile
import tile_processing as tp

image1=image("LargeImage.ome.tif",10000,10000)
contour=tp.find_edges(image1.tiles[1])
areas=tp.find_area(contour)
tp.draw_contours(image1.tiles[1],contour,areas)