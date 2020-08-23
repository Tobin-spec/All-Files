import instaloader
from instaloader import Profile,Post

instance = instaloader.Instaloader()

instance.login(user="__one_wolf__",passwd="mylovemymerin")

instance.download_profile(profile_name="_luttuz_")
