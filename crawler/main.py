import requests
from crawler.model import Post
#main function
if __name__ == '__main__':
    req = requests
    post_test = Post.Post(1, "Chuyen muc test", "https://amis.misa.vn", 1234, "https://example.com", "h", 1,2,4,5,4,3,4)
    print(post_test.canonical)