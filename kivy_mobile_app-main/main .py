from kivy.app import App
from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import sqlite3 as sql
from kivy.properties import ObjectProperty
from database import DataBase
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window

kv_string = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory

#:set text_color get_color_from_hex("#4a4939")
#:set focus_color get_color_from_hex("#e7e4c0")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#f7f4e7")
#:set selected_color get_color_from_hex("#0c6c4d")

<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color

<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True

<CreateAccountWindow>:
    name: "create"

    namee: namee
    email: email
    password: passw

    BoxLayout:
        orientation: 'vertical'
        spacing: '15dp'
        padding: '15dp', '15dp', '15dp', '30dp'
        
        Label:
            color: '#000000'
            text: "Создайте учетную запись"
            size_hint: 1, None
            size: 1, '50dp'
            font_size: '20sp'
            
		AnchorLayout:
		    anchor_x: 'center'
	        GridLayout:
	            cols: 2
	            rows: 3
	            spacing: '20dp'
	            size_hint: 1, None
	            size: 1, '220dp'
	    
	            Label:
	                color: '#000000'
	                size_hint: 0.25, None
	                size: 1, '50dp'
	                #pos_hint: {"x":0, "top":0.8}
	                text: "Имя: "
	                font_size: '17sp'
	
	            TextInput:
	                id: namee
	                size_hint: 0.5, None
	                size: 1, '50dp'
	                opacity: 0.8
	                multiline: False
	                font_size: '20sp'
	
	            Label:
	                color: '#000000'
	                size_hint: 0.25, None
	                size: 1, '50dp'
	                text: "Почта: "
	                font_size: '17sp'
	
	            TextInput:
	                id: email
	                size_hint: 0.5, None
	                size: 1, '50dp'
	                multiline: False
	                font_size: '20sp'
	
	            Label:
	                color: '#000000'
	                size_hint: 0.25, None
	                size: 1, '50dp'
	                text: "Пароль: "
	                font_size: '17sp'
	
	            TextInput:
	                id: passw
	                size_hint: 0.5, None
	                size: 1, '50dp'
	                opacity: 0.8
	                multiline: False
	                password: True
	                font_size: '20sp'
                
        Button:
            background_color: '#00BFFF'
            size_hint: 1, None
            size: 1, '60dp'
            opacity: 0.8
            font_size: '20sp'
            text: "У вас уже есть учетная запись?"
            on_release:
                root.manager.transition.direction = "left"
                root.login()

        Button:
            background_color: '#00BFFF'
            size_hint: 1, None
            size: 1, '60dp'
            opacity: 0.8
            text: "Регистрация"
            font_size: '20sp'
            on_release:
                root.manager.transition.direction = "left"
                root.submit()


<LoginWindow>:
    name: "login"

    email: email
    password: password

    BoxLayout:
        orientation: 'vertical'
        padding: '15dp'
        spacing: '15dp'
        canvas.before:
            Color:
                rgba:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'pngwing.com.png'
        Image:
            source:'paint1.png'
            size_hint: 1, None
            size: 1, '200dp'
        
        AnchorLayout:
		    anchor_x: 'center'
	        GridLayout:
	            cols: 2
	            rows: 2
	            spacing: '20dp'
	            size_hint: 1, None
	            size: 1, '220dp'
                Label:
                    size_hint: 0.25, None
    	            size: 1, '50dp'
                    color: '#000000'
                    text:"Почта: "
                    font_size: '17sp'
        
                TextInput:
                    id: email
                    font_size: '20sp'
                    multiline: False
                    opacity: 0.8
                    size_hint: 0.5, None
    	            size: 1, '50dp'
        
                Label:
                    color: '#000000'
                    text:"Пароль: "
                    font_size: '17sp'
                    size_hint: 0.25, None
    	            size: 1, '50dp'
        
                TextInput:
                    id: password
                    font_size: '17sp'
                    multiline: False
                    opacity: 0.8
                    password: True
                    size_hint: 0.5, None
    	            size: 1, '50dp'

        Button:
            background_color: '#37A4E0'
            size_hint: 1, None
	        size: 1, '60dp'
            font_size: '20sp'
            text: "Войти"
            opacity: 0.9
            on_release:
                root.manager.transition.direction = "up"
                root.loginBtn()

        Button:
            background_color: '#37A4E0'
            size_hint: 1, None
	        size: 1, '60dp'
            font_size: '20sp'
            text: "Создать учетную запись"
            opacity: 0.9
            on_release:
                root.manager.transition.direction = "right"
                root.createBtn()
                
<MainWindow>:
    n: n
    email: email
    created:created
    BoxLayout:
        orientation: 'vertical'
        padding: '15dp'
        spacing: '15dp'
        
        AnchorLayout:
    		anchor_x: 'center'
    	    BoxLayout:
    	        orientation: 'vertical'
    	        spacing: '20dp'
    	        size_hint: 1, None
    	        size: 1, '220dp'
                Label:
                    id: n
                    font_size: '16sp'
                    color: '#000000'
                    size_hint:1,None
                    size: 1, '60dp'
                    text: "Имя учетной записи: "
        
                Label:
                    id: email
                    font_size: '16sp'
                    color: '#000000'
                    size_hint:1,None
                    size: 1, '60dp'
                    text: "Почта: "
        
                Label:
                    id: created
                    font_size: '16sp'
                    color: '#000000'
                    size_hint:1,None
                    size: 1, '60dp'
                    text: "Дата создания: "
        
        Button:
            background_color: '#00BFFF'
            size_hint:1,None
            size: 1, '60dp'
            font_size: '20sp'
            opacity: 0.8
            text: "Войти"
            on_release:
                root.manager.current='screen'
                root.manager.transition.direction = "left"
    
        Button:
            background_color: '#00BFFF'
            size_hint:1,None
            size: 1, '60dp'
            font_size: '20sp'
            opacity: 0.8
            text: "Назад"
            on_release:
                root.manager.current= "login"
                root.manager.transition.direction = "right"


