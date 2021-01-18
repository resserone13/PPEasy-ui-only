
import time 
import ui
from ppeasytext import info

#--- to do ---
#make intro, main, mask, gowns and wipes page full screen. 
#make links page scroll
#add suffix to urls so that the link goes to a certian page of the website. 
#mask are not showing on mask menu
#center titles and pictures


bg_clr = 'CAF0F8'

app_title = 'PPEasy'
app_title_fnt = 'Didot'
app_txt_sz =25

txt_fnt = 'Didot'
txt_sz = 20
txt_clr = '1D3557'

btn_fnt = 'Didot'
btn_txt_sz = 20
btn_clr= 'black'
btn_border_clr = '0077B6'
btn_clr = 'CAF0F8'
btn_shadow=('gray', 0, 7, 2)
btn_corner_radius = 10

level_1_img = 'Level1Mask.PNG'
level_3_img = 'Level3Mask.PNG'
kn95_img = 'Kn95Mask.PNG'
N95_img = 'N95Mask.PNG'
papr_img = 'PaprMask.PNG'
face_shield_img = 'FaceShield.JPG'
oxi_img = 'OxivirWipes.PNG'
sani_img = 'SaniWipes.PNG'
bleach_img = 'BleachWipes.PNG'
ammonia_img = 'AmmoniaWipes.PNG'
cloth_gown_img = 'ClothGown.PNG'
plastic_gown_img = 'PlasticGown.PNG'

intro_mes = 'Thanks for being safe'

width, height = ui.get_window_size()

class Main_View(ui.View):
    def __init__(self):
        self.background_color=bg_clr
    
    def add_title(self, l_txt):   
        t= ui.Label()
        t.font= txt_fnt, 25
        t.text = l_txt
        t.alignment= ui.ALIGN_CENTER
        t.frame=width/4, height * 0.04, width * 0.50, height * 0.05
        self.add_subview(t)
    
    def custom_label(self, l_txt, size, x, y , w, h):
        t= ui.Label()
        t.font= txt_fnt, size
        t.text = l_txt
        t.alignment= ui.ALIGN_CENTER
        t.frame=width * x, height * y, width * w, height * h
        self.add_subview(t)
        
    def add_img(self, image, x, y, w, h):
        img = ui.ImageView()
        img.image = ui.Image.named(image)
        img.frame=(width * x, height * y, w, h)
        img.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
        self.add_subview(img)

    def add_btn(self, btn_names, actions_list,):
        for i, (n, a) in enumerate(zip(btn_names, actions_list)):
            btn= ui.Button()
            btn.background_color=btn_clr
            btn.title=n
            btn.font=(btn_fnt, btn_txt_sz)
            btn.tint_color=txt_clr
            btn.border_width=2
            btn.border_color=txt_clr
            btn.frame=(width * 0.15, height * (0.10 + i * 0.1), width * 0.7, height * 0.07)
            btn.corner_radius= btn_corner_radius
            btn.action=a
            self.add_subview(btn)
            
    def add_textview(self, txt, x, y, w, h):
        tv = ui.TextView()
        tv.editable=False
        tv.scroll_enabled=True
        tv.background_color=bg_clr
        tv.alignment= ui.ALIGN_LEFT
        tv.number_of_lines= 0
        tv.line_break_mode = ui.LB_CHAR_WRAP
        tv.font= app_title_fnt, 17
        tv.frame= (x, y, w, h)
        tv.text = txt
        self.add_subview(tv)
            
def open_url(sender):
     wv = ui.WebView()
     wv.load_url(f'https://{sender.title}')
     wv.frame = sender.superview.frame
     wv.present('sheet', hide_title_bar=True)
     wv.wait_modal()

def mask_pg(sender):
    mask_btns = ['Level 1', 'Level 3', 'Kn95', 'N95', 'Papr']
    v = Main_View()
    v.add_title('Masks')

    v.add_img(level_1_img, width * 0.15, height * 0.20, 150, 150)
    v.add_img(level_3_img, width * 0.45, height * 0.20, 150, 150)
    v.add_img(kn95_img, width * 0.05, height * 0.2, 150, 150)
    v.add_img(N95_img, width * 0.15, height * 0.1, 150, 150)
    v.add_img(papr_img, width * 0.15, height * 0.50, 150, 150)
    v.add_btn(mask_btns, mask_actions)
    v.present('full_screen', hide_title_bar=True)

