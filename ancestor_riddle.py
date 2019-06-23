"""
Hungry Horace was looking through the family photograph album,
which has a photo of each of his parent, each of his grandparents,
all the way up to each of his great-great-great-grandparents.

How many photos is that?
"""

PHOTOS = 2

## The more long winded approach.

# def family_tree(generations):
#     photos = {}
#     number_of_photos = 0

#     # parents
#     # grandparents
#     # great-gp
#     # great-great-gp
#     # great-great-great-gp

#     for generation in range(1, generations + 1):
#         number_of_photos_for_this_generation = PHOTOS

#         if generation != 1:
#             number_of_photos_for_this_generation = photos[generation - 1] * 2

#         photos[generation] = number_of_photos_for_this_generation
#         number_of_photos += number_of_photos_for_this_generation
    
#     print("The total number of photos will be: " + str(number_of_photos))

def family_tree(generations):
    number_of_photos = 0

    for generation in range(1, generations + 1):

        if generation is 1:
            number_of_photos = PHOTOS
        else:
            number_of_photos = number_of_photos * 2 + PHOTOS
    
    print("The total number of photos will be: " + str(number_of_photos))

if __name__ == '__main__':
    family_tree(5)