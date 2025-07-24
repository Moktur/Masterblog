import json


def read_json():
    """reads the json file, returns the datastructure"""
    with open("blogdata.json", "r", encoding="utf-8") as fileobj:
        return json.load(fileobj)


def save_json(data):
    """saves the json file"""
    if isinstance(data, dict):
        list_of_posts = read_json()
        list_of_posts.append(data)
        data = list_of_posts
    with open("blogdata.json", "w", encoding="utf-8") as fileobj:
        json.dump(data, fileobj, indent=2)


def fetch_post_by_id(post_id):
    """returns the post with given id"""
    posts = read_json()
    for post in posts:
        if post['id'] == int(post_id):
            return post
    return None


def delete_post_by_id(post_id):
    """delete post with given id"""
    list_of_posts = read_json()
    for post in list_of_posts:
        if post['id'] == int(post_id):
            print(f"{post} Datensatz wird gelöscht!")
            list_of_posts.remove(post)
            print("Löschung erfolgt")
    save_json(list_of_posts)

