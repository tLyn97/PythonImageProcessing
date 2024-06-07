import tensorflow as tf
import numpy as np
import ReadImage

def parse_csvline(csv_row, image_shape, default_list):
	filename,label = tf.io.decode_csv(csv_row,default_list)
	img=read_and_decode(filename,image_shape)
	return img,label

 
