import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Smallg - Indie Game Dev", page_icon=":tada:", layout="wide")

def LoadLottieURL(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Gaming section
gaming_lottie = LoadLottieURL("https://assets6.lottiefiles.com/packages/lf20_znokougu.json")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Hello World - Smallg")
        st.subheader("Indie Dev Game Projects")
        st.write("I am a solo indie game developer mainly using Unity (and a little GG Max)")
        st.write("I mostly just release small demos and WIPs as well as scripts for other to use in their own games")
        st.write("I enjoy VR and have made some cool demos for the quest and steam VR")
    with right_column:
        st_lottie(gaming_lottie, width=600, height=400, key="gaming")

# VR section
vr_lottie = LoadLottieURL("https://assets3.lottiefiles.com/packages/lf20_p8xzlbof.json")
with st.container():
    left, mid, right = st.columns(3)
    with mid:
        st.markdown("<h1 style='text-align: center; color: white;'>VR Demos</h1>", unsafe_allow_html=True)
        st_lottie(vr_lottie, key="VR", height=430)
        st.write("Despite easily getting motion sick I do love VR and especially wireless VR with the Quest")

    with st.expander("VR Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Fruit Ninja style clone")
            st.video("https://www.youtube.com/watch?v=GsjLUNkzZt0")
            st.write("A game I made based on fruit ninja which started life as an experiment into how to dynamically"
                     "chop object meshes at runtime")

        with middle_column:
            st.subheader("VR Shooting Range Demo")
            st.video("https://www.youtube.com/watch?v=bUbnJcIZQnU")
            st.write("This is a tech demo I made to explore gun interactions in VR such as using physical joints to"
                     "simulate cocking your gun and slotting in the ammo clips")

        with right_column:
            st.subheader("VR Boxing")
            st.video("https://www.youtube.com/watch?v=jCrz704fjdw")
            st.write("I wanted to explore a game that felt more impactful than animation based boxing games")

    with st.expander("More VR Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Magical powers gesture system")
            st.video("https://www.youtube.com/watch?v=jL9wNCUL1QE")
            st.write("I did a lot of similar experiments using the gesture system in VR, this one uses more basic"
                     "movements to register a spell cast")

        with middle_column:
            st.subheader("Physical VR IK")
            st.video("https://www.youtube.com/watch?v=9mpn6Av8-SQ")
            st.write("VR physics was always a difficult task to get right as too much physics can often make the "
                     "movement feel restricted or sluggish")

        with right_column:
            st.subheader("Hangman in VR")
            st.video("https://www.youtube.com/watch?v=afOzThtDKsU")
            st.write("more VR gesture based gameplay, this one involved themed locations and words and even had the "
                     "beginnings of multiplayer (1 vs 1 at least)")

    with st.expander("Even More VR Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("VR Gesture based inventory system")
            st.video("https://www.youtube.com/watch?v=jZ7kV5H1QPg")
            st.write("Experimenting with a way to summon or magic items into your possession rather than a "
                     "traditional click based inventory for VR")

        with middle_column:
            st.subheader("Energy Sword style firefight")
            st.video("https://www.youtube.com/watch?v=x5IutjcK4TM")
            st.write("Everybody loves Starwars and it feels great in VR to fight with scifi swords :smile:")

# unity demos
unity_gaming_lottie = LoadLottieURL("https://assets3.lottiefiles.com/packages/lf20_5josuovc.json")
with st.container():
    left, mid, right = st.columns(3)
    with mid:
        st.markdown("<h1 style='text-align: center; color: white;'>Unity Game Demos</h1>", unsafe_allow_html=True)
        st_lottie(unity_gaming_lottie, key="Unity", height=430)
        st.write("Unity is my go-to engine for more serious or complex game creation, it has a great mix of ease-of-use"
                 "and control over every aspect of your game")

    with st.expander("Unity Game Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Boxing with Rigidbody physics")
            st.video("https://www.youtube.com/watch?v=WZUXDR3rtX8")
            st.write("More fun with physical combat, I just love ragdolls")

        with middle_column:
            st.subheader("AI Soccer Game")
            st.video("https://www.youtube.com/watch?v=QdvqKMpEiXg")
            st.write("I spent way too long watching the AI battle it out in this dumb but fun soccer game")

        with right_column:
            st.subheader("Demon Monster - Low Poly Horror")
            st.video("https://www.youtube.com/watch?v=_HO3HQa2Ea4")
            st.write("Synty Studios have the coolest style and always at a great price for a world of assets and I have"
                     "always had a soft spot for horror games")

    with st.expander("see more Unity games (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("SCIFI air suction")
            st.video("https://www.youtube.com/watch?v=pBwwjrglvtI")
            st.write("Making combat feel more dynamic with some destructible assets and breaking the windows to "
                     "literally help (or hinder) your chances was a fun idea for a space themed game")
        with middle_column:
            st.subheader("SCIFI Shooter AI Test")
            st.video("https://www.youtube.com/watch?v=5vCgnuGfwhI")
            st.write("Complex AI with smart logic is always a challenge, in this I was mostly trying to get the AI to"
                     "use cover in a reasonably believable and smart way")
        with right_column:
            st.subheader("SCIFI Shooter - RayFire destruction fun")
            st.video("https://www.youtube.com/watch?v=gI90FJ_uKDo")
            st.write("RayFire is a great asset for allowing you to completely destroy your game world in the most fun"
                     "way possible")

    with st.expander("see even more Unity games (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Mud tracks for Squad based AI")
            st.video("https://www.youtube.com/watch?v=qxtiQiA6Dh8")
            st.write("We all love snow shaders and such, this one was very much inspired by "
                     "the return of the Tomb Raider games which made some great use of mud and water")
        with middle_column:
            st.subheader("Soccer Game - Transfer Market player cards")
            st.video("https://www.youtube.com/watch?v=PYjYvmFS6X4")
            st.write("player stat sheets are a staple in most games - this one was to go with my AI Soccer game")
        with right_column:
            st.subheader("Asynchronous scene swapping for seamless gameplay")
            st.video("https://www.youtube.com/watch?v=5mxyi9CvJoM")
            st.write("A demo showing the potential for seamless gameplay even with some complex destruction physics,"
                     "this was using real-time RayFire destruction so couldn't handle many objects at once")

# GG Max
max_gaming_lottie = LoadLottieURL("https://assets3.lottiefiles.com/packages/lf20_i9arxzcg.json")
with st.container():
    left, mid, right = st.columns(3)
    with mid:
        st.markdown("<h1 style='text-align: center; color: white;'>GameGuru Max Script Demos</h1>", unsafe_allow_html=True)
        st_lottie(max_gaming_lottie, key="GGMax", height=430)
        st.write("GameGuru Max (formerly Classic) was a great starting point as I learned game dev and coding,"
                 "home to a great community and a great development team")
        st.write("Below are some examples of videos I made to showcase my freely shared scripts for the GG community")

    with st.expander("GG Max Script Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Quest system")
            st.video("https://www.youtube.com/watch?v=c8Z5h51_KrU")
            st.write("A completely custom and self-contained quest system which can be used to make your Max games "
                     "much more engaging")
        with middle_column:
            st.subheader("Loot drop system")
            st.video("https://www.youtube.com/watch?v=mw6kazlZpZE")
            st.write("Real-time spawning is not really a thing in GG so loot systems have always been a bit more "
                     "difficult / tricky to set-up so this is a more logical pool-based loot system with variable "
                     "loot and rates")
        with right_column:
            st.subheader("Skyrim inspired Text Radar")
            st.video("https://www.youtube.com/watch?v=Y6JFzr_8FFI")
            st.write("A clean and simple Radar like the one found in Skyrim - images and landmarks are fully "
                     "customisable by the end user")

    with st.expander("More GG Max Script Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Object inspect")
            st.video("https://www.youtube.com/watch?v=TrjRyfmW25U")
            st.write("A simple but important object inspect/interact script which lets the player pick up and look at "
                     "an object - similar to the classic resident evil games")
        with middle_column:
            st.subheader("Simple move and rotate")
            st.video("https://www.youtube.com/watch?v=WM0AFrDi31g")
            st.write("This is more for a repeated movement which allows many objects to have their own values but all "
                     "from one simple script")
        with right_column:
            st.subheader("Resident Evil inspired zombie AI")
            st.video("https://www.youtube.com/watch?v=DlrLfwI2g9s")
            st.write("We all love a good shambling zombie")

    with st.expander("Yet more GG Max Script Demos (Click me)", expanded=False):
        left_column, middle_column, right_column = st.columns(3)
        with left_column:
            st.subheader("Alien Isolation style motion tracker")
            st.video("https://www.youtube.com/watch?v=bczxTj8KDeU")
            st.write("Alien Isolation was one of my favourite games of all time, the atmosphere, the tension,"
                     "the perfect recreation of the original alien setting.. it's amazing how long I spent hiding"
                     "inside lockers the first time I played through it :laughing:")
        with middle_column:
            st.subheader("Squash the bugs mini game")
            st.video("https://www.youtube.com/watch?v=9lC7SyCJxug")
            st.write("I made a bunch of these mini games type scripts which were mainly used as ways to unlock doors"
                     "in a more engaging way that simply finding a key")
        with right_column:
            st.subheader("Radial Inventory")
            st.video("https://www.youtube.com/watch?v=Ti0YCOCK14I")
            st.write("Yet another one inspired by Alien Isolation, a good inventory system can be hard to find")

with st.container():
    st.write("###")
    st.write("Check out all my project videos on youtube -> (https://www.youtube.com/channel/UCiQ9gT4d8wiPtqy7P05mGwA/videos)")

