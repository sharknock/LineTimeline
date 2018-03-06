#coding: utf-8
import requests
import json
import lxml.html

class LineTimeline:

    host = "https://timeline.line.me/api/"

    headers = {
        "Host": "timeline.line.me",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "X-Timeline-WebVersion": "1.10.2",
        "X-Line-AcceptLanguage": "ja",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Origin": "https://timeline.line.me",
        "Content-Type": "application/json;charset=UTF-8",
        "Referer": "https://timeline.line.me/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
        "Cookie": ""
    }

    homeId = ""
    name   = ""


    def __init__(self, token):
        self.headers["Cookie"] = "lwtl={}".format(token)
        try:
            r = requests.get(url="https://timeline.line.me/", headers=self.headers)
            r = lxml.html.fromstring(r.text)
            home = r.xpath("//a")
            name = r.xpath("//span")

            for x in home:
                try:
                    if '83' == x.attrib["data-reactid"]:
                        self.homeId = x.attrib["href"].replace("/user/","")
                except:
                    pass

            for x in name:
                try:
                    if '79' == x.attrib["data-reactid"]:
                        self.name = x.text
                except:
                    pass

            if not self.name or not self.homeId:
                print("Loggin Failed")
            else:
                print("Loggin Success")
                print("Name : {}\nhomeId : {}".format(self.name, self.homeId))

        except Exception as e:
            print(e)


    def createPost(self, viewType=0, text=None):
        if viewType == 0:
            viewType = "NONE"
        elif viewType == 1:
            viewType = "FRIEND"
        elif viewType == 2:
            viewType = "ALL"
        if text == None:
            text == ""
        json = {"postInfo": {"readPermission": {"type": viewType,}},"contents": {"text": text,"stickers": [],"media": [],"contentsStyle": {"textStyle": {},"stickerStyle": {}}}}
        r = requests.post(url=self.host + "post/create.json", headers=self.headers, json=json)
        return r.json()

    def deletePost(self, postId):
        json = {"postId": postId}
        r = requests.post(url=self.host + "post/delete.json", headers=self.headers, json=json)
        return r.json()

    def likePost(self, postId, likeType=1001):
        json = {"contentId": postId, "likeType": "1001"}
        r = requests.post(url=self.host + "like/create.json", headers=self.headers, json=json)
        return r.json()

    def unlikePost(self, postId):
        json = {"contentId": postId}
        r = requests.post(url=self.host + "like/cancel.json", headers=self.headers, json=json)
        return r.json()

    def createComment(self, postId, text=None):
        if text == None:
            text = ""
        json = {"contentId": postId, "commentText": text}
        r = requests.post(url = self.host + "comment/create.json", headers=self.headers, json=json)
        return r.json()

    def deleteComment(self, postId, commentId):
        json = {"postId": postId, "commentId": commentId}
        r = requests.post(url = self.host + "comment/delete.json", headers=self.headers, json=json)
        return r.json()
