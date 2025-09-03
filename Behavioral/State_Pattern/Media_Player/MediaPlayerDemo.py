from MediaPlayer import MediaPlayer

class MediaPlayerDemo:

    def run():
        player = MediaPlayer()
        
        player.play()

        player.pause()

        player.play()

        player.stop()

        player.pause()

if __name__ == "__main__":
    MediaPlayerDemo.run()