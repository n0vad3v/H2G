import frontmatter
import markdown2
import json
import os
import sys

path = sys.argv[1]
author_id = sys.argv[2]

files_with_path = [os.path.join(path, f) for f in os.listdir(path)]

dict_list = []

for files in files_with_path:
    # Get the slug from md filename.
    file_name_with_path = os.path.splitext(files)[0]
    file_name_without_path = file_name_with_path.split("/")[-1]

    with open(files) as f:
        post = frontmatter.load(f)
        d = dict()
        d['id'] = None
        d['uuid'] = None
        d['title'] = post['title']
        d['slug'] = file_name_without_path

        # TODO: How to generate mobiledoc
        d['mobiledoc'] = None
        d['html'] = markdown2.markdown(post.content)

        # TODO: How to generate comment id?
        d['comment_id'] = None
        d['plaintext'] = post.content
        d['markdown'] = post.content

        d['feature_image'] = None
        d['featured'] = 0
        d['page'] = 0
        d['status'] = "published"
        d['locale'] = None
        d['visibility'] = "public"

        d['meta_title'] = None
        d['meta_description'] = None

        d['author_id'] = author_id
        d['created_at'] = str(post['date'])
        d['created_by'] = author_id
        d['updated_at'] = str(post['date'])
        d['updated_by'] = author_id
        d['published_at'] = str(post['date'])
        d['published_by'] = author_id

        d['custom_excerpt'] = None
        d['codeinjection_head'] = None
        d['codeinjection_foot'] = None
        d['og_image'] = None
        d['og_title'] = None
        d['og_description'] = None
        d['twitter_image'] = None
        d['twitter_title'] = None
        d['twitter_description'] = None
        d['custom_template'] = None

        dict_list.append(d)


json_list = json.dumps(dict_list,indent = 4,ensure_ascii=False)

with open('./h2g_data.json','w') as f:
    f.write(json_list)
