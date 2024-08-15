# https://jekyllrb.com/
config = {
    "name": "Jekyll",
    "posts": {
        "path": ["_posts"],
        "depth": [-1],
        "type": [".md"],
        "save_path": "_posts/${filename}.md",
        "scaffold": "",
        "excludes": [".placeholder"]
    },
    "drafts": {
        "path": ["_drafts"],
        "depth": [-1],
        "type": [".md"],
        "save_path": "_drafts/${filename}.md",
        "scaffold": "",
        "excludes": [".placeholder"]
    },
    "pages": {
        "path": ["_tabs"],
        "depth": [-1],
        "type": [".md"],
        "save_path": "_tabs/${filename}.md",
        "scaffold": "",
        "excludes": [".placeholder"]
    },
    "configs": {
        "path": [".github", "", "_data", "_includes", "_layouts"],
        "depth": [3, 1, -1, -1, -1],
        "type": [".yml", ".yaml", ".toml", ".js", ".ts", ".json", ".styl", ".html"]
    }
}
