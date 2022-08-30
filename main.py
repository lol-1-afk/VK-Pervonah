from sys import exit
import requests
import time
import json

try:
    with open("settings.json", "r") as settings_file:
        settings = json.loads(settings_file.read())

    auth_token = str(settings["token"])
    group_id = int(settings["group_id"])
    comment_text = str(settings["text"])
    offset = int(settings["offset"])
    delay = int(settings["delay"])

    if group_id > 0:
        group_id = -abs(group_id)
    # TODO: rewrite this part

except Exception as error:
    input(f"Error while trying to read config: {str(error)}")
    exit()


def get_last_post_id():
    params = {
        "access_token": auth_token,
        "filter": "owner",
        "count": "1",
        "owner_id": group_id,
        "offset": offset,
        "v": "5.131"
    }

    api_request = requests.get("https://api.vk.com/method/wall.get", params=params).json()
    return api_request["response"]["items"][0]["id"]
    # TODO: handle invalid token error
    # TODO: handle zero posts error
    # TODO: handle private group error


def create_comment(postId: int):
    params = {
        "access_token": auth_token,
        "owner_id": group_id,
        "post_id": postId,
        "message": comment_text,
        "v": "5.131"
    }
    api_request = requests.get("https://api.vk.com/method/wall.createComment", params=params).json()
    return True if "response" in api_request and "comment_id" in api_request["response"] else False
    # TODO: adding images, videos, files and other media to comment
    # TODO: handling captcha, solvind int


firtstId = get_last_post_id()
print("Firt post id:", firtstId)

while True:
    lastId = get_last_post_id()
    if lastId != firtstId:
        firtstId = lastId
        print("New post with ID", lastId)
        is_created = create_comment(postId=lastId)
        print("is comment created:", is_created)

        if is_created:
            break

    time.sleep(delay)

input(f"Done! https://vk.com/wall{group_id}_{firtstId}")
