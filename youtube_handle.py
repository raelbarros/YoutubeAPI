from google.cloud import storage
import requests
import pytube
import shutil


class YoutubeHandle:
    storage = storage.Client.from_service_account_json('key.json')

    def __init__(self, api_key):
        self.api_key = api_key

    def listVideosIdByChannel(self, channelId):
        url = 'https://www.googleapis.com/youtube/v3/search?part=snippet,id&order=date&maxResults=5&channelId=' \
              + channelId + '&key=' + self.api_key

        try:
            listVideoId = []
            resp = requests.get(url).json()
            #pageToken = resp['nextPageToken']
            for video in resp['items']:
                video = video['id']
                listVideoId.append(video['videoId'])

            print(listVideoId)
        except:
            print(resp['error']['message'])

    def videoInfos(self, videoId):
        url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id=' \
              + videoId + '&key=' + self.api_key

        try:
            resp = requests.get(url).json()
            for video in resp['items']:
                return [{
                    'videoID': video['id'],
                    'channelId': video['snippet']['channelId'],
                    'channelTitle': video['snippet']['channelTitle'],
                    'publishedAt': video['snippet']['publishedAt'],
                    "title": video['snippet']['title'],
                    "tags": video['snippet']['tags'],
                    "statistics": video['statistics']
                }]

        except:
            print(resp['error']['message'])

    def channelInfo(self, channelId):
        url = 'https://www.googleapis.com/youtube/v3/channels/?part=snippet,contentDetails,statistics&id=' \
              + channelId + '&key=' + self.api_key

        try:
            resp = requests.get(url).json()
            for channel in resp['items']:
                return [{
                    "channelId": channel['id'],
                    "title": channel['snippet']['title'],
                    "description": channel['snippet']['description'],
                    "localized": channel['snippet']['localized']['country'],
                    "statistics": channel['statistics']
                }]

        except:
            print(resp['error']['message'])

    def createVideoURL(self, videoId):
        return 'https://www.youtube.com/watch?v=' + videoId\

    def downloadYoutubeVideo(self, videoId):
        url = self.createVideoURL(videoId)

        bucket = self.storage.bucket('paparazzo-landing')
        blob = bucket.blob(videoId)

        youtube = pytube.YouTube(url).streams.first().download('.download/')
        blob.upload_from_filename(youtube)
        print(self.hasDownload(videoId))
        self.deleteLocalVideo()

    def hasDownload(self, videoId):
        return self.storage.get_bucket('paparazzo-landing').blob(videoId).exists()

    def deleteLocalVideo(self):
        try:
            print('deletando video..')
            shutil.rmtree('.download/')
        except OSError as e:
            print(e.strerror)
