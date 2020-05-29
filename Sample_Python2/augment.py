    # -*- coding: utf-8 -*-
    """
    Created on Mon Feb  3 14:39:14 2020

    @author: 100119
    """

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
# keras.preprocessing.image.ImageDataGenerator(featurewise_center=False, samplewise_center=False,\
#                                              featurewise_std_normalization=False, samplewise_std_normalization=False,
#                                              zca_whitening=False, zca_epsilon=1e-06, rotation_range=0, width_shift_range=0.0, height_shift_range=0.0,\
#                                              brightness_range=None, shear_range=0.0, zoom_range=0.0,\
#                                              channel_shift_range=0.0, fill_mode='nearest', cval=0.0, horizontal_flip=False,\
#                                              vertical_flip=False, rescale=None, preprocessing_function=None, data_format='channels_last', \
#                                              validation_split=0.0, interpolation_order=1, dtype='float32')

datagen = ImageDataGenerator(
            # featurewise_center = True,
            # featurewise_std_normalization=True,
            rotation_range=0,
            width_shift_range=0.01,
            height_shift_range=0.01,
            shear_range=0.1,
            zoom_range=0.2,
            #horizontal_flip=True,
            fill_mode='nearest'
            )
directory = 'C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/DATA_SET/ORIGINAL_DATA/FORMAT_14'
for filename in os.listdir(directory):
    img = load_img(directory+"/"+filename)  
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    j = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/vidya/DATA_SET/AUG_IMAGES/14', save_prefix="FORMAT_14_", save_format='jpg'):
        i += 1
        j += 1
        if i >100:
            break  # otherwise the generator would loop indefinitely