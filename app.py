# Importing all the necessary libraries
import streamlit as st
import replicate
import time
from googletrans import Translator

# Create text-to-image generation API model
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")
translator = Translator()


# Visualize the design of the web application
def main():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2641/2641264.png")
        st.title("Cube")
        st.write("Ali Valiyev | 35")
        
        # Create bio for the user
        with st.expander("Biografiya"):
            st.write("""
            Mening ismim Ali Valiyev. Men Andijonda o'n yildan buyon faoliyat yuritaman. Asosiy yo'nalishim 
            sharqona va g'arbiy interyer dizaynlarini bog'lash. Men har doim mijozlarim bilan ishlashdan xursandman. 
            Cube ilovasi esa mening ishimni ancha yengillashtirdi. Qoyil!""")
            
    # Open menu slider with several options        
    menu = ["Sarlavha", "Takliflar", "Dizaynlar"]
    choice = st.sidebar.selectbox("Menyu", menu)
    if choice == "Sarlavha":
        st.header("Sarlavha")
        st.write("Oxirgi bir necha yil ichida interyer dizayni bo'yicha ko'plab mutaxassislar o'z loyihalari atrofida "
                 "moliyaviy, masshtablash va vaqtni boshqarish muammolariga duch kelishdi. Yangi stable diffusion "
                 "modeli bilan ular endi o'z mahsulotlarini ancha yaxshi loyihalashtira oladilar.")

        st.write("Ushbu model qanday ishlaydi?")
        st.write("Stable diffusion ish vaqtidagi “tasvir yaratish” jarayonini shovqin bilan boshlanadigan "
                 "“diffuziya” jarayoniga ajratadi. Keyin shovqin yo'qolguncha va natija taqdim etilgan matnning "
                 "tavsifiga yaqinroq bo'lguncha tasvir sifatini asta-sekin yaxshilaydi.")
        
        # Create two separate columns for text
        column1, column2 = st.columns(2)
            
        with column1:
            st.image("https://pbs.twimg.com/media/FdEriAQaEAENQyj.jpg")

        with column2:
            st.write("Stable diffusion asosan matn tavsifiga asoslangan batafsil tasvirlarni yaratish uchun "
                     "ishlatilishi mumkin. Bundan tashqari, uni tashqi bo'yash, ichki bo'yash va matn so'rovi "
                     "yordamida tasvirdan tasvirga tarjimalarni yaratish kabi boshqa vazifalar uchun ham qo'llash "
                     "mumkin. Modelning asosiy xususiyati sifat va tezlik hisoblanadi.")

            st.write("Bizning jamoa Google Translate freymvorkidan foydalangan holda, mahalliy aholi uchun ushbu "
                     "modelning prototip versiyasi yaratdi. Bunda biz o'zbek tilida kiritilgan matn asosida Replicate "
                     "stable diffision modelga jo'natadi. O'zbek tilida qabul qilingan ma'lumot ingliz tiliga "
                     "o'girilib mijoz uchun ma'lum bir muddat mo'baynida rasmni chiqarib beradi.")

        st.write("Kelajakda ushbu ilovaning ancha optimizatsiya qilingan versiyasini yaratish bizning maqsadlarimizdan "
                 "biri hisoblanadi. Bundan tashqari Web3 yordamida ushbu ilovaning yangi ko'rinishini hamda Meta "
                 "versiyasini yasamoqchimiz. Albatta, bunday o'zgarishlar bilan mijozlarimiz xursand bo'lsa, biz ham "
                 "xursand bo'lamiz. Bizdan foydalanishni davom eting!")
        st.write("Ravshan Sunnatillayev | @flamewalker, Dilmurod Abdusamadov | @thisisdilmurod")

    # Add image generating feature
    if choice == "Takliflar":
        st.header("Takliflar")
        
        # Gather input from the user
        user_suggestion = st.text_input("Matnni kiriting", key="suggestions")
        translated_suggestion = translator.translate(user_suggestion, dest='en')
        
        # Snooze the time for better functionality
        time.sleep(1)

        colum1, colum2, colum3, colum4, colum5, colum6 = st.columns(6)

        with colum1:
            st.button("Download")

        with colum2:
            st.button("Share")
        
        # Create some vacant spots to open the space for buttons
        with colum3:
            pass

        with colum4:
            pass

        with colum5:
            pass

        with colum6:
            pass

        output = version.predict(prompt=translated_suggestion.text)
        st.image(output)

    # Add designs/gallery feature
    if choice == "Dizaynlar":
        st.header("Dizaynlar")
        st.write("Quyida siz bir necha xil avvalgi interyer dizaynlarini ko'rishingiz mumkin. Siz ham o'zingizni "
                 "mahsulotlaringizni boshqalar bilan ulashing va yordam berishni unutmang!")
        st.write("")
        
        # Layout the previously used designs
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://replicate.delivery/pbxt/ZgRvaC9Ol3a3AJwkP8fUKvqHaYRSrqXKEli3WfK9DR9n6INQA/out-0.png")
            st.image("https://replicate.delivery/pbxt/0KnK657qsGqBO5YxnjDlub6dAGOye3EDfGSc8IayeLyDIAagA/out-0.png")
        with col2:
            st.image("https://replicate.delivery/pbxt/BRFhAsoz97Z6ANR9Q3s072iRaM3u8MPUc65u8QGgfOJI1hGIA/out-0.png")
            st.image("https://replicate.delivery/pbxt/jFwyWIpIU8b2KFsKLo3pKrciXDLZMsHIN1cLtdr1OdMWesGIA/out-0.png")

        with col3:
            st.image("https://replicate.delivery/pbxt/UbTGWrjuc9bfTy67UBlz0v4dvVPV90t3ZF8J8mfggJ6dDANQA/out-0.png")
            st.image("https://replicate.delivery/pbxt/G956h9Wup2KZAtMSBgyzdI5fpeK1QxgJ6a4cp6AbBeWelfnBC/out-0.png")


# Reiterate the run (OOP)
if __name__ == '__main__':
    main()
