import instaloader

mod = instaloader.Instaloader()

a = input("ENTER the user name ")

mod.download_profile(a,profile_pic_only=True)