<screen2>:

    FloatLayout:
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'f1.png'

        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.7
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]



    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='main'
            root.manager.transition.direction='right'

    ImageButton:
        source:'pngwing.com (8).png'  #дети, данные
        font_color:0,0,0,1
        size_hint_y:.2
        size_hint_x:.3
        pos_hint:{'x':.05,'y':.67}
        back_color:(0,0,0,.2)
        on_release:
            root.manager.current='it'
            root.manager.transition.direction='left'

    ImageButton:
        source:'pngwing.com (5).png'  #Факультет интеллектульного развития
        size_hint_y:.3
        size_hint_x:.4
        pos_hint:{'x':.54,'y':.59}
        back_color:(0,0,0,.2)
        on_press:
            root.manager.current='screen5'
            root.manager.transition.direction='left'


    ImageButton:
        source:'pngwing.com (3).png'   #Факультет раннего развития
        size_hint_y:.2
        size_hint_x:.3
        pos_hint:{'x':.05,'y':.42}
        back_color:(0,0,0,.2)
        on_press:
            root.manager.current='screen3'
            root.manager.transition.direction='left'

    ImageButton:
        source:'pngwing.com (6).png'   #Факультет спорта
        size_hint_y:.2
        size_hint_x:.3
        pos_hint:{'x':.6,'y':.42}
        back_color:(0,0,0,.2)
        on_press:
            root.manager.current='screen6'
            root.manager.transition.direction='left'



    ImageButton:
        source:'pngwing.com (4).png'   #факультет танца
        size_hint_y:.3
        size_hint_x:.4
        pos_hint:{'x':.01,'y':.12}
        back_color:(0,0,0,.2)
        on_press:
            root.manager.current='screen4'
            root.manager.transition.direction='left'

    ImageButton:
        source:'pngwing.com (7).png'   #Факультет творческого развития
        size_hint_y:.2
        size_hint_x:.3
        pos_hint:{'x':.6,'y':.17}
        back_color:(0,0,0,.2)
        on_press:
            root.manager.current='screen7'
            root.manager.transition.direction='left'




    MDNavigationLayout:
        ScreenManager:
            MDScreen:

                MDToolbar:
                    title: "Talento"
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: get_color_from_hex("#408EB5")

                    specific_text_color: text_color
                    left_action_items: [ [ 'menu', lambda x: nav_drawer.set_state("open") ] ]


        MDNavigationDrawer:
            id: nav_drawer
            opening_transition: 'out_bounce'
            opening_time:2
            closing_transition: 'out_elastic'
            closing_time:2
            BoxLayout:
                orientation: 'vertical'
                padding: 25
                spacing: 10

                Image:
                    source: 'paint1.png'
                    size_hint_y:  None
                    height: '140dp'

                MDLabel:
                    text: "+7 (3452) 383-700"
                    font_style: "Button"
                    font_size: '15sp'
                    size_hint_y: 1, None
                    size: 1, '40dp'
                    height: self.texture_size[1]

                MDLabel:
                    text: "intera.tmn@mail.ru"
                    font_style: "Button"
                    font_size: '15sp'
                    size_hint_y: 1, None
                    size: 1, '50dp'
                    height: self.texture_size[1]



                MDFillRoundFlatIconButton
                    icon: "chat"
                    size_hint_x: 1
                    icon_size: "64sp"
                    text: 'Онлайн чат'
                    md_bg_color : ("#408EB5")
                    text_color : ("#2E3033")
                    on_release:
                        root.manager.current='online'
                        root.manager.transition.direction='left'



                MDFillRoundFlatIconButton
                    icon: "calendar"
                    size_hint_x: 1
                    text: 'Расписание'
                    md_bg_color : ("#408EB5")
                    text_color : ("#2E3033")
                    on_release:
                        root.manager.current='schedule'
                        root.manager.transition.direction='left'

                MDFillRoundFlatIconButton
                    icon: "newspaper"
                    size_hint_x: 1
                    text: 'Новости'
                    md_bg_color : ("#408EB5")
                    text_color : ("#2E3033")
                    on_release:
                        root.manager.current='news'
                        root.manager.transition.direction='left'

                MDFillRoundFlatIconButton
                    icon: "credit-card"
                    size_hint_x: 1
                    text: 'Оплата'
                    md_bg_color : ("#408EB5")
                    text_color : ("#2E3033")
                    on_release:
                        root.manager.current='payment'
                        root.manager.transition.direction='left'


                MDFillRoundFlatIconButton
                    icon: "email"
                    size_hint_x: 1
                    text: 'Написать нам'
                    md_bg_color : ("#408EB5")
                    text_color : ("#2E3033")
                    on_release:
                        root.manager.current='message'
                        root.manager.transition.direction='left'

                Widget:



    Label:
        text:'[ref=some][u][color=#4a4939]О НАС[/color][/u][/ref]'
        font_size: '15sp'
        size_hint_t: None
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'x':.40,'y':.445}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/about.html")


<message>:
    FloatLayout:
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.7
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'
    Image:
        source: 'paint15.png'
        size_hint_y: None
        height: '200dp'
        pos_hint:{'center_x':.5, 'center_y': .85}

    Image:
        source: 'email.png'
        size_hint_y: None
        height: '40dp'
        pos_hint:{'center_x':.25, 'center_y': .5}

    Label:
        text:'[color=#4a4939]Мы всегда вам рады[/color]'
        font_size: '20sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .7}
        bold:True



    Label:
        text:'[ref=some][u][color=#4a4939]Написать[/color][/u][/ref]'
        font_size: '20sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .5}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("mailto:intera.tmn@mail.ru")


<news>:
    FloatLayout:


        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.7
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'

    Image:
        source: 'paint15.png'
        size_hint_y: None
        height: '200dp'
        pos_hint:{'center_x':.5, 'center_y': .89}

    Label:
        text:'[color=#4a4939]Новости нашего детского центра[/color]'
        font_size: '20sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .75}
        bold:True

    Label:
        text:'[ref=some][u][color=#4a4939]Запись открыта[/color][/u][/ref]'
        font_size: '30sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .2}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/programs/fakultet/kopiya-gruppa-nepolnogo-dnya-evrosadik.html")

        BoxLayout:
            orientation: 'vertical'
            size: root.width, root.height

            Widget:


            Carousel:
                direction: "right"

                Image:
                    source: "Screenshot_1.png"


                Image:
                    source: "Screenshot_2.png"

                Image:
                    source: "Screenshot_3.png"

                Image:
                    source: "Screenshot_4.png"

                Image:
                    source: "Screenshot_5.png"



            Widget:

<online>:
    FloatLayout:
        FloatLayout:


        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.7
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'

    Image:
        source: 'paint15.png'
        size_hint_y: None
        height: '200dp'
        pos_hint:{'center_x':.5, 'center_y': .89}


    Image:
        source: 'chat.png'
        size_hint_y: None
        height: '40dp'
        pos_hint:{'center_x':.25, 'center_y': .5}

    Label:
        text:'[color=#4a4939]Мы раскрываем таланты[/color]'
        font_size: '20sp'
        size_hint_t:1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .7}
        bold:True



    Label:
        text:'[ref=some][u][color=#4a4939]Онлайн чат [/color][/u][/ref]'
        font_size: '20sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .5}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("http://172.20.10.2:8080/")



