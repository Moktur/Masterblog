import json



def read_json():
    with open("blogdata.json", "r", encoding="utf-8") as fileobj:
        return json.load(fileobj)


def save_json(data):
    if isinstance(data, dict):
        list_of_posts = read_json()
        list_of_posts.append(data)
        data = list_of_posts
    with open("blogdata.json", "w", encoding="utf-8") as fileobj:
        json.dump(data, fileobj, indent=2)


def fetch_post_by_id(post_id):
    list_of_posts = read_json()
    for post in list_of_posts:
        if post['id'] == int(post_id):
            print(f"DEBUG TEST IF DICT: {post}")
            return post
