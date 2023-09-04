import pafy_fixed.pafy_fixed as pafy

def pafy_search(youtube_link_or_id):
        
        media = pafy.new(youtube_link_or_id)
        if media.dislikes == 0:
            print("Ignoring dislike count in new media")

        return media

