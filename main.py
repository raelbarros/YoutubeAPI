from youtube_handle import YoutubeHandle

class Main(object):

    def main(self):
        key = 'AIzaSyCxGk0onlLpbkD_mA2IWtZFrn1BZasVHSc'
        teste = YoutubeHandle(key)
        #teste.listVideosIdByChannel('UCG-fFAxQjZgJmn0w7Brj5xQ')
        #teste.videoInfos('OTOYD8kNWGk')
        #teste.channelInfo('UCG-fFAxQjZgJmn0w7Brj5xQ')
        teste.downloadYoutubeVideo('WZIGwN-5Ioo')


if __name__ == '__main__':
    Main().main()