<schedule>:
    FloatLayout:
        FloatLayout:

            BoxLayout:
                orientation: 'vertical'


                Carousel:
                    direction: "bottom"

                    Image:
                        source: "Screenshot_6.png"
                        size: 0.5, 0.5
                        pos_hint:{'center_x':.5, 'center_y': .5}


                    Image:
                        source: "Screenshot_7.png"

        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.9
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'


<payment>:
    FloatLayout:
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.7
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'
    Image:
        source: 'paint15.png'
        size_hint_y: None
        height: '200dp'
        pos_hint:{'center_x':.5, 'center_y': .85}

    Image:
        source: 'pay.png'
        size_hint_y: None
        height: '40dp'
        pos_hint:{'center_x':.25, 'center_y': .5}

    Label:
        text:'[color=#4a4939]За обучение ребенка «Таленто»[/color]'
        font_size: '20sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .67}
        bold:True


    Label:
        text:'[ref=some][u][color=#4a4939]Оплатить[/color][/u][/ref]'
        font_size: '20sp'
        size_hint_t: 1, None
        size: 1, '50dp'
        multiline: True
        markup: True
        height: self.texture_size[1] + dp(5)
        pos_hint:{'center_x':.5, 'center_y': .5}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://cent.app/transfer/k7EQGPg97K")



