from .data import get_chapter, get_next


def get_catalogue():
    catalog = {
        'by_category': [
            {
                'category': 'Biography',
                'title1' : 'Abraham Lincoln',
                'title2' : 'Steve Jobs',
                'title3': 'Narendra Modi',
                'thumbNailURL1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Abraham_Lincoln_by_Byers%2C_1858_-_crop.jpg/340px-Abraham_Lincoln_by_Byers%2C_1858_-_crop.jpg',
                'thumbNailURL2': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg/440px-Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg',
                'thumbNailURL3': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Official_portrait_of_the_Prime_Minister_Narendra_Modi%2C_November_2020_%28cropped%29.jpg/440px-Official_portrait_of_the_Prime_Minister_Narendra_Modi%2C_November_2020_%28cropped%29.jpg',
                'properties' : {
                    "title1" : {
                        "fontSize" : "16"
                    },
                    "title2": {
                        "fontSize": "16"
                    },
                    "title3": {
                        "fontSize": "16"
                    },
                    "category" : {
                        "textColor" : "#FFFF00"
                    }
                }
            },
            {
                'category': 'The famous Rockbands',
                'title1': 'The Beatles',
                'title2': 'Radiohead',
                'title3': 'Porcupine',
                'thumbNailURL1': "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/The_Beatles_performing_at_The_Ed_Sullivan_Show_%28cropped_2%29.jpg/2880px-The_Beatles_performing_at_The_Ed_Sullivan_Show_%28cropped_2%29.jpg",
                'thumbNailURL2': "https://upload.wikimedia.org/wikipedia/commons/5/5f/Radiohead_Coachella_2004_cropped.jpg",
                'thumbNailURL3': "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/ColdplayBBC071221_%2853_of_53%29_%2851740659597%29.jpg/2880px-ColdplayBBC071221_%2853_of_53%29_%2851740659597%29.jpg",
                'properties': {
                    "title1": {
                        "fontSize": "16"
                    },
                    "title2": {
                        "fontSize": "16"
                    },
                    "title3": {
                        "fontSize": "16"
                    },
                    "category": {
                        "textColor": "#FFFF00"
                    }
                }
            }
            # {
            #     'category' : 'The famous Rockbands',
            #     'movies' : [
            #         {
            #             'title' : 'The Beatles',
            #             'brief' : '',
            #             'thumbNailURL' : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/The_Beatles_performing_at_The_Ed_Sullivan_Show_%28cropped_2%29.jpg/2880px-The_Beatles_performing_at_The_Ed_Sullivan_Show_%28cropped_2%29.jpg"
            #         },
            #         {
            #             'title': 'Radiohead',
            #             'brief': '',
            #             'thumbNailURL': "https://upload.wikimedia.org/wikipedia/commons/5/5f/Radiohead_Coachella_2004_cropped.jpg"
            #         },
            #         {
            #             'title': 'Radiohead',
            #             'brief': '',
            #             'thumbNailURL': "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/ColdplayBBC071221_%2853_of_53%29_%2851740659597%29.jpg/2880px-ColdplayBBC071221_%2853_of_53%29_%2851740659597%29.jpg"
            #         },
            #         {
            #             'title': 'Radiohead',
            #             'brief': '',
            #             'thumbNailURL': "https://upload.wikimedia.org/wikipedia/commons/c/c0/Porcupine_Tree_%40_Poznan%2C_Poland_2007_04.jpg"
            #         }
            #
            #
            #
            #                 ]
            # }

        ]
    }
    return catalog


def get_movie(movie):
    movie = {
        "Abraham Lincoln": {
            'title': 'Abraham Lincoln',
            'brief': 'The gripping story of Lincoln who started his career as a Store clerk, taught Law to himself and went on to become the President of United States.',
            'thumbNailURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/AbrahamLincolnOilPainting1869Restored.jpg/340px-AbrahamLincolnOilPainting1869Restored.jpg',

            "rating": 4,
            "runTimeMins": 8,
            "peopleReviewed": 1123,
            "favorited": "645",

            'episodes': [
                {
                    "title1": "Episode 1",
                    "title2": "Career",
                    "thumbNailURL" : "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/The_Peacemakers_1868.jpg/560px-The_Peacemakers_1868.jpg",
                    "splash": {
                        "text": "Abraham Lincoln's History",
                        "image": "",
                        "fontSize": 23,
                        "font": "sans-serif",
                        "fontStyle": "bold|italic",
                        "underlined": False
                    },
                    "clips": get_chapter('Career'),
                    "credits": {
                        "text": ""
                    },
                    "next": get_next('Career')
                },
                {
                    "title1": "Episode 2",
                    "title2": "Practicing Law",
                    "thumbNailURL": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Emancipation_proclamation.jpg/560px-Emancipation_proclamation.jpg",
                },
                {
                    "title1": "Episode 3",
                    "title2": "Family and children",
                    "thumbNailURL": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/A%26TLincoln.jpg/384px-A%26TLincoln.jpg",

                },
                {
                    "title1": "Episode 4",
                    "title2": "Presidential candidate",
                    "thumbNailURL": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Lincoln_assassination_slide_c1900_-_Restoration.jpg/440px-Lincoln_assassination_slide_c1900_-_Restoration.jpg",

                }
            ]
        }
    }
    return movie['Abraham Lincoln']

def get_featured_movie_list():
    return {
        "featuredMovies" : [
            {
                "image" : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/The_Beatles_performing_at_The_Ed_Sullivan_Show_%28cropped_2%29.jpg/2880px-The_Beatles_performing_at_The_Ed_Sullivan_Show_%28cropped_2%29.jpg"
            },
            {
                "image" : "https://upload.wikimedia.org/wikipedia/commons/5/5f/Radiohead_Coachella_2004_cropped.jpg"
            },
            {
                "image" : "https://upload.wikimedia.org/wikipedia/commons/c/c0/Porcupine_Tree_%40_Poznan%2C_Poland_2007_04.jpg"
            }
        ]
    }