def lvl_1_pg(sender):
    v = Main_View()
    v.add_title('Level 1')
    v.add_img(level_1_img, 0.15, 0.12, 300, 300)
    v.add_textview(info[1], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present('full_screen', hide_title_bar=True)
  
def lvl_3_pg(sender):
    v = Main_View()
    v.add_title('Level 3')
    v.add_img(level_3_img, 0.05, 0.12, 375, 375)
    v.add_textview(info[2], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present('full_screen', hide_title_bar=True)
    
def kn95_pg(sender):
    v = Main_View()
    v.add_title('Kn95')
    v.add_img(kn95_img, 0.15, 0.12, 300, 300)
    v.add_textview(info[3], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present('full_screen', hide_title_bar=True)

def n95_pg(sender):
    v = Main_View()
    v.add_title('N95')
    v.add_img(N95_img, 0.15, 0.12, 300, 300)
    v.add_textview(info[4], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present('full_screen', hide_title_bar=True)

def papr_pg(sender):
    v = Main_View()
    v.add_title('Papr')
    v.add_img(papr_img, 0.15, 0.12, 300, 300)
    v.add_textview(info[5], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present('full_screen', hide_title_bar=True)

def face_shield_pg(sender):
    v = Main_View()
    v.add_title('Face Shield')
    v.add_img(face_shield_img, 0.15, 0.12, 300, 300)
    v.add_textview(info[0], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)

def gowns_pg(sender):
    gowns_btns = ['Cloth', 'Plastic']
    v = Main_View()
    v.add_title('Gowns')
    v.add_img(cloth_gown_img, -0.02, 0.32, 280, 280)
    v.add_img(plastic_gown_img, 0.30, 0.57, 280, 280) 
    v.add_btn(gowns_btns, gown_actions)
    v.present('full_screen', hide_title_bar=True)

def cloth_pg(sender):
    v = Main_View()
    v.add_title('Cloth')
    v.add_img(cloth_gown_img, 0.12, 0.12, 300, 300) 
    v.add_textview(info[6], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)
   
def plastic_pg(sender):
    v = Main_View()
    v.add_title('Plastic')
    v.add_img(plastic_gown_img, 0.12, 0.12, 300, 300) 
    v.add_textview(info[7], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)
    
def wipes_pg(sender):
    wipes_btns = ['Oxivir', 'Sani', 'Bleach', 'Ammonia']
    v = Main_View()
    v.add_title('Wipes')
    v.add_btn(wipes_btns, wipes_actions)
    v.add_img(oxi_img,  0.10, 0.50, 150, 150)
    v.add_img(sani_img, 0.55, 0.50, 150, 150)
    v.add_img(bleach_img, 0.10, 0.70, 150, 150)
    v.add_img(ammonia_img, 0.55, 0.70, 150, 150)
    v.present('full_screen', hide_title_bar=True)

def oxi_pg(sender):
    v = Main_View()
    v.add_title('Oxivir')
    v.add_img(oxi_img, 0.15, 0.12, 300, 300) 
    v.add_textview(info[11], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)
    
def sani_pg(sender):
    v = Main_View()
    v.add_title('sani')
    v.add_img(sani_img, 0.15, 0.12, 300, 300) 
    v.add_textview(info[12], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)
    
def bleach_pg(sender):
    v = Main_View()
    v.add_title('Bleach')
    v.add_img(bleach_img, 0.15, 0.12, 300, 300) 
    v.add_textview(info[13], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)
    
def ammonia_pg(sender):
    v = Main_View()
    v.add_title('Ammonia')
    v.add_img(ammonia_img, 0.15, 0.12, 300, 300) 
    v.add_textview(info[14], width * 0.12, height * 0.50, width * 0.75, height * 0.60)
    v.present(hide_title_bar=True)
    
def faq_pg(sender):
    v = Main_View()
    v.add_title('FAQ')
    v.add_textview(info[8], width * 0.10, height * 0.08, width *0.87, height * 0.85)
    v.present(hide_title_bar=True)

def dd_pg(sender):
    v = Main_View()
    v.add_title("Dos / Don'ts'")
    v.add_textview(info[9], width * 0.07, height * 0.08, width *0.87, height * 0.85)
    v.present(hide_title_bar=True)

def covid_pg(sender):
    v = Main_View()
    v.add_title('Covid')
    v.add_textview(info[10] , width * 0.07, height * 0.08, width *0.87, height * 0.85)
    v.present(hide_title_bar=True)

def links_pg(sender):
    v = Main_View()
    v.add_title('Links')
    v.add_btn(info[15], links_actions)
    v.present('full_screen', hide_title_bar=True)

main_pg_actions = [mask_pg, face_shield_pg, gowns_pg, wipes_pg, faq_pg, dd_pg, covid_pg, links_pg]   
            
mask_actions = [lvl_1_pg, lvl_3_pg, kn95_pg, n95_pg, papr_pg]

gown_actions = [cloth_pg, plastic_pg]  

wipes_actions = [oxi_pg, sani_pg, bleach_pg, ammonia_pg]

links_actions = [open_url, open_url, open_url, open_url, open_url, open_url, open_url]
        
intro = Main_View()
intro.custom_label(app_title, 30, 0.1, 0.3, 0.75, 0.2)
intro.custom_label(intro_mes, 15, 0.1, 0.35, 0.75, 0.2)
intro.present(hide_title_bar=True)

time.sleep(2)

intro.close()
time.sleep(0.5)

main_menu = Main_View()
main_menu.add_title('PPEasy')
main_menu.add_btn(info[16], main_pg_actions)
main_menu.present('full_screen', hide_title_bar=True)
