from flask import Flask, render_template, request, redirect, url_for
import data_processer

app = Flask(__name__)


def highest_blog_id():
    """
    calculates the highest id for al blogposts,
    returns the most highest id number increased by 1 for the new blog post to save
    """
    id = 0
    for post in data_processer.read_json():
        if post['id'] > id:
            id = post['id']
    return id + 1

@app.route('/')
def index():
    return render_template('index.html', posts=data_processer.read_json())


@app.route('/update/<post_id>', methods=['GET','POST'])
def update(post_id):
    post_to_update = data_processer.fetch_post_by_id(post_id)
    if post_to_update is None:
        return "Post not found", 404
    if request.method == 'POST':
        post_to_update['author'] = request.form['author']
        post_to_update['title'] = request.form['title']
        
        post_to_update['content'] = request.form['content']
        data_processer.delete_post_by_id(post_id)
        data_processer.save_json(post_to_update)
        return redirect(url_for('index'))
    else:
        return render_template('update.html',post=post_to_update)


@app.route('/delete/<post_id>', methods= ['POST'])
def delete_post(post_id):
    list_of_posts = data_processer.read_json()

    for post in list_of_posts:
        if (post['id']) == int(post_id):
            list_of_posts.remove(post)
    data_processer.save_json(list_of_posts)
    return redirect(url_for('index'))


@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        id = highest_blog_id()
        new_blog = {'id': id, 'author': author, 'title': title, 'content': content}
        data_processer.save_json(new_blog)
        return redirect(url_for('index'))
    return render_template('add.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)