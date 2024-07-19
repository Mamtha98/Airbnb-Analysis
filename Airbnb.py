#Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import plotly.figure_factory as ff
from streamlit_option_menu import option_menu


pd.set_option('display.max_rows',6000)
pd.set_option('display.max_columns',6000)

df = pd.read_csv('C:/Users/RISHI/OneDrive/Desktop/AirBNB project/airbnb_listings.csv')

def render_logo_and_heading(logo_url, heading_text):
    st.markdown(f"""
    <div style="display: flex; align-items: center;">
        <img src="{logo_url}" alt="Logo" style="width: 80px; height: auto; margin-right: 5px;">
        <h2>{heading_text}</h2>
    </div>
    """, unsafe_allow_html=True)
    return None 


# SETTING PAGE CONFIGURATIONS
st.set_page_config(page_title= "Airbnb Dashboard - Mamtha S")

#set the colour of sidebar
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FF5A5F;
    }
    .sidebar-title {
    font-weight: bold; /* Makes the text bold */
    color: #333; /* Sets the text color to a dark shade (e.g., black) */
}

</style>
""", unsafe_allow_html=True)

#set the option menu's option list and customise styles
st.sidebar.title(" Airbnb Dashboard ")
with st.sidebar:
    option = option_menu(None,
                #menu_title='Main Menu',
                options=["Home", 'Dashboard'],
                icons=['house', "graph-up-arrow"],
                menu_icon="cast",
                default_index=0,
                styles={
                    "container": {"background-color":'white',"height":"140px","border": "3px solid #000000","border-radius": "0px"},
        "icon": {"color": "black", "font-size": "16px"}, 
        "nav-link": {"color":"black","font-size": "15px", "text-align": "centre", "margin":"4px", "--hover-color": "white","border": "1px solid #000000", "border-radius": "10px"},
        "nav-link-selected": {"background-color": "#FF5A5F"},}

                
                )
    
if option == "Home":
    #st.markdown("## :black[Phonepe Data Visualization and Exploration]")
    render_logo_and_heading("data:image/png;base64,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", "Airbnb Data Visualization")
    st.divider()
    col1,col2 = st.columns([3,2],gap="medium")
    with col1:
        st.image('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUSExMVFhUXGRsYGBcWGBgYGRsgGxkaFxgYFxoYHSggGB4mHRkaITEiJSkrLi4uHh8zODMtNygtLisBCgoKDg0OGxAQGy0mICYvLy0vLS0tLS0tLy0tLS0tLS01LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAMkA+wMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAAEAAIDBQYBB//EAEgQAAECBAMFBgIGBwUHBQAAAAECEQADITEEEkEFIlFhcQYTgZGhsTLBQlJy0eHwBxQjM2KS8TSCorLSQ1Nzg5Oj0xUWJMLi/8QAGgEAAwEBAQEAAAAAAAAAAAAAAAIDAQQFBv/EACcRAAICAgMAAQMEAwAAAAAAAAABAhEDIRIxQQQiUWETMnHwQoGR/9oADAMBAAIRAxEAPwD0WFEGCxaZqQpOuhoaXgiKkRrQmjsKAKGtCaHQoDBkKHQoAGtCaHNHGgA40caHNCaNMONCaOtCaADjRyHQoAGwodCaABsKHNCaADjQmjrR2ABrR2OtCgA5CjsNmKABJsIAoC2vjhJQSTUuB1aMHMxiVzlBxmIctVXU+vpE219ozJ5WFKOQk5ALBIcv1oPOIdm7PzLeqM7pzMagOSz0sPOOHLk5OjpxRaLXY2FEzMtSXRQBLgPXeL8gPWLjY8ubkJVQ52GYFgl6eYBL2qIFTJTIUlAV+yfKQqpNFKUoAc8oLcI0QDJKSpyK2bnpSsJGJ03QLhCRmCyks5HN+XWM3iJJKjvC/ONNilBKcxLsKA2fR2ipwO00lAOU6+59ISavQ6rsrf11UmYEi0s0e7u6j41HSNtKmBSQpJcEODHmsyaVEEk8H1pZ4uOzGIWJoQDuqdw5agJcc6R68o6s8PFl+qvGbWE0V2ImkTMrgApzA6uDlU+jVTDUbVIAKxTNkLXB43tQxFHW1RZNCaGy5qVWLxI0aYMaE0OhQWA2FDmhNAYNhR1oTQWA2FDmhNGgNhQ5oTQGDY7HWhNAByFHWhNAByFHWhNAByFHWhNAByMj2u2qSRJlqoQQvWrhhToY0m0ccmSl1XL5RxLPGNweGVOmEqZrqAsCSXAcWYRz5snFUiuPHyZBsDDBSCxdRUyXfe6luDRaTwuXNlpfdCcoNaBlORxUzDS8FnemIQhmSFfAKJI3RWtn/pFngdngNMWcyquqtfDTgwjkScno7aSVEezpaEoSVKKiz5lMSxJy1NrwZNV4WYvfpEZlhYZjpZwfvs/KFi9xIUogBN/Y+UVSpUYqB9qFpSylJO7ugakkCBsPslQSAQ9NP6QTJxBOVTFlB0uNGo40LnrFFjNtTgsjvMv8LCnpEpcb2O20immSVIUyhlJqNKOzgRZbEXlmZj9AKUegSYj2+sT8pF0lguoBDUBBbx6DjHOz2IHe5JlAUlJJoC6SLx693E8BR45K8L+TiTlEyZYKKCeILB+mYAvDZsgSpSpZZRyBSNS4zJpwannDJJJld0qtChqNSgbqCKwZtZJTJSsEZ5TE6vYKB15vEfTt3VlBhdqErQN4EFLly5DsoDTjSNIZ8xKltmUUqdiXzIO9u8wygOkZFYKlqXLSWfMGqxv7xqtojeQMzEu5s7hQan2ieUPPVUSw207LLBY+XNSFIVQ8aHyMNRtCWZnd5t7Tn0OsZBIWJk1SD8GZYGlFUSOhV+XgjG7LCJaZtc0v4g4tduRZteJgpWbzlXRsWhNGV7Ndpwod3OJzCgW1+GZrHnGqBeotGSi12bjyRmrQmhNDo5GDnITR2FABxoTQ6FAA2FDo5AByE0dhQAcaE0dhQBRxojnTQhJUosAHJiRSgLxjNv8AahMxK5MsG7ZjYgX6Qk5KKs1Ij2vtITVFYLJRZ3aoID839oq9i41cwoEoEhE0uWf4gqmYjgHPBxA2HlBe6pwlRClEuwY/kt1i5RttIUMPKRlZykJupgSoNrbnaOFyttvs64qki92YiWUOhLbxDltHfpWLZSqJIYi55cKm2sV2CkFUuWpSVIYvlJYl3fMPF2MGy1pKikKdiCptKW+bQ8bRR0SSZZU6i4u3qxbSI8SRMCUqDkVUNH/qHh8+ZkQSXVQsNSbgddIEE3IQ4dZdkpLuQHNfSsM3RiR3aeIEsBzSzN+dYyGKxAznebX4TrWNBjsKuZMQ43crrA0PAc2F348YZJ2VJYZ5QKtS79KmppHNO5SGp0ZfZSwtSpMxQSr6JLB7i+lWNb1aKpMp1MCXSWqHfTeHo8WO15Cc5XLJCczgtY6lusVs2YpwVM4NFC3j4R70K7R8xmbWpeel9h5wlFJUpWWhCiDlSoiqVEVNPa0XmEIWmY5BEwuS/wDKx6Bm5Rmpis6G0LQKgzJBLhRlk34MWzJOrGJyx30dEPkce1o0ez5CkIJSa5iCFA+DH1+6C8TNV3iczfApjwOV1B9KejxFsSfm+IgFRJSm7/xM+68dXLzLMpZTu76bg1szauIi+9nbH9ioL2IpIEwq3SokgEMQKEt6eQh2MmpmGZLcMQP5gSBTlc+EAbAxAmTpm6AnKAlwN1h8PiXLco5tNSsP3jWVlrwz5hToR5GNr6jOa/TvwyvdATXO6l+dGOraRrtk7WTh6LUDKUSAznLRJzN9WvpAu0NlBEvMPjJdRApUEhKeFoC2mQUZgQRlcABgxZJDcmHrFnJTaONQlhTa77PQpE9K05kEEHURI0efdlduiQwmH9mo7xaiSRQ06MevKPQkKBAILg1BFjE5w4s6cOZZI36caOtHYUIWGtCixwOAzDMq2g484LM6Umm74B/YRlm0UbQoupmFlzA6WB4j5iKmbLKSQbiBA0Rwo7CjTDkKOwFtTHJlILqAUQco4lizRjdbYUU/a7aeQBCFb7gsLizGMbLyozuczsSAxAoSwo71gqcpUyemcsioZjqWyuQK8PGOYbZqpp3QElTkqU7s6QouzDWkcOSfOR0QhQpktSsik1CgVFJpQfB4u3nrFzsHs3lJxBT+0UN3MS6QS7gWTp4NBezsOJgQlIIloYOQTmKb3uHEWy5yUJLHdQHqzMDX0MLBf8LcUFCWyRqwvqXuYHwqilKyEgEqNWq1KkeNoHnbTT3WdxmKbeDm8Mwu2EzkgoStywIYBrufCKOSBBuIUGAWXLNQNXUiAMPtBOZYUQDmZ3A1ZIrxjmPnkI7sEFYCQ5I8RyoweKJeDmIOfK1khviUXADfVTz/AKxGeTehlo0sqcSOLvWtj83eJTJJq0D7Lwplp3i6jfgOA4U46xDiNpkKIDNC3rZpm9sLUhASCDq6RSth7Hwip2bNTMdJbNbkeD6eMN2Klc3B5wSSklN3ty/vCAkOlV6jhyuG+Ue5jXaPnfkSdqVaDJI7oqc7ps1hF2pAnyUylBlpzFB4kkEDmDUV5RXSgJjDjqfnD9l4jupgSUh0FwDqxenjppDS2JjajrxlzssmROSlQDWqPA5eAdhBm05jKbKKu5Dg8X5FxC2pNC5slaE5goFgbHSo4gm0WRANCmltOTHp90csvuepBKnFFXJVKSjco4cFg5q7F9dIimDvZaszkUVS4anW8PmJOHW/xS1aPY3BtygrE4cIWmYgshVC1Q/yprGfkKtU0QbDmhSS5cg5QH1TRzwvSKnbWGyTlAj9msUADNYluFQIftArw8zPLv8ASFxypoDeL7aGHTiJIUGJ0LdHHpFOXF39yLhzi4eoxkqX3boWMwHkzA04isaHsrt0SsuHmncJPdrNhX4FfIxWKkghIWd5CiS18q2rTQFhSK3EKyky1jMAQHHRwYump6ZwSUsLUo/38M9aBifCSc6gNLnpHlOw+083DNLUc0vgatzTy5R652cUTIE5bDOM4ozJul35V8Yhkg4Hf8f5Ecy136iTbO0kSgEFaUkh2cAtag9POMxie0UhIcEqGuUW82gTa8lOJnGY5cuKlmSHDcvx5xRJwah3qB9FnSrhUuNbCMikUnKSZocP2yEtYPdnK4zV01LNUgVjXbZKe7E590M5FQxselb8Hjy5eyFEryu4bKDY3JS/EOPWNr2C2l38heFmsVS6ZTqhVGI5F09GjZJdoSE5XUvegpJBDiojsZJOOXs/ELw04KVJKnQs6A2PAhr8wY1sEotG48qna9XaGrWEhyQBxNIxPaWcJk0rFUhOX3Lg8zF72jxYymVrQxjlpUlyVBKaXuyaKNtRHF8jJ/ijqxw9YsPITMyqNKBLVoXBqHalIstppyBPdGoLFxSlS3rFEnbaApIzAJXQAXdSh5Ev+Wi1Ukb6VmpWWAdmyuQTxf3Mcuy8WvC52dtWWUFDpQEuwuSwckCKROOKVCW/72qjckkAkgs7Mm2rRBNwYzGpBU7NzDeFTF1h8ImWylkLUlIcnQMz16m5jXMZWyCVsczQkKWqXLQVVB+IKzOK6VzF9bRIjGiWkplMEfRIuQPenvBE/aKFIUjMBSzUaxY6/hFTLkNmmGrHKEjmQK6pc6DgIRyAaqb3pUrOQ7MoBib2PhdoJwO1lOFZVqlpCgVKBoxAJc0JvbnEGEISobuYVKgQ4r9HnpE2PnZho7GlvzSEckjYpvYXtHbAZLZg4fl52ikkYlSxmGpP1TYkcOUVe1VTFEAoGTOE/R+Fms9hHZu2kSyUA5QLBj1GkNTYjl9xvY9aymchCmzALGru6CG65a847tHAlCnd1tUjXw/Nop9m7S/V5yJgH7MEpUAalKgAoDhxEbDbeHSVFcpWaWyTmJJvb0YnrHvN8ZnhpLJhr1FHhsaABmDElm6FiYOmqCmUKsf6w3HbOASlyCDVJTd3rXhoxibDqIIAHgeFiOZasa5rwWGGXTLDY2IabLzVTmAHImjvp841ikZmSlsuUkHya2lTHn6ZxSaCl+BOtH8DG02djkmUk5gGZ6OxJJILVAPlEstPZ2fGbVxYTiJDsS44+VbRUTJagChKiUn6Lve9/aNKhYUlx+bj3EC4vChdeERR1yjZlsfLb9muysoB4jMCGN6tB+wJykpWgMQlW69zmJOUtw4xDtBKFBlEhLkBQulWrsXA6deMASivDrAs2pNG+68V7VHJ+2dllt3BJ7tM1AdQIzfxA/F5xmNsSwSCgNlQlKuNg7jUdI1UzaSZkpjRQ3m47pAblURTYkkTN4BiAKMHbcCxoKgGKYm0Q+VGMuvQPsdsb9cxKEH4BvzPspZw/Msnx5R6/wBpMSpKUoSKEjPVmTanj7HjFX2F2OjB4dc9ZAMz9opRoEoSHHQfErx5QOvaf6wgTwcoU9CxYOzHmzecJmnyf4KfDwrFGn29lXMVkWo7xFKKTYlw44htOUVeHRNK5qkUYA5CHSoOaHhSNrsnYQmpK54BStiE8RcE8By1i1zYSUcrSkk0oAbUqQNOcInR0ShZ59IWC0yWlaakqBLpO6xD1b8RFrslSZc5M1KWVTNl1BDEEa1c9QI1X/o+HWCqUEpzay2yk8SBQn1jI7V2aqXMFwp2JFiNOAqfzeNuw40i57ebM7yUJ6amX8WroPuxr4mM3sjbBlNLXVAoBqnpy5Rs+z2MExCpSxYWNilWnNqjyjz7tHIMifMlM2Wo5hQoeXDqDCTyqEdgsXKdoW1piSsrd8xYebA+UUeInFaVcap9NS1I7iJajMcswDhLnzVzcCGYmbnaXLGUucygBQm5MeY3crOzyh+ycP3XdysmbKCrMRq7jkCzekFpxeYSwpwSSluBKiOOoeB8qpZCylSkjL8J0rWnxUakEKlGUEkkBKah2cm4sOJLn8YJOwjpDjNPekUZizPV1DL4vDZUhQWoklVEgktZi5yvxAFYr8BM71ip/ioQSKClXuKmLFWISgKUAAk1d7sWpWJvQy2SJRmyqWAhqBr0JJD8DeItoY9MsLy3fN6u8CDFGbLSbO5zF3DglN+nBoDlAzJalqOUvl+sKCpDAAmnR41b7AMl7SKwVb2YJFAzbx6ip+6BMMiaVjPSW9SSOe6CFkkmlKdYZgkd3nUoOCwLnh/CXGjtzi2kozBKlOzulgavqQwYWAhZKpaGirW2VmHkd33qjnmqKlFDu6XuE836Q5OyCveIKXqxKgRW1KRaSUIDEJs4cvezVPKDciTXKo/nmYOTvZkYI8uNKKcg+hix7O7WMs92SyVHU2Jb7orQpJSXO8A3WIDLIAVoaPH0klaPm4ScXaNpLxai1aIDl+FDodXeHTDlFzUgamp3fD88Yy+z9qKl0O8ktQ6MCAR525CNPgcQmYnMghhdNMzl2CuFWqNbRGScTqhLl/JISLPpS9Ax49BFhsvGZFBRf6p4kFnBGod6RWGYxrL3qh7/AAgEkl738hE0gKqcgcBy6uBICXbgfU8IV9Dx0zebPnJyjIXHM1Trl8NHghUzM9Nfb2rGIw2JUkhTsWFQdGBL8rD5Qdhds5lAgZVNWjJNS6hXWJcWdSyrplnNwMvMaPckElquc1NfxhszDhQyKCTfLmPQAPpwF4AxG0Dmclhx0iaXiMwdSg9muPz4PWG2L9IBNw5fuwohQLgFxwZlV8oN2BsxU/EJkqBy1KwdAKmxo9vGJpqEzkuqpGiQ1izv63jZ9jtnd1KM1eXMqyv4BZz1fwaG5CfppsE/SFjCJAwyCypl2oyEkU8TToDGQ7OSN6VJUTvTQCBwca8Ke0P2vtRU/ETJlkmiQSxygskVsTU+cD7OxPdz5a6slaSU0e9fR7RquqElTny/0ejdq9o9xJDUzHK40DVI9Iy0taQmWQoBrBqHM9Bw+UaPtrhO8koVohbk8iCPfLHnBmTAcgDhyfhdqtRuhhYqys58WbPZM4ycRLyn9nM3VJqzmxGgLt68Yt+1oyoEyjih6X+/zjM9m5n6xNkoPxS1BSqH6FQaUd2pz5wR+k/aikHDSEXmKJVUClAAeR3vKEyPirHg0+iuwfaQSsRLW+6DkVY7pYlRbkxi9/SFs8KlDFJAJlhlHiglwX1ZVf7xjz+egJCR8RBY6CruTxj0bsRjhicIqRMFUDuyDqhQ3Dyo6fCOSE3luMi7jxdo8qXOZVd7vFABIOjanT8IOkoDKcKYKbroABc/eYW0dljCTZgWM65ZYE3Y/CRwdJ9YrFhYUshQVlTRIVqfi8mIjlf2KLW2T7TnMrKCWSLWfwHyiCTtgrmCXMBIUGAYtTi/xWt/SINihU2WoEEusgLJozD4bE3/AC0E7UlqQlCZaDMUMuoccSRoPK8MopaMu9oIxM8JSSC5QaJSA45N09hE8jZswSx3hSVEABIawc+Z8RwioweHKKLyJK1lJqSoVIDqqBpqXtQxdbQxzrQhJDhQc3IAdww1NYxx8HVPbJJaUALSk51ooCpnqRRrC4HSK+ZhyVy0jNQkFqJqSRYMfnBOFwi0zVzFGmQBILE5nJVYkAOBUvyEcTNPfyg43wtzSjBybuaC2jwKl0b2jpkokJLstYBUaOqrOqClSwRLCQakFqWIpS+jtzhHuxMSkkqdLs1KW9/OEvEZHUk1NGppoPPWEb9GitCw4YOo1dRZiCwdI+/wiOTjipIUhIKTYlunGGSipSQFkOTYkGhUSASKGkTDGZd1IYCgqLaQWbxR5YK9YkRNIDPThECVRKVB3j6RHzLQ5SWLRJJmlJCkkgjUGIlqcu8OBgFNDs/brsmaEg6LqzkvvAeNYvkqBSSFVUb5QQQ7B+OtPGMEa2eCsPOmo+EqA5c+XhE5Y0+i0M7XezZzpiRulKgCDUhhRnvQVPvD507gpL23gwYsb9OcUmxdtKCiJxJS3Cr6BxpV4C7e7VSZSO5Uqq99nZgGGbxaIyTi6Z1Y2si0zW4fEJWPiTXgQejHo134RKrMgZgmzksK+LX84wf6N5q1zJwLkZQW0d78jePREZwAcpJrQFL+D/OEc0tFf02GbCK5s1EqrrISS2g+Iu9wAS0brtXjRJkCWmmbdpokCvyHjGe7AqzYjeAcS1EcRvJHhQmO9s53/wApj9FCQPEkmhob+kY5KrHSaVFFiMOmYCd3OGqRdtDz4RVKlEul1pNABow1B4cng9coFbhID3t4dbRL3TOrKzt+PS0MsqRKWJy8N92axacThjKXUoHdLuCQzA2FxrxBjBbSwKsNOKD8YNFWcVyqHgfOmkE7C2scPNCyVFNiDqLnqRd+UegYrZ8jFiVMLKA3kkWUD9E8Ry/GNUl4M4NorexWze6k98sALmByTfLcO9nZ/KMZ2hx4nYiZNb4mSg8EpBZuDuT4xoO3/aPIRhJShmVWabkJykpQG1JAfl9qMelwkAnecDqfyescPysjejpwwSK6ZJUuYgpQaJqSaJr1uzxo+yu0xh8QFKLJVuzC9KsHL2Zgej8YEICBlHUPqS5MV6pZy5ATvqcm5AFAwI1vHHGb5KvC7iqNl+k/ZBUZWISzA5ZtWoHUg+bp/vDhHn+GRllzJpoZhAoACBmINRex5Uj1XtBNKtkKWrNm7hCy28rMAlVOJePKJS5isJKBQtKgrKp2CrgA0etfeOvPD6r8ZGD1QthqljvcrnKoFyUm9wGpYWHJ4nkyXmBXFKx8JcOxF6XBa1DEWydimTMWssSvLnqSU6s5Lmpd+AMWOzsGoFUxZLOQEvupYNRxQ84hNxt0PGLpAmGwpTJXNmtmUM2VPEENYuTT8tE2A2SQlEyYSCS5BABy3Cer5a8o5Iw82Ylct8iQaEpUdXd1Blcb8It5+HzhKSsOKOKM+iQNW5UhZS2UUbQPiqMihJqfmadRAqJTTczkHe4Za0Yah6Q7a0srJZQSHy2ckU1B03tHtESsSEslRUVF6uSSAAVKA5NaFXQWBS8WB35spJIOYhmABIT46gXiFGNK5WfUkhk8WGo5N5wejZpTNUlUsgTCVE1ckh2VkDCmr8AzxIhaUo7tCA6RmNMxG8xSGBLm/jDvXgquitkkJWkJckAk5A7m28XYPUOYsRKQQHuw+sdOOsTKnhUlC0pKAoPvDLpby0pFBMx8sEgzQ4oWLxOpS0Uk0mYtCUc/OJ0iX/F6QMmHgx9IfNsJeXwV5j7oJkzpIuhXn+EVyzWHoDxohcS8VIB/dn+Y/KDsPisN/unfiuZFFKwilcvy0WmHwFK+0JJpelIKT8LALwjKUZeUAEk94tg3URke0O3pExBlYeWpIJGZS1O4BcBIalWL3pFh2ql5MOQNVAHnV/cCMREXI7sUFV1s1XYztSMJnQtJKFEF0s4Ni/EN5R6fs/aiJqEzJZCkqsR7cRHg0ehfo3nHuZidAtx4pr7ROUUy/Jo9X7LbSTLxKFEABe4T1t/iAi+7a7NcpxASCwyrpYO4PSp9IwMirRvOz3adOUSsQagMFmxHBfPnrrzxLwy7MgRLeqR84nTOT/F4H8I22I7K4Wac6XS9XlqGU9AQQPCOyezmEkb66gazVDKOoonzg4hbKHZGwhigFKQRLF1k1VyTT1tGkxm18PhDLk0SLMkUQPrK8fG5iq2z2xQn9nh95Vs7bo+yPpH06xhsRiCtRUoklTuTUkw1UtGOR6B2l7MIxP7eV+8y6EZZgo3LM1lcKHlhlp7slKs6SCQUkAEOXaC9gdq5mFKUEZ5JLFL1TzQT/lNOkbgTMFj0h8izwJyzE+yvlHLKKydaf5LRbj/B54VS9SoliHpbpEmyNnHELRKlKW4d1ZUnKLEqL8KD8Y257E4d3zTW4Zg3+V/WHYraeD2dLKUZcw/2aDmWTpmJqOqvDhE44Gnc6SHeS9IG7fY9MjCiSk5VLZKWALBLF2PRI8Y852RMlpQCtSpiTMzELIFRZimwCg/pA20tuzMauYuYQ+bdSLJSLJH5qSYFwq2wqeSyfUwuSfKQRVI02Ex0ouMgd6kLFXSBEgxKFPupZlZgVO/nQjk3Dxy+ytolUyYl7Mfl8oPweLqRxf5xN2n0Ui012XIxcsucoFD9Kj6H8I4RLJSSCaj6bDW7dfaKeViN1an4+kHGe6UqhHJpjrocmRh0TFKCVh7pExWX6Vanio+kNwsrCofJJYkMVFSituGYnMPAwJtJTKJ4xAk/nwgUn2ZoP/UsOlaknvSSLKnLUkZkvRKlFJvYgw/D4XCCUpCZP7MklScxAJIYuHYhha3BorMRinnm1Ep4fUAhuHngyyaa/OHlKX3NTRpNnrlS5ZTJkIRL+qkJHWhiWXjJbUlJbwHoDGek4gCUAwMADEHhE7bY8mlo8/y0h7MkcY6tTBoZKBUQI+j6PmOxCLTA4DMxIPofnEmCwgAJOUsefTj+TFhRIoOI4aGElIpGHrH4fDhLUGv+Yt7QWiYMpgUqDt+dXh8gE0rXr10vE2WTrSKztbKKsOrKHykK8NfeMDHr+IkolS1TZhTkSHVmSqtAMrOHclvGPJMQoFSiBlBJIHAPQeEIdMOiON3+jqSe7mq0KgPJJ/1CMJHrPYqaibh5YlpCWGVSRXeFyXrV83jAbLo0WClUJ+Z4xPPmBJA5G/SAJ+LA3EafVqfIiB8RNqBq1aM3UNfxjaJuVINVtBQcIUU0FQTxrVJgGdNUqpUVGnxEk+ZMMQwNeHXhHBWvhwhkSk7DJUx1Dn90MQveSnnxhsktUaH8PzeJxgSU5yBfiOOhz/KA3bWiDFA5SQDQ8KfRs0BS8YKhW7UAOWq5Gt40kzCBMtADbxFPK9YD2rsVJTnABZiLjV9ViOXNhUtnTjk0qKrGY+ckpHeTMtiMy210doXehja3vAmIWSK/W4g6wP3pc9OPAxxuNovyo5LBQQsO2t+IvTlE0ic4XKPBx5vTzgVOJHwqIANBrr6QxThdBpld/X0gpmXom2LNBXNL8B87wZ3uSal6BzU0Hwn5xS7OTkK7ioNfyInxeLKk5gQSHpb5kw7jbMUqRZYPGbq0lhQ1J4hx+EPk44hORQZlUdx8ucUkqcp1JNKD5C/yi2xUoKlCYGJYGlOGgB94WUVeykZNrRb4teYdPwgIzwFpHEgekQDFK71KDYu/gzViDFqYorULB8IVQ8GcvQgpImrJ+kzc2BiOXmShQPH3eDMUBmSRxqbUhk0A2ZiLg8IzwEtAqZ5ZPIwUmkCpltmSRa1GuH94IUscR5/jCtDN32YhEoqISkFSlGgAJPgBUxoMNswykkFSsztlIKTr9F39Ii7M4RJUqaoOUZclSwV8TsK0AgnamMUZiiWfM9n5dfCPdbt0jw4pRhyY/ESikgF6gXcaczEYSS9eJt6UgObjlKKbVawbkIsZTMCQXOg4NegMY1xNhJTdIjxSSlJVmS2tjpZkl/SJJE2YlilaARaqvRo53aNE5fN/8sMSE1r6W8hCNnSoJEm2MROxMkyFLQEqY7oINCDw4iMhN7LTB/tEH+b7o2CEo515K+6JUyUHi3Fl++WEKmH/APa8366P8X3Re7BE/CJUlCpe8cxcF7AUqGtF9Lko0J8l+5TEa5KNT5BVf8LRqZjRXHac9zvJHQK+Rh0jaawrfKSmrslQPW5h+IwqCSxNeRH4QPisANFKDaFL+sPZJwRc7Ux1d0AUFjyFYtdiYRSpHeMpW+T8Liw1ufwjJTMoASnOSBXOx8mAYci9I9OwCES8LKl5gDkClAkA1DmwrWkNNpRVEMUJPK+XiKuVIAzWdy6SzCtG9YsMNiHQhBYEqLjkKj3gTGTEpVMciiQ2uvhA2ExIMwDMN1KjdmtoaRM6dJ0HYmc6kpqCmwAd6gOK8KxYzlgIIcDxaM/s6eDMzkggWmFgKgin1vOCsSsrSAFEjkGfS5o3KBo1S02QbRwSWT+0IzH66joW+lrGWVuqYvrqfKtY0u1pqQUAs7pOU+Zb1MU22JaTMdDEFi9r3iOXDatBHJumUs9Bz6kUINWJBGsEy8QylOUhw12fpSIMSlglRLaX52Y9ISzunLlzU4u3tWOZqyydEm0Q4BHjr72gVOCfKctLvlpQ8Qp4lM05QHvSrBydIKmzmBS+VKWBFmdiQ/nBTjoLTGrAqaE0FC9+XWJMLPIQUKzEOQkMABuuObQHkKVqoQk1HOtGg81ygas45i/pCNaGskw09ClBRuA1eNbZfCBMTMJCqklJD6kfhDTh1JzkDRx7cYiY51OndPvTxjYo1y1QecalZY3FXLAX/CHYdbSyAXIe1vzaKZEx10LfR1iwwk5rlwxzV62HhBKNGwlYeMQSS+oB00EB4nDEqJCqeP3wu+SLHQN0gkEGriF66NuwDZycmEC8yklRdwQNSBVvqiKmZiSolz11iXHEoQmVmO7oDSJth7JVOOYg92DvFjX+EMDX2j2YauTPGy3JqER+z5ad0qBbSianmTwi1ROzEhidKEU57vSLSTswG8uYwt8YA0AACKQ6fhUj/ZE+K/8AREpy5M7MWHgqKeYEmylP9s/IQk4YamZ/Ov7oLnkJsG0bMo+8t44lQVdIpxK/nLhCtEQSBbP4lR9xDlJD3mHqV/JMOSw0T/Mf/HCE8WKU/wAw/wBEBoxk65/EzG9o53Q/i/7je0SpmJ0yP9tP+iECkO5T4Ll+m5AAJNkpp/8As+VISZKeB8lA+eWJzk1WgdVSvnLhhy2zJ5fu/kiNsyiObKoCEq5E5vZo12yNq98lCFHKWCDZIPR3rRvKMosgUdDGl5X3Q2TPEtQWhwQfo936FuEYCNVMkiZMIVrRgWIufciK6TJWieoOBuE0JNKBhwPSCJUuZMQJsrvCeI7snmKV9IrZsqfLUtakzEhviWm9mqE8R7RSKZDI0mE4dBByopvIclZUtWZQFU214RJj9pS5TIBOYC7VFTxDGjRSf+oqSXamVviIPFzV3eA5KCtehf6ym8yo+8Oo32QeWlUQrE4pa1Z1qUQKAkDpYe8aLs9spagJhkoUhQBSVrKfEBLnzEV+D7IT1qCl91k4Fai/Qy/vj0DDoCEhKaAAAfnWGlVaExKTbcjG9r5KxMKig5SBYFSaBmzEUvy1jHTEHM7U/pHqPaDZ/fIcKIKXPxEAi5cC9o8vWsZizvYu2lfnHBlhUrPQjK1QLLxBTUqO6aOyWrx+k9IPmALzm4UAxe4q5HKK+bhcxUyRVqeLOTpUQfh5IyoQaDKoOHalWep4ekJKjY2STw4Q1gQCPMV8BDwgujKEsVZQ5D2pR4GxOISAz0Jp4cYN2dtCX3RSSBlN1JzC1LG/OJtOiiabpjVqIzO1aECvK/WIk4VK8oqCdLsaBrRYoRnG6ZSs1gQSa1Bpq3vAU1aZcxlMnK5o7aFwaQqGaADs9I3sxcKdmaxZntDp61JLBSddDr0tEs/E3FC7keNaxP3QUkEkORorlqAbxsr7ZkavRVqnkKQN1iCFeF2rUV4ROuet6TKabqYgnyBQhPwl31FL8RUQIcVMVUrbwT84fjfRNumF7SkArqpKQalRIADi/PprBuFxMlISlOJltpva2f4hXWFs74Zv933MTY76P2Ux3yb6IY4r9xIjGoJb9alnrNI5fX5xIZ41xUv/AKin/wAxgWV8I/PCGq+IQhYMVNSA4nprZ50xj0qYemZTcnp6CfN++JZP3QZh7eMYaAqnMP3wP/PmCF3o/wB4H/48z/TFriLHr98RKtGG0V2cv+8S/wDxl/NEPTnBrMH/AFj/AOOJMb8X55QEL+AgAmXOIUAZ0sE2/b1t9iIloU/xpP8AzT75I6uw6RXTPi/PARopbSpc363/AHfvRA+LxQRuqJr/ABj03KwHhPjgHaf0/s/MwAts2HZ7avdEKCgZS7vMFvrJGUOeUaXEbKTMDomzEPV0K3SOgpHlmyv3Ur7I9jHqPZz+zS+nzMUgyOWJTYvseo/DMSr7TpPRwDBmG7IyAll5ieSmalQKVjQxwxQhxQsNLCEhCRQBhb5RJmiMQoDbH5oxv6RnEtBAbeqpg1mAKrvyjXGK7bv7lXhCzVoZSpnlBnkEsSKipr4RbyFkyiSpCiHY2UOLMa29opcZeZBOzvhV0McMkdUJbLLs1LCkklSksTTu0rBtWoJ8oj7RpKphAY5gGDMzOLO5PyalIs0f29P2Ydt3+0Sev/1XGelq+mir2eCiahJUlK0Agj4wWqQ6QaNrS0F7XxneZBmTmH1TmDHVlfCaWrEOI/tM/wD4Sv8AKmKE/vkdD7mM47M5UqCMVuqel/qsfb0iYoKtSwLWHDUFuVot537hfj7iKI2V1+UZZjjRdYPvQmiAUFFD3aTp5xUqkzf93/gUPlGo2L+4R9lMHybCJKWyzhaR/9k=', use_column_width=True)
    with col2:
        st.markdown("<h4 style='text-align: left;'><strong>Problem Statement</strong></h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.</p>""", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left;'><strong>Domain: Travel Industry, Property Management and Tourism</strong></h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: left;'><strong>Technologies Used:</strong></h5>", unsafe_allow_html=True)
    multi = ''' 
        1. Data Preprocessing/EDA
        2. Python scripting
        3. PowerBI
        4. Visualization'''
    st.markdown(multi)
    st.markdown("<h5 style='text-align: left;'><strong>Overview:</strong></h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>By leveraging Streamlit for developing interactive web applications, this project aims to provide a comprehensive analysis of Airbnb data. From data cleaning and preparation to interactive visualization development and dashboard creation, the project aims to uncover actionable insights that can inform decision-making related to Airbnb listings, pricing strategies, and market trends.</p>""", unsafe_allow_html=True)

