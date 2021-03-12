class Video:
    def __init__(self, videoId, channelId, channelTitle, publishedAt, title, tags, statistics):
        self.videoId = videoId
        self.channelId = channelId
        self.channelTitle = channelTitle
        self.publishedAt = publishedAt
        self.title = title
        self.tags = tags
        self.statistics = statistics