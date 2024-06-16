from dataclasses import dataclass


@dataclass
class Post:
    id: str
    author: str
    created_utc: int
    media: dict
    name: str
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
    created_utc: int
    name: str
    permalink: str
    score: int
