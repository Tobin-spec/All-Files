import instaloader
from instaloader import Profile,Post

instance = instaloader.Instaloader()


instance.login(user="__one_wolf__",passwd="mylovemymerin")

profile = Profile.from_username(instance.context,username="neringakriziute")

instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))
