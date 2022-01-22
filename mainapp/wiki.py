from .data import get_chapter, get_next


def get_catalogue():
    catalog = {
        'by_category': [
            {
                'category': 'Biography',
                'movies': [
                    {
                        'id': 1001,
                        'title': 'Abraham Lincoln',
                        'brief': 'The gripping story of Lincoln who started his career as a Store clerk, taught Law to himself and went on to become the President of United States.',
                        'thumbNailURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Abraham_Lincoln_by_Byers%2C_1858_-_crop.jpg/340px-Abraham_Lincoln_by_Byers%2C_1858_-_crop.jpg'
                    },
                    {
                        'id': 1002,
                        'title': 'Steve Jobs',
                        'brief': 'From being a mischief monger at school to a high-school dropout and then on to an entreprenuer and finally an all time legend, Steve Jobs\'s story is a must read. ',
                        'thumbNailURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg/440px-Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg'
                    },
                    {
                        'id': 1003,
                        'title': 'Narendra Modi',
                        'brief': 'Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament from Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the ...',
                        'thumbNailURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Official_portrait_of_the_Prime_Minister_Narendra_Modi%2C_November_2020_%28cropped%29.jpg/440px-Official_portrait_of_the_Prime_Minister_Narendra_Modi%2C_November_2020_%28cropped%29.jpg'
                    },
                    {
                        'id': 1004,
                        'title': 'Dwayne Johnson',
                        'brief': 'Dwayne Douglas Johnson (born May 2, 1972), also known by his ring name The Rock,[3] is an American actor, businessman, and former professional wrestler.',
                        'thumbNailURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Dwayne_Johnson_2014_%28cropped%29.jpg/440px-Dwayne_Johnson_2014_%28cropped%29.jpg'
                    },
                    {
                        'id': 1005,
                        'title': 'Tom Cruise',
                        'brief': 'Thomas Cruise Mapother IV (born July 3, 1962) is an American actor and producer. One of the world\'s highest-paid actors,[1] he has received various accolades throughout his career, including three Golden Globe Awards, ',
                        'thumbNailURL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Tom_Cruise_by_Gage_Skidmore_2.jpg/440px-Tom_Cruise_by_Gage_Skidmore_2.jpg'
                    }
                ]
            }
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
