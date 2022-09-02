import requests
from bs4 import BeautifulSoup as BS
import json


# BASE_URL = 'https://coursive.id/api/v1/courses'


def get_response(url):
    response = requests.get(url)
    response_json = response.text
    return response_json


my_url = 'https://coursive.id/api/v1/courses'

def parse(link):
    data_list = []
    # print(123)
    courses_list_response = get_response(my_url)
    data = json.loads(courses_list_response)
    for i in data['results']:
        id_ = i['id']
        title = i['title']
        # image = i['image']
        slug = i['slug']
        details_response = get_response(f"{my_url}/{slug}")
        # youtube_url = details_response['youtube']
        # blocks = details_response['blocks']
        data_list.append(
            {
                'course_id': id_,
                'title': title,
                # 'image': image,
                'slug': slug,
                # 'youtube_url': youtube_url,
                # 'blocks': blocks,
            }
        )
        # return data_list
    print(data_list)
    return data_list


# get_response(my_url)
parse_objects = parse(my_url)


# get_response(my_url)
parse(my_url)


# import requests
#
#
# class Parsing:
#     BASE_URL = 'https://coursive.id/api/v1/courses'
#
#     def get_response(self, link):
#         response = requests.get(link)
#         response_json = response.json()
#         return response_json
#
#     def parse(self):
#         data_list = []
#         print(123)
#         courses_list_response = self.get_response(self.BASE_URL)
#         for i in courses_list_response['results']:
#             id_ = i['id']
#             title = i['title']
#             image = i['image']
#             slug = i['slug']
#
#             details_response = self.get_response(f"{self.BASE_URL}/{slug}")
#
#             youtube_url = details_response['youtube']
#             blocks = details_response['blocks']
#
#             data_list.append(
#                 {
#                     'course_id': id_,
#                     'title': title,
#                     'image': image,
#                     'slug': slug,
#                     'youtube_url': youtube_url,
#                     'blocks': blocks,
#                 }
#             )
#         return data_list