if option == "Dashboard":
    col1,col2 = st.columns(2)
    with col1:
        unique_country = df['listing_country'].unique()
        option_dropdown1 = st.selectbox("Select the state",unique_country)
        room_type_df = df[(df['listing_country']==option_dropdown1)].groupby('room_type').agg({'price':'mean'})
        room_type_df.reset_index(inplace=True)
        fig = px.pie(room_type_df, values="price", names="room_type",title = 'Average price of each Room type', hole=0.5,width=120,height=160,)
        fig.update_traces(text=room_type_df["room_type"], textposition="outside")
        fig.update_layout(
            showlegend=True,  # Show legend
            margin=dict(l=65, r=65, t=65, b=65),  # Adjust margins
            width=300,  # Set width of the chart
            height=300,  # Set height of the chart
            paper_bgcolor='rgba(0,0,0,0)',  # Set background color to transparent
            plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
            legend=dict(font=dict(size=9)),  # Adjust legend font size
        )
        st.plotly_chart(fig)
    with col2:
        st.subheader("")
        df['listing_rating'].max()
        df['listing_rating'].min()
        bins = [-0.1, 0.0, 25.0, 50.0, 75.0, 100.0]
        ages = ["No Reviews","Poor", "Avereage", "Good", "Very Good"]
        df["Descriptive_listing_rating"] = pd.cut(df["listing_rating"], bins=bins, labels=ages)
        plt.figure(figsize=(20,11))
        bar_plot=sns.barplot(x="room_type", y="price", hue="Descriptive_listing_rating",  data=df)
        plt.title('Price by room type and descriptive rating', fontsize=45)
        plt.xticks(rotation=360,fontsize=30)
        plt.yticks(fontsize=30)
        plt.xlabel('Room Type', fontsize=35)  # Increase x-axis label font size
        plt.ylabel('Price', fontsize=35)
        plt.legend(title='Rating', fontsize=30, title_fontsize=30)
        fig = bar_plot.get_figure()
        st.pyplot(fig)
        with st.popover("Observation"):
            st.markdown("In price the most contributor is Entire home/apt but in Rating shared room has the highest rating. " 
                    "The price of shared room is lower because the count of listings is less.")
        #fig = ff.create_table(room_type_df, colorscale="Pastel1")
        #st.plotly_chart(fig)
    col5,col6,col7 = st.columns(3)
    with col5:
        Rating_desc = df['Descriptive_listing_rating'].unique()
        option_dropdown2 = st.selectbox("Select the Rating",Rating_desc)
        option_dropdown3 = st.selectbox("Select Top/Least ",['Top ','Least'])
        if option_dropdown3 == 'Top':
            Flag = False
        else:
            Flag = True
        Room_type_df = df['room_type'].unique()
        option_dropdown4 = st.selectbox("Select the Rating",Room_type_df)
    with col6:
        property_df_most_reviewed = df[(df['listing_country']==option_dropdown1) & (df['Descriptive_listing_rating']==option_dropdown2) & (df['room_type'] == option_dropdown4 )].groupby('property_type').agg({'number_of_reviews':'count'})
        property_df_most_reviewed.reset_index(inplace=True)
        property_most_reviewed = property_df_most_reviewed.sort_values(by='number_of_reviews', ascending=Flag).head(5)
        fig = px.bar(property_most_reviewed, x='property_type', y='number_of_reviews',width = 200,color_discrete_sequence=px.colors.sequential.Agsunset)
        fig.update_layout(title={'text': f"{option_dropdown3} 5 Properties based on no of reviews",
                         'font': {'size': 12}},  # Adjust the font size here as needed
                  width=250)
        st.plotly_chart(fig)
        
    with col7:
        property_df_most_reviewed = df[(df['listing_country']==option_dropdown1) & (df['Descriptive_listing_rating']==option_dropdown2) & (df['room_type'] == option_dropdown4 )].groupby('property_type').agg({'price':'sum'})
        property_df_most_reviewed.reset_index(inplace=True)
        property_most_reviewed = property_df_most_reviewed.sort_values(by='price', ascending=Flag).head(5)
        fig = px.bar(property_most_reviewed, x='property_type', y='price',width = 200,color_discrete_sequence=px.colors.sequential.haline_r)
        fig.update_layout(title={'text': f"{option_dropdown3} 5 Properties based on the Average price",
                         'font': {'size': 12}},  # Adjust the font size here as needed
                  width=250)
        st.plotly_chart(fig)
    st.divider()    
    col3,col4 = st.columns([3,2],gap="medium")
    with col3:
        R_df1 = df.groupby('listing_country').agg({'price':'mean','listing_id' : 'count'})
        R_df1.reset_index(inplace=True)
        fig = go.Figure()
        trace1= fig.add_trace(go.Bar(
        x=R_df1['price'],
        y=R_df1['listing_country'],  
        orientation ='h',
        name="Average Price",
        marker_color='indianred'
        ))
        trace2=fig.add_trace(go.Bar(
        x=R_df1['listing_id'],
        y=R_df1['listing_country'], 
        orientation ='h',
        name='Total count of listings',
        marker_color='lightsalmon'
        ))
        fig.update_layout(title=f'Average Price & listing count by Listing country',barmode='group',xaxis_tickangle=-90)
        fig.update_layout(
            showlegend=True,  # Show legend
            margin=dict(l=65, r=65, t=65, b=65),  # Adjust margins
            width=450,  # Set width of the chart
            height=300,  # Set height of the chart
            paper_bgcolor='rgba(0,0,0,0)',  # Set background color to transparent
            plot_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent
            legend=dict(font=dict(size=9)),  # Adjust legend font size
        )
        st.plotly_chart(fig)

    with col4:
        container = st.container(border=True)
        container.write("1. United states has the highest count of listings. ")
        container.write("2. Portugal offers the least price listings and offers the low price when compared to other contries.")
        container.write("3. Hong kong charge the most for renting the listings. ")
    col3,col4 = st.columns([3,2],gap="medium")
    with col3:
        plt.figure(figsize=(5, 5))
        hist_plot = sns.histplot(df['accommodates'], bins=20, kde=False, color='green')
        plt.title('Distribution of Accommodates',fontsize = 12)
        plt.xlabel('No of Accommodates',fontsize = 10)
        plt.ylabel('counts of listings',fontsize = 10)
        plt.tight_layout()
        fig = hist_plot.get_figure()
        st.pyplot(fig)
    with col4:
        unique_accommodates = df['accommodates'].unique()
        option_dropdown5 = st.selectbox("Select the no of accommodates",unique_accommodates)
        with st.expander("Lising Name"):
            accommodates_data = df[(df['accommodates']==option_dropdown5)].copy()
            acc_sample = accommodates_data[['listing_id','listing_name']]   
            acc_sample.reset_index(drop=True, inplace=True) 
            st.write(acc_sample.iloc[:500])

    st.subheader("Airbnb Analysis in Map view")
    df = df.rename(columns={"listing_latitude": "lat", "listing_longitude": "lon"})
    st.map(df)
