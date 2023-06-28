from dataclasses import dataclass, field

@dataclass
class Post:
    id: str
    author: str
    media: dict
    num_comments: int
    permalink: str
    preview: dict
    score: int
    selftext: str
    selftext_html: str
    subreddit: str
    thumbnail: str
    title: str
    url: str

@dataclass
class Comment:
    id: str
    author: str
    body: str
    body_html: str
    permalink: str
    score: int
    