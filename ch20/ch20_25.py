# Train neural network
network.fit_generator(augment_images,
                      #Number of times to call the generator for each epoch
                      steps_per_epoch=2000,
                      # Number of epochs
                      epochs=5,
                      # Test data generator
                      validation_data=augment_images_test,
                      # Number of items to call the generator
                      # for each test epoch
                      validation_steps=800)