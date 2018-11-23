# H2G Hexo to Ghost Migrator

Tries to convert all markdown files in Hexo to a Ghost-like JSON file.

**IT WON'T WORK NOW,HELP WANTED!SEE KNOWN ISSUES BELOW.**

# Usage

You should export your Ghost data from 'Lab'(One JSON file), beautify it and check your current user id, for example, in `posts` section, an post entry may contain data like below:

```json
{
		"id": "5bf664e243629700019d2722",
		"uuid": "2ed2bc5c-91f4-4c00-9dc0-54f5d7d139d0",
		"title": "Creating a custom theme",
		"slug": "themes",
		"comment_id": "5bf664e243629700019d2722",
		...
		"author_id": "5951f5fca366002ebd5dbef7",
		"created_at": "2018-11-22 08:12:18",
		"created_by": "1",
		"updated_at": "2018-11-22 08:12:18",
		"updated_by": "1",
		"published_at": "2018-11-22 08:12:18",
		"published_by": "1",
		...
}
```

The post above is auto-generated post by default user called "Ghost" which has the `author_id` with value "5951f5fca366002ebd5dbef7", custom created `user_id` are counted from 1(i.e the first user created on installation.)

Before started, you should install `markdown2` and `frontmatter` by `pip3`.

```bash
python3 h2g.py /path/to/hexo/source/_posts/ <user_id>
```

The step above will create a file called `h2g_data.json` with posts data compatible with Ghost Exported file, you will need to copy those content to the corresponding part in the exported JSON file.

On Ghost Website:

> Ghost automatically generates the html and plaintext formats when MobileDoc content is provided.
> If you don't send the mobiledoc field, we generate a blank structure.

`h2g.py` can generate html from the markdown files in Hexo, but importing them into Ghost will result in posts without any content.

# Known Issues

* Importing the generated file will result in all imported blog posts without any content

# TODO

* Write posts data directly into the exported json.