<screen3>:
    FloatLayout:
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'f2.png'  #фон#4DACDB



        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            opacity: 0.8
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            opacity: 0.8
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
    Label:
        text:'Факультет раннего развития'
        font_size: '17sp'
        size_hint_t: 1, None
        size: 1, '40dp'
        pos_hint:{'x':.0,'y':.465}
        

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'PinClipart.com_clipartradio-gr_1316563.png'
        pos_hint:{'x':.39,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='up'

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'


    ScrollView:
        size_hint: (0.98, 0.78)
        pos_hint:{'center_x': 0.5,'center_y': 0.5}
        do_scroll_x: False

        Label:
            text: root.long_text
            height: self.texture_size[1] + dp(10)
            multiline: True
            markup: True                   #Разметка
            size_hint_y: None
            front_size: '14sp'
            color: 0, 0, 0, 1


    Label:
        text:'[ref=some][u][color=FFD700]ЗАПИСАТЬСЯ[/color][/u][/ref]'
        font_size: '12sp'
        size_hint_t: 1, None
        size: 1, '35dp'
        multiline: True
        markup: True
        pos_hint:{'x':.38,'y':.415}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/programs/fakultet/kopiya-1-stupen-karapuz-klab.html")

<screen4>:         #ТАНЦЫ
    FloatLayout:
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'f3.png'  #фон


        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#74991A')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#74991A')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
    Label:
        text:'Факультет танца'
        font_size: '17sp'
        size_hint_t: 1, None
        size: 1, '40dp'
        pos_hint:{'x':.0,'y':.465}

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'PinClipart.com_clipartradio-gr_1316563.png'
        pos_hint:{'x':.39,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='up'

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'


    ScrollView:
        size_hint: (0.98, 0.78)
        pos_hint:{'center_x': 0.5,'center_y': 0.5}
        do_scroll_x: False

        Label:
            text: root.long_text
            height: self.texture_size[1] + dp(10)
            multiline: True
            markup: True                   #Разметка
            size_hint_y: None
            front_size: '14sp'
            color: 0, 0, 0, 1


    Label:
        text:'[ref=some][u][color=FFD700]ЗАПИСАТЬСЯ[/color][/u][/ref]'
        font_size: '12sp'
        size_hint_t: 1, None
        size: 1, '35dp'
        multiline: True
        markup: True
        pos_hint:{'x':.38,'y':.415}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/programs/k/kopiya-tanczevalnaya-studiya-«dance-class».html")


<screen5>:   #интеллектуального развития
    FloatLayout:
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'f4.png'  #фон


        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C9641F')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#C9641F')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
    Label:
        text:'Факультет интеллектуального развития'
        font_size: '17sp'
        size_hint_t: 1, None
        size: 1, '40dp'
        pos_hint:{'x':.0,'y':.465}

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'PinClipart.com_clipartradio-gr_1316563.png'
        pos_hint:{'x':.39,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='up'

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'


    ScrollView:
        size_hint: (0.98, 0.78)
        pos_hint:{'center_x': 0.5,'center_y': 0.5}
        do_scroll_x: False

        Label:
            text: root.long_text
            height: self.texture_size[1] + dp(10)
            multiline: True
            markup: True                   #Разметка
            size_hint_y: None
            front_size: '14sp'
            color: 0, 0, 0, 1


    Label:
        text:'[ref=some][u][color=FFD700]ЗАПИСАТЬСЯ[/color][/u][/ref]'
        font_size: '12sp'
        size_hint_t: 1, None
        size: 1, '35dp'
        multiline: True
        markup: True
        pos_hint:{'x':.38,'y':.415}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/programs/fakultet-intellektualnogo-razvitiya/programma-kompleksnoj-podgotovki-k-shkole.html")


<screen6>:   #спорта
    FloatLayout:
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'pngwing.com (6).png'  #фон


        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#408EB5')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
    Label:
        text:'Факультет спорта'
        font_size: '17sp'
        size_hint_t: 1, None
        size: 1, '40dp'
        pos_hint:{'x':.0,'y':.465}

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'PinClipart.com_clipartradio-gr_1316563.png'
        pos_hint:{'x':.39,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='up'

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'


    ScrollView:
        size_hint: (0.98, 0.78)
        pos_hint:{'center_x': 0.5,'center_y': 0.5}
        do_scroll_x: False

        Label:
            text: root.long_text
            height: self.texture_size[1] + dp(10)
            multiline: True
            markup: True                   #Разметка
            size_hint_y: None
            front_size: '14sp'
            color: 0, 0, 0, 1


    Label:
        text:'[ref=some][u][color=FFD700]ЗАПИСАТЬСЯ[/color][/u][/ref]'
        font_size: '12sp'
        size_hint_t: 1, None
        size: 1, '35dp'
        multiline: True
        markup: True
        pos_hint:{'x':.38,'y':.415}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/programs/fakultet-sporta/sekcziya-rukopashnogo-boya.html")

<screen7>:   #творческого развития
    FloatLayout:
        canvas:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'f5.png'  #фон


        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#106CB8')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#106CB8')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
    Label:
        text:'Факультет творческого развития'
        font_size: '17sp'
        size_hint_t: 1, None
        size: 1, '40dp'
        pos_hint:{'x':.0,'y':.465}

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'PinClipart.com_clipartradio-gr_1316563.png'
        pos_hint:{'x':.39,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='up'

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'


    ScrollView:
        size_hint: (0.98, 0.78)
        pos_hint:{'center_x': 0.5,'center_y': 0.5}
        do_scroll_x: False

        Label:
            text: root.long_text
            height: self.texture_size[1] + dp(10)
            multiline: True
            markup: True                   #Разметка
            size_hint_y: None
            front_size: '14sp'
            color: 0, 0, 0, 1


    Label:
        text:'[ref=some][u][color=FFD700]ЗАПИСАТЬСЯ[/color][/u][/ref]'
        font_size: '12sp'
        size_hint_t: 1, None
        size: 1, '35dp'
        multiline: True
        markup: True
        pos_hint:{'x':.38,'y':.415}
        bold:True
        on_ref_press:
            import webbrowser
            webbrowser.open("https://tmn.deti-talento.ru/programs/fakultet-tvorcheskogo-razvitiya/teatralnaya-studiya.html")



<it>:
    container: container
    FloatLayout:
        canvas.before:
            Rectangle:
                size:self.size
                pos:self.pos
                source:'f6.png'

        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
        FloatLayout:
            pos_hint:{'x':0.210,'y':.010}
            size_hint:.600,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
    Label:
        text:'Дети'
        font_size: '20sp'
        pos_hint:{'x':.0,'y':.445}
        color:
        bold:True
        #italic:True


    BoxLayout:
        #orientation:'horizontal'
        FloatLayout:
            size_hint:.42,.78
            pos_hint:{'x':0,'y':.12}
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                    #rgba:get_color_from_hex('#f98b88')
                    #rgba:get_color_from_hex('#fff5ed')

                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
            Label:
                text:'Фильтр'
                pos_hint:{'x':.18,'y':.85}
                size_hint:.2,.2
                font_size: '15sp'
                bold:True
                color:0,0,0,1
                markup:True
                underline:True
            CheckBox:
                pos_hint:{'x':.07,'y':.665}
                size_hint: .2,.2
                background_checkbox_down:'chk3.png'
                background_checkbox_normal:'unchk.png'
                height:'12dp'
            TextInput:
                pos_hint:{'x':.25,'y':.74}
                size_hint: .73,.06
                background_color:0,0,0,0
                multiline:False
                hint_text:'Имя'
            Label:
                text:'______________'
                pos_hint:{'x':.26,'y':.74}
                color:0,0,0,1
                bold:True
                text_size: self.size
                font_size: '15sp'
            CheckBox:
                pos_hint:{'x':.07,'y':.54}
                size_hint: .2,.2
                background_checkbox_down:'chk3.png'
                background_checkbox_normal:'unchk.png'
            TextInput:
                pos_hint:{'x':.26,'y':.62}
                size_hint: .9,.06
                background_color:0,0,0,0
                multiline:False
                hint_text:'Возраст'
            Label:
                text:'_______________'
                pos_hint:{'x':.26,'y':.62}
                color:0,0,0,1
                bold:True
                text_size: self.size
                font_size: '15sp'
            CheckBox:
                pos_hint:{'x':.07,'y':.42}
                size_hint: .2,.2
                background_checkbox_down:'chk3.png'
                background_checkbox_normal:'unchk.png'

            TextInput:
                pos_hint:{'x':.25,'y':.50}
                size_hint: .9,.06
                background_color:0,0,0,0
                multiline:False
                hint_text:'Телефонный номер'
            Label:
                text:'_______________'
                pos_hint:{'x':.26,'y':.50}
                color:0,0,0,1
                bold:True
                text_size: self.size
                font_size: (root.width**2 + root.height**2) / 14**4

        BoxLayout:
            size_hint:.012,.9
            pos_hint:{'x':.4}
            pos_hint:{'y':.12}

        ScrollView:
            size_hint: (.4, .78)
            pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
                #get_color_from_hex('00640')
            bar_color:
                get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:10
            GridLayout:
                id:container
                cols:1
                height:self.minimum_height
                row_default_height:280
                size_hint_y:None


    ImageButton:
        size_hint:.15,.15
        pos_hint:{'x':.07,'y':.12}
        source:'add.png'
        on_release:
            Factory.custompopup().open()
    ImageButton:
        size_hint:.15,.15
        pos_hint:{'x':.27,'y':.12}
        source:'refresh.png'
        on_release:
            root.add_text_inputs()


    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'delete-icon-ios-19.jpg'
        pos_hint:{'x':.14,'y':.03}
        background_color:0,1,0,.4
        on_release:app.stop()

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'PinClipart.com_clipartradio-gr_1316563.png'
        pos_hint:{'x':.39,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='up'

    ImageButton:
        size_hint_x:.25
        size_hint_y:.05
        source:'free-black-left-arrow-icon-png-vector-241709.png'
        pos_hint:{'x':.64,'y':.03}
        background_color:0,1,0,.4
        on_release:
            root.manager.current='screen'
            root.manager.transition.direction='right'

<custompopup@Popup>:
    title:''
    fnameb:fnameb
    lnameb:lnameb
    mobileb:mobileb
    addressb:addressb
    emailb:emailb
    ageb:ageb
    dobb:dobb
    bmarkb:bmarkb
    genderb:genderb
    size_hint:.8,.8
    separator_height: 0
    background_color:0,0,0,0.4
    border: (1, 1, 1, 1)
    FloatLayout:
        canvas.before:
            Color:
                rgba:get_color_from_hex('#ffffff')
            Rectangle:
                size:self.size
                pos:self.pos
        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#21b68a')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]

        ImageButton:
            source:'student2.png'
            size_hint_y:.35
            size_hint_x:.35
            pos_hint:{'x':.3,'y':.7}

        BoxLayout:
            pos_hint:{'x':.0,'y':.0}
            size_hint:1,.75
            orientation:'horizontal'
            ScrollView:
                bar_width:10
                GridLayout:
                    cols:1
                    height:self.minimum_height
                    row_default_height:60
                    size_hint_y:None
                    Label:
                        text:'Имя'
                        font_size:35
                        pos_hint:{'x':.5,'center_y':1.2}
                        #color:0,0,0,1
                        text_size:self.size
                        underline:True
                        color:get_color_from_hex('#21b68a')
                    Label:
                        text:'Имя'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:fnameb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        font_size:30
                    Label:
                        text:'фамилия'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:lnameb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Label:
                        text:'Контакты'
                        font_size:35
                        pos_hint:{'x':.5,'center_y':1.2}
                        #color:0,0,0,1
                        text_size:self.size
                        underline:True
                        color:get_color_from_hex('#21b68a')
                    Label:
                        text:'Телефонный номер'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:mobileb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Label:
                        text:'Адрес'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:addressb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Label:
                        text:'Почта'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:emailb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0

                    Label:
                        text:'Возраст'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:ageb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Label:
                        text:'Дата рождения'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:dobb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Label:
                        text:'Родинка'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:bmarkb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Label:
                        text:'Пол'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:genderb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                    Button:
                        text:'ДОБАВИТЬ'
                        font_size:"25sp"
                        size_hint:.7,.7
                        on_press:app.add_user(fnameb.text,lnameb.text,mobileb.text,addressb.text,emailb.text,ageb.text,dobb.text,bmarkb.text,genderb.text)
                        background_color:get_color_from_hex('#00a572')
                        on_release:
                            root.dismiss()
                    Label:

<custompopup2@Popup>:
    u1:''
    u2:''
    u3:''
    u4:''
    u5:''
    u6:''
    u7:''
    u8:''
    u9:''
    title:''
    fnameu:fnameu
    lnameu:lnameu
    mobileu:mobileu
    addressb:addressb
    emailb:emailb
    ageb:ageb
    dobb:dobb
    bmarkb:bmarkb
    genderb:genderb
    size_hint:.8,.8
    separator_height: 0
    background_color:0,0,0,0.4
    border: (1, 1, 1, 1)
    FloatLayout:
        canvas.before:
            Color:
                rgba:get_color_from_hex('#ffffff')
            Rectangle:
                size:self.size
                pos:self.pos
        FloatLayout:
            pos_hint:{'x':.0,'y':.9}
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ea3c53')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]

        ImageButton:
            source:'student2.png'
            size_hint_y:.35
            size_hint_x:.35
            pos_hint:{'x':.3,'y':.7}

        BoxLayout:
            pos_hint:{'x':.0,'y':.0}
            size_hint:1,.75
            orientation:'horizontal'
            ScrollView:
                bar_width:10
                GridLayout:
                    cols:1
                    height:self.minimum_height
                    row_default_height:60
                    size_hint_y:None
                    Label:
                        text:'ИМЯ'
                        font_size:35
                        pos_hint:{'x':.5,'center_y':1.2}
                        #color:0,0,0,1
                        text_size:self.size
                        underline:True
                        color:get_color_from_hex('#ea3c53')
                    Label:
                        text:'Имя'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:fnameu
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        font_size:30
                        text:app.u1
                    Label:
                        text:'Фамилия'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:lnameu
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        text:app.u2
                        #background_color:0,0,0,0
                    Label:
                    Label:
                        text:'Контакты'
                        font_size:35
                        pos_hint:{'x':.5,'center_y':1.2}
                        #color:0,0,0,1
                        text_size:self.size
                        underline:True
                        color:get_color_from_hex('#ea3c53')
                    Label:
                        text:'Телефонный номер'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:mobileu
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u3
                    Label:
                        text:'Адрес'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:addressb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u4
                    Label:
                        text:'Почта'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:emailb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u5

                    Label:
                        text:'Возраст'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:ageb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u6
                    Label:
                        text:'Дата рождения'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:dobb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u7
                    Label:
                        text:'Родинка'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:bmarkb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u8
                    Label:
                        text:'Пол'
                        color:0,0,0,1
                        pos_hint:{'x':0,'y':.7}
                        size_hint:.2,.2
                    TextInput:
                        id:genderb
                        multiline:False
                        color:0,0,0,1
                        size_hint:1,.35
                        size:self.size
                        pos_hint:{'x':.05,'y':.68}
                        #background_color:0,0,0,0
                        text:app.u9
                    Button:
                        text:'ОБНОВИТЬ'
                        font_size:"25sp"
                        size_hint:.7,.7
                        on_press:app.update(fnameu.text,lnameu.text,mobileu.text)
                        background_color:get_color_from_hex('#ea3c53')
                        on_release:
                            root.dismiss()
                    Label:


<btn>:
    r1:''
    r2:''
    r3:''
    r4:''
    data:''
    data_id:''
    FloatLayout:

        MDCard:
            focus_behavior:True
            ripple_behavior: True
            #focus_behavior: True
            orientation: "vertical"
            padding: "4dp"
            size_hint: None, None
            size: "163dp", "130dp"
            pos_hint: {"center_x": .5, "center_y": .5}

            MDLabel:
                orientation:'vertical'
                text: root.r2
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]

            MDSeparator:
                height: "1dp"
            MDLabel:
                text: root.r3
            MDLabel:
                text: root.r4
        MDIconButton:
            icon:'account-edit'
            pos_hint:{'x':.75,'y':.6}
            on_press:
                Factory.custompopup2().open()
                #app.root.current='popup2'
        MDIconButton:
            icon:"account-remove"
            pos_hint:{'x':.75,'y':.3}
            on_release:root.delete()

<smooth@Button>:
    background_color:0,0,0,0
    back_color:(0,0,0,0)
    border_radius:[100,]
    canvas.before:
        Color:
            rgba:self.back_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[150,]



"""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class message(Screen):
    pass
class schedule(Screen):
    pass
class news(Screen):
    pass
class payment(Screen):
    pass

class screen2(Screen):
    pass

class online(Screen):
    pass


class screen3(Screen):
    long_text = StringProperty('')
    def __init__(self, **kwargs):
        super(screen3, self).__init__(**kwargs)
        self.long_text = """
        [b][i][size=20][u]         1 ступень "Карапуз-Клаб"[/u][/size][/i][/b]\n
        [b]Комплексная программа развития 
        для малышей[/b]
        [b]Первая ступень развития.[/b]
        [b]Возраст[/b] от 1 до 2 лет. 
        [b]Группы[/b] формируются с учетом
        возрастных особенностей. 
        [b]В группе[/b] 6-8 детей. 
        Занятия проводятся с мамами. 
        Детский центр Talento предлагает
        уникальную программу, которая
        является результатом 10 летней работы 
        лучших специалистов по раннему 
        развитию, педагогов дополнительного
        образования,  семейных психологов.
        В основупрограммы для  малышей 
        вошли лучшие традиции
        отечественной системы дошкольного 
        воспитания, авторские разработки 
        педагогов нашегоцентра и новейшие 
        мировыеобразовательные технологии.
        Программа построена  с учётом 
        возрастных возможностей детей.
        
        Программа направлена на всестороннее 
        развитие ребенка:
        интеллектуальное, эмоциональное, 
        творческое, музыкальное, физическое. 
        
        Каждое занятие имеет 
        сюжетно-ролевое решение,объединяющее
        разнообразные виды деятельности. 
        
        [i][size=17]Содержание программы: [/size][/i]
        
        ---Развитие коммуникативных навыков
        
        ---Развитие внимания, памяти, 
        мышления, речи
        
        ---азвитие мелкой и крупной моторики 
        (пальчиковые и подвижные игры,
           сенсорные дорожки, упражнения на 
           координацию движений и т.д.)
        
        ---Музыкально-эстетическое развитие 
        (слушание музыка, разучивание песен,
        игра на детских музыкальных
        инструментах, танцы)
           
        ---Театрализовано-игровая деятельность 
        (показ мини-кукольных представлений,
         сюжетно-ролевые игры)
        
        ---Изобразительно-прикладная деятельность
           (рисование восковыми мелками, 
           красками, пальчиками, аппликация, 
           работа с пластилином и соленым 
           тестом, а также с природными
            и другими поделочными материалами)
           
        [b][i][size=20][u]         2 ступень "Малышандия"[/u][/size][/i][/b]  
        
        [b]Комплексная программа
         развития для детей 2 – 3 лет.[/b]
        
        Данные занятия ставят своей 
        целью  всестороннее и гармоничное
        развитие ребенка младшего 
        возраста. Занятия проходят в
        увлекательной и игровой форме,
        чередуя различные виды деятельности,
        направленные на   интеллектуальное,
        речевое, эмоциональное,
        эстетическое и физическое  
        развитие малыша, способствуя 
        его социальной адаптации. 
        Эти занятия дают возможность
        деткам побыть в обществе своих 
        сверстников, а маме дает
        свободное время.
        
        Занятия проводятся в возрастных группах 
        по 6-7 человек.
        
        Занятия проводятся без мам.
        
        [b][i][size=20][u]         3 ступень "Я - молодец"[/u][/size][/i][/b] 
        
        [b]Комплексная программа развития 
        для детей 3 – 4 лет.[/b]
        
        Занятия проводятся в игровой форме с 
        учетом индивидуальных особенностей
        каждого ребенка. В процессе занятия 
        развивается речь, наблюдательность, 
        внимание, память,  мышление детей. 
        Совершенствуется грамматический 
        строй языка: согласование 
        прилагательных с существительными, 
        образование форм глагола.
        
        [b]Целями программы является:[/b]
        
        ---появление интереса к окружающему 
        их миру,
        
        ---расширение словарного запаса,
        
        ---расширение кругозора,
        
        ---умение вступать в контакт со 
        сверстниками и взрослыми людьми,
        
        ---развитие мелкой и общей моторики.
        
        [b][i][size=20][u]         Детский сад неполного дня"[/u][/size][/i][/b]
        
        [b]Комплексная программа развития 
        и воспитания дошкольников (от 2 до 6 лет).[/b]
        
        Группа неполного дня — Евросадик 
        существуетв нашей Академии 
        Талантов уже более 13 лет.
        За это время мы выпустили
        13 групп детей, которые 
        полноценно подготовились к школе,
        а первый выпуск уже закончил школу! 
        
        В нашем центре занимаются три 
        возрастные группы:
        
        ---2 - 3 года
        
        ---3 - 5 лет
        
        ---5 - 6 лет
        """

    def update(self, dt):
        pass

class screen4(Screen):
    long_text = StringProperty('')

    def __init__(self, **kwargs):
        super(screen4, self).__init__(**kwargs)
        self.long_text ="""
        [b][i][size=20][u]        Брейк-данс[/u][/size][/i][/b]\n
        Брейк появился в Нью-Йорке 
        в конце 70-х годов 
        XX века,вобрав в себя 
        множество различных форм 
        от фольклорной хореографии,
        до элементов из спортивной
        гимнастики,единоборств, капоэйры. 
        Однако в ходе развития породил
        абсолютно оригинальные 
        хореографические элементы,
        что сделало его узнаваемым и 
        чрезвычайно популярным во всем мире. 
        
        Занятия способствуют укреплению и 
        тренировке нервной и дыхательной 
        систем, поддержке мышечного тонуса, 
        развития чувства ритма, музыкального 
        слуха,физических способностей, 
        творческойиндивидуальности, харизмы. 
        
        Педагог индивидуально, с каждым 
        ребёнком, поэтапно разбирает
        сновные принципы отработки техники 
        исполнения отдельных танцевальных
         движений, фигур и полной 
         композиции танца. 
        
        [b]Цели:[/b] 
        
        ---Тренировка и улучшение результатов
         по выполнению брейк - элементов 
         и силовых трюков;
        
        ---Логическое завершение движения 
        и переход на новое;
        
        ---Изучение акробатических элементов.
        
        [b][i][size=20][u]        Хореография с 3 лет[/u][/size][/i][/b]\n
        
        Занятия способствуют выработке 
        правильной осанки,пластики, 
        координации движений, развивают 
        чувство ритма и музыкальный слух 
        и просто радуют детей. На занятиях 
        дети получают 
        музыкально-хореографическое
        развитие, пробуют себя  
        в танце и в музыке.
        
        Программа  рассчитана  на  детей 3 - 7 лет, 
        Занятия проводятся в группах, 
        по возрастам, 8 человек в группе.
        
        [b]Задачи программы:[/b]
        
        ---Воспитывать чувство ритма.
        
        ---Формировать художественный вкус.
        
        ---Развивать музыкальные и
         творческие способности и мышление.
        
        ---Укреплять здоровье, улучшать 
        общее физическое развитие ребенка.
        
        --- Формировать положительный 
        эмоциональный тонус.
        
        [b]В программе:[/b] 
        
        ---Классическая хореография. 
        
        ---Современная хореография. 
        
        ---Расслабляющая гимнастика, 
        детский фитнес на фитбольных мячах.
        
        [b][i][size=20][u]        Современные танцы[/u][/size][/i][/b]\n
        
        Современная школа танцев 
        для детей в Тюмени- 
        современные методики 
        преподавания, современная 
        музыка,интересное увлечение 
        для современных детей!
        
        Занятия проводятся в возрастных
        группах по 8 человек.
        
        Современный танец развивает гибкость,
        чувство ритма, несет хорошую
        физическую нагрузку
        
        R-n-B, Hip-hop, Free-style и 
        многие другие стили - то, 
        что нужно знать, тобы модно 
        и современно танцевать,
        как: Justin Timberlake,
        he Black Eyed Peas, Akon, Mario Winnans,
        Тимати, Дима Билан и другие яркие звезды. 
        """


    def update(self, dt):
        pass


class screen5(Screen):
    long_text = StringProperty('')

    def __init__(self, **kwargs):
        super(screen5, self).__init__(**kwargs)
        self.long_text ='''
        [b][i][size=20sp][u] Программа комплексной 
                 подготовки к школе[/u][/size][/i][/b]\n
        
        Программа предназначена для 
        детей от 4-х лет
        (группы делятся по возрасту)
        Программа подготовки к школе 
        по предметам:  математика, 
        развитие речи, обучение грамоте.
        
        [b][i][size=20][u]   Наррy English - 
                  английский для детей[/u][/size][/i][/b]\n
        
        [b]Английский язык для детей[/b]
        [b]Три ступени:[/b]
        1 ступень  — для детей от 4 до 7 лет.
        2 ступень  — от 7 до 8 лет.
        3 ступень — от 8 лет.
        I ступень — Курс английского для дошколят.
        
        Программа рассчитана на дошкольников 
        в возрасте 4 - 7  лет.
        Все занятия проводятся в 
        мини-группах по 6 детей.
        
        [b][i][size=20sp][u]          Каллиграфия[/u][/size][/i][/b]\n
        
        Каллиграфически правильное письмо 
        способствует эстетическому, 
        эмоциональному воспитанию школьников,
        воспитанию аккуратности, 
        сосредоточенности старательному 
        отношению квыполнению любой работы.
        
       [b]Задачи курса каллиграфии в Таленто:[/b]
       
       ---Укрепление мышц кисти рук и пальцев.
       
       ---Ознакомление с гигиеническими 
       требованиями предъявляемыми к письм
       
       ---Правильная посадка и 
       владение инструментами,
       
       [b][i][size=20][u]        Продленка[/u][/size][/i][/b]\n
       
       [b]Группа продлённого дня для 
       учащихся младших классов.[/b]
       
       [b]Продлёнка для начальных
        классов 1 смены.[/b]
       
       Программа дневного пребывания школьников. 
       
       Группы формируются с учетом возрастных 
       особенностей, наполняемость 8-12 детей.
       
       [b]Цель:[/b] создание условий для развития
       функционально грамотной
       личности-человека, способного
       решать любыежизненные задачи, 
       максимального раскрытия
       ндивидуального возрастного 
       потенциала ребенка.
       
       [b][i][size=20][u]          Скорочтение[/u][/size][/i][/b]\n
       
       [b]Уникальная программа развития внимания, 
       памяти и управления[/b]
       [b]информацией по методике Talento, 
       которую еще называют #Мозгоспорт[/b]
       
       Как научить ребёнка быстро
       читать, при этом усваивая 
       необходимый объём информации?
       Как повысить внимание ребенка? 
       как помочь ребенку стать успешным
       в учебе и в дальнейшей профессиональной 
       деятельности?
       
       Одним из самых популярных на 
       сегодняшний день  способов решения
       той проблемы, является обучение 
       школьника скорочтению.
       
       Самостоятельное осознанное чтение в 
       хорошем темпе, а также полное 
       усвоение прочитанной информации – 
       один из основных навыков, 
       необходимых для успешной учебы в школе
       и дальнейшей профессиональной 
       деятельности в наш век,
        где правит информация. 
       
       
       [b][i][size=20][u]          Шахматная школа[/u][/size][/i][/b]\n
       
       Шахматная школа в Таленто  
       – отличная возможность
       интеллектуального и психологического
       развития ваших детей, а также 
       подготовки их к школьному обучению.
       Не секрет, что наибольшие трудности 
       в начальной школе испытывают не
       те дети, которые имеют недостаточный
       объем знаний и навыков а те,
       которые проявляют интеллектуальную 
       пассивность, которых отсутствует 
       желание и привычка думать, решать задачи.
       
       Наиболее оптимальный возраст для начала
       обучения шахматам – 4-6 лет.
       
       Обучение шахматам - это целостный курс,
       направленный на   формирование 
       гармоничной, творчески активной
       личности ребенка.
        '''

    def update(self, dt):
        pass


class screen6(Screen):
    long_text = StringProperty('')

    def __init__(self, **kwargs):
        super(screen6, self).__init__(**kwargs)
        self.long_text ='''
        [b][i][size=20][u]          Секция рукопашного боя[/u][/size][/i][/b]\n
        
        Для детей 4-12 лет, групповые тренировки, 
        8 человек в группе.
        
        Группы комплектуются с учетом 
        возраста детей.
        
        Рукопашный бой – универсальный вид 
        прикладной подготовки, впитавший 
        в себя самое лучшее из разных видов 
        единоборств.В основе программы 
        – принцип позволения или
        использования силы соперника 
        против него самого.
        
        Это единоборство позволяет стать 
        более уравновешенным, благотворно 
        влияет на психическое развитие.
        
        Рукопашный бой — неотъемлемая часть 
        общефизическойподготовки военных,
         работников полиции, поэтому те, кто
        хочет избрать себе такую профессию
        в будущем, могут готовиться уже в 
        юном возрасте.
        
        [b]Задачи занятий:[/b]
        
        ---овладение и совершенствование
         техники рукопашного боя; 
        
        ---воспитание смелости, воли, 
        решительности и других качеств; 
        
        ---укрепление здоровья, повышение 
        иммунитета;
        
        ---обучение общению и конфликтологии;
        
        ---повышение уровня общей физической
            подготовки и навыков самообороны;
        
        ---укрепление психологической устойчивости
            и уверенности в себе;
        
        ---развить умение не сдерживать силу,
         пропускать ее через себя, переводить 
         в нужное русло.
         
         Индивидуально для каждого ребенка подбирается
         нагрузка и специальные физические упражнения.

        '''

    def update(self, dt):
        pass


class screen7(Screen):
    long_text = StringProperty('')

    def __init__(self, **kwargs):
        super(screen7, self).__init__(**kwargs)
        self.long_text ='''
        [b][i][size=20][u]          Театральная студия[/u][/size][/i][/b]\n
        
        Приобщение детей к театрализованной
        деятельности способствует своению 
        ребенком мира человеческих чувств, 
        коммуникативных навыков, развитию 
        способности к сопереживанию,
        развивает умение четко, правильно и 
        выразительно говорить, уверенно 
        чувствовать себя на публике,
        управлять своим телом и голосом.
        
        [b]Цель программы:[/b] 
        
        ---научиться управлять своими 
        эмоциями и телом.
        
        ---выражать эмоции через творчество.
        
        ---научиться громко и чётко говорить.
        
        ---приобрести навыки общения.
        
        ---стать увереннее в себе.
        
        ---развить творческие способности.
        
        ---развить память и пополнить 
        словарный запас.
        
        На занятиях Ваш ребенок найдет новые
        сказочные сюжеты для игр и, конечно, 
        новых друзей.
        
        [b]В программу обучения входит:[/b]
        
        ---актерское мастерство.
        
        ---сценическое движение, пластика. 
        
        ---артикуляционная и дыхательная 
        гимнастика. 
        
        ---ритмические, музыкальные игры 
        и упражнения. 
        
        ---искусство создания костюма и грима.
        
        [b][i][size=20][u]          Студия ИЗО[/u][/size][/i][/b]\n
        
        Занятия помогают раскрывать и 
        развивать творческие способности,
        заложенные в ребенке. Вопросы
        гармоничного развития
        и творческой самореализации находят 
        свое разрешение
        в условиях изостудии. 
        [b]Открытие в себе неповторимой
        индивидуальности поможет ребенку 
        реализовать себя  в учебе, творчестве,
         в общении с другими людьми.[/b]
        
        По окончании курса ребенок будет
        
        ЗНАТЬ:
        
        ---Особенности материалов, применяемых
            в художественной деятельности;
        
        ---Разнообразие выразительных средств:
            цвет, свет линия, объем, композиция, ритм.   
            
        УМЕТЬ:
        
        ---Пользоваться гуашью, акварелью, 
        белой и цветной бумагой;
        
        ---Различать и передавать в рисунке
         ближние и дальние предметы;
        
        ---Рисовать кистью элементы 
        растительного и животного мира;
        
        ---Выполнять орнамент в круге, овале, ленте;
        
        ---Использовать теплую и холодную
         гамму цветов;
        
        ---Сознательно выбирать средства 
        выражения своего замысла.
            
        '''

    def update(self, dt):
        pass


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "Login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Имя учетной записи: " + name
        self.email.text = "Почта: " + self.current
        self.created.text = "Дата созданный: " + created



class screen10(Screen):
    pass




class student(Screen):
    pass


class btn(Screen):
    def __init__(self, **kwargs):
        super(btn, self).__init__(**kwargs)

    def delete(self):
        con = sql.connect('students_detail.db')
        cur = con.cursor()
        cur.execute('delete from studenti where ID=' + self.data_id)
        con.commit()
        con.close()


class it(Screen, MDApp):

    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(it, self).__init__(**kwargs)
        Clock.schedule_once(self.setup_scrollview, 1)

    def setup_scrollview(self,dt):
        self.container.bind(minimum_height=self.container.setter('height'))
        self.add_text_inputs()

    def add_text_inputs(self):
        self.container.clear_widgets()
        con = sql.connect('students_detail.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM studenti""")
        row = cur.fetchall()
        for i in row:
            wid = btn()
            wid2 = MyMainApp()
            r1 = str(i[0]) + '\n'
            r2 = i[1] + ' ' + i[2] + '\n'
            r3 = str(i[3]) + '\n'
            r4 = str(i[4])

            u1 = i[1]
            u2 = i[2]
            u3 = str(i[3])
            u4 = i[4]
            u5 = i[5]
            u6 = str(i[6])
            u7 = i[7]
            u8 = i[8]
            u9 = i[9]



            wid.data_id = str(i[0])
            wid2.data_id = str(i[0])
            wid.data = r1 + r2 + r3 + r4
            wid2.data = r1, r2, r3, r4

            wid.r1 = r1
            wid.r2 = r2
            wid.r3 = r3
            wid.r4 = r4

            wid2.u1 = u1
            wid2.u2 = u2
            wid2.u3 = u3
            wid2.u4 = u4
            wid2.u5 = u5
            wid2.u6 = u6
            wid2.u7 = u7
            wid2.u8 = u8
            wid2.u9 = u9


            self.container.add_widget(wid)





class ImageButton(ButtonBehavior, Image):
    pass



class popup2(Screen):
    pass

def invalidLogin():

    pop = Popup(title='Неверный логин',
                  content=Label(text='Неверное имя пользователя или пароль.'),
                  size_hint=(None, None), opacity=0.8, size=(400, 400))
    pop.open()


def invalidForm():

    pop = Popup(title='Недействительная форма',
                  content=Label(text='Пожалуйста, заполните все входные данные\nдостоверной информацией.'),
                  size_hint=(None, None),opacity=0.8, size=(400, 400))

    pop.open()


db = DataBase("users.txt")
sm = ScreenManager()




class MyMainApp(MDApp, App):
    fnameu = StringProperty()
    lnameu = StringProperty()
    mobileu = StringProperty()

    def update(self, fnameu, lnameu, mobileu):
        con = sql.connect('students_detail.db')
        cur = con.cursor()
        a1 = (fnameu, lnameu, mobileu)
        s1 = 'update studenti SET'
        s2 = 'fname="%s",lname="%s",mobile="%s" ' % a1
        s3 = ('where ID=' + self.data_id)
        cur.execute(s1 + ' ' + s2 + ' ' + s3)
        con.commit()
        con.close()

    fnameb = StringProperty()
    lnameb = StringProperty()
    mobileb = StringProperty()
    addressb = StringProperty()
    emailb = StringProperty()
    ageb = StringProperty()
    dobb = StringProperty()
    bmarkb = StringProperty()
    genderb = StringProperty()



    def add_user(self, fnameb, lnameb, mobileb, addressb, emailb, ageb, dobb, bmarkb, genderb):
        con = sql.connect('students_detail.db')
        cur = con.cursor()
        cur.execute(""" INSERT INTO studenti(fname,lname,mobile,address,email,age,dob,bmark,gender
        ) VALUES (?,?,?,?,?,?,?,?,?)""", (fnameb, lnameb, mobileb, addressb, emailb, ageb,
                                                                  dobb, bmarkb, genderb))
        con.commit()
        con.close()



    def build(self):
        Builder.load_string(kv_string)
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(screen2(name='screen'))
        sm.add_widget(screen3(name='screen3'))
        sm.add_widget(screen4(name='screen4'))
        sm.add_widget(screen5(name='screen5'))
        sm.add_widget(screen6(name='screen6'))
        sm.add_widget(screen7(name='screen7'))
        sm.add_widget(CreateAccountWindow(name='create'))
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(screen10(name='screen10'))
        sm.add_widget(student(name='student'))
        sm.add_widget(news(name='news'))
        sm.add_widget(message(name='message'))
        sm.add_widget(online(name='online'))
        sm.add_widget(schedule(name='schedule'))
        sm.add_widget(payment(name='payment'))
        sm.add_widget(it(name='it'))
        sm.add_widget(btn(name="btn"))
        sm.add_widget(popup2(name='popup2'))



        return sm



if __name__ == '__main__':
    MyMainApp().run()
