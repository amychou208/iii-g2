#coding: utf-8
from django import forms
from web import models
from .models import Registration 
from .models import Choose

class UploadForm(forms.Form):
    file = forms.ImageField()


class RegistrationForm(forms.ModelForm):
#	BIRTH_YEAR_CHOICES = ('1950', '1951', '1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963', '1964','1965', '1966', '1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978', '1979','1980','1981', '1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',)
#	birthday = forms.DateField(widget=SelectDateWidget (years=BIRTH_YEAR_CHOICES))
	class Meta:	
		model = Registration
		fields =['matchgender','account_name','gender','star','height','eye','hair','figure','race','sport','sport_habbit','smoke','drink','interest','faith','job','income','language','education','political','relationship','wantchild','children',]
		widgets = {
                        'income': forms.Select(
                                choices=[
                                        ("$35,001至$50,000","$35,001至$50,000"),
                                        ("無答案","無答案"),
                                        ("$25,000以下","$25,000以下"),
                                        ("$25,001至$35,000","25,001至35,000"),
                                        ("$50,001至$75,000","$50,001至$75,000"),
                                        ("$75,001至$100,000","75,001至100,000"),
                                        ("$100,001至$150,000","$100,001至$150,000"),
                                        ("$150,001以上","$150,001以上"),
                                ]),
		        'faith': forms.Select(
                                choices=[
                                        ("基督教/天主教","基督教/天主教"),
                                        ("無答案","無答案"),
                                        ("不可知神論","不可知神論"),
                                        ("無神論","無神論"),
                                        ("佛教/道教","佛教/道教"),
                                        ("基督教/摩門教","基督教/摩門教"),
                                        ("基督教/新教","基督教/新教"),
                                        ("印度教","印度教"),
                                        ("猶太教","猶太教"),
                                        ("穆斯林/依斯蘭","穆斯林/依斯蘭"),
                                        ("信仰精神與靈魂，但不信教","信仰精神與靈魂，但不信教"),
                                        ("其他","其他"),
				]),
			'language': forms.Select(
                                choices=[
                                        ("中文","中文"),
                                        ("無答案","無答案"),
                                        ("英語","英語"),
                                        ("阿拉伯語","阿拉伯語"),
                                        ("荷蘭語","荷蘭語"),
                                        ("法語","法語"),
                                        ("德語","德語"),
                                        ("希伯來語","希伯來語"),
                                        ("印度語","印度語"),
                                        ("義大利語","義大利語"),
                                        ("日語","日語"),
                                        ("韓語","韓語"),
                                        ("挪威語","挪威語"),
                                        ("葡萄牙語","葡萄牙語"),
                                        ("俄語","俄語"),
                                        ("西班牙語","西班牙語"),
                                        ("瑞典語","瑞典語"),
                                        ("其他","其他"),
				]),
                        'job': forms.Select(
                                choices=[
					("銷售/市場","銷售/市場"),
					("無答案","無答案"),
					("行政/秘書","行政/秘書"),
					("藝術/創意/表演","藝術/創意/表演"),
					("執行/管理","執行/管理"),
					("金融服務","金融服務"),
					("勞務/建築","勞務/建築"),
					("法律","法律"),
					("醫療/牙醫/獸醫","醫療/牙醫/獸醫"),
					("政治/政府/民政服務/軍隊","政治/政府/民政服務/軍隊"),
					("零售/食品服務","零售/食品服務"),
					("退休","退休"),
					("自僱人士","自僱人士"),
					("學生","學生"),
					("教師/教授","教師/教授"),
					("技術/計算機/工程","技術/計算機/工程"),
					("旅遊/酒店/運輸","旅遊/酒店/運輸"),
					("時尚/模特/美容","時尚/模特/美容"),
					("建築/室內設計","建築/室內設計"),
					("執法/安全/軍事","執法/安全/軍事"),
					("非營利/義工/活動家","非營利/義工/活動家"),
					("其他職業","其他職業"),
				]),	
                        'drink': forms.Select(
                                choices=[
                                        ("出於社交可以喝一兩杯","出於社交可以喝一兩杯"),
                                        ("無答案","無答案"),
                                        ("從不","從不"),
                                        ("只喝非酒精飲料","只喝非酒精飲料"),
                                        ("經常","經常"),
					("適度","適度"),
				]),
                        'smoke': forms.Select(
                                choices=[
                                        ("偶爾","偶爾"),
                                        ("無答案","無答案"),
                                        ("從不","從不"),
                                        ("每天","每天"),
                                        ("雪茄愛好者","雪茄愛好者"),
					("嘗試戒菸中","嘗試戒菸中"),
                                ]),
                        'sport_habbit': forms.Select(
                                choices=[
                                        ("每週1~2次","每週1~2次"),
                                        ("無答案","無答案"),
                                        ("從不","從不"),
                                        ("每週3~4次","每週3~4次"),
                                        ("每週5次以上","每週5次以上"),
				]),
			'education': forms.Select(
                                choices=[
                                        ("大專","大專"),
                                        ("無答案","無答案"),
                                        ("高中以下","高中以下"),
                                        ("高中","高中"),
                                        ("學士","學士"),
                                        ("碩士","碩士"),
					("博士/以上","博士/以上"),
				]),
                        'political': forms.Select(
                                choices=[
                                        ("中立","中立"),
                                        ("無答案","無答案"),
                                        ("不墨守成規","不墨守成規"),
                                        ("極端保守","極端保守"),
                                        ("其他觀點","其他觀點"),
                                        ("保守","保守"),
                                        ("非常自由","非常自由"),
				]),
                        'relationship': forms.Select(
                                choices=[
                                        ("從未結婚","從未結婚"),
                                        ("無答案","無答案"),
                                        ("目前分居","目前分居"),
                                        ("離異","離異"),
                                        ("喪偶","喪偶"),
                                ]),
			'figure': forms.Select(
                                choices=[
                                        ("苗條","苗條"),
                                        ("無答案","無答案"),
                                        ("高大健美","高大健美"),
                                        ("曲線曼妙","曲線曼妙"),
                                        ("普通","普通"),
                                        ("運動健美","運動健美"),
                                        ("豐滿","豐滿"),
                                        ("魁偉","魁偉"),
                                        ("微胖","微胖"),
                                        ("敦實","敦實"),
				]),
                        'children': forms.Select(
                                choices=[
                                        ("沒有","沒有"),
                                        ("無答案","無答案"),
                                        ("是的，他們有時住在家裡","是的，他們有時住在家裡"),
                                        ("是的，他們不住在家裡","是的，他們不住在家裡"),
                                        ("是的，他們住在家裡","是的，他們住在家裡"),
				]),
			'eye': forms.Select(
                                choices=[
					("棕色","棕色"),
					("無答案","無答案"),
					("黑色","黑色"),
                                        ("金色","金色"),
                                        ("藍色","藍色"),
                                        ("綠色","綠色"),
					("淡褐色","淡褐色"),
				]),
                        'wantchild': forms.Select(
                                choices=[
                                        ("日後可能吧","日後可能吧"),
                                        ("無答案","無答案"),
                                        ("肯定要","肯定要"),
                                        ("不確定","不確定"),
                                        ("很可能不要","很可能不要"),
                                        ("不想要孩子","不想要孩子"),
 				]),
			'hair': forms.Select(
                                choices=[
					("無答案","無答案"),
					("黑色","黑色"),
					("金色","金色"),
					("淺棕色","淺棕色"),
					("深棕色","深棕色"),
					("紅褐色/紅色","紅褐色/紅色"),
					("灰色","灰色"),
					("白色","白色"),
					("光頭","光頭"),
				]),
                        'matchgender': forms.Select(
                                choices=[
                                        # 前面是值後面是顯示
                                        ('男性', '男性'),
                                        ('女性', '女性'),
                                ]),
			'gender': forms.Select(
				choices=[
					# 前面是值後面是顯示	
					('女性', '女性'),
					('男性', '男性'),
				]),
			'star': forms.Select(
				choices=[
					("白羊座","白羊座"),
                			("不顯示我的星座","不顯示我的星座"),
                			("摩羯座","摩羯座"),
                			("水瓶座","水瓶座"),
                			("雙魚座","雙魚座"),
            				("金牛座","金牛座"),
                			("雙子座","雙子座"),
                			("巨蟹座","巨蟹座"),
                			("獅子座","獅子座"),
                			("處女座","處女座"),
                			("天秤座","天秤座"),
                			("天蠍座","天蠍座"),
                			("射手座","射手座"),
                			("我不相信星座","我不相信星座"),
				]),
			   
			'race': forms.CheckboxSelectMultiple(
				choices=[
					('亞洲人', '亞洲人'),
	                                ('拉丁/西班牙人', '拉丁/西班牙人'),
         	                        ('太平洋島人 ', '太平洋島人 '),
                                        ('黑人/非洲裔', '黑人/非洲裔'),
                                        ('中東人', '中東人'),
                                        ('白人/高加索人', '白人/高加索人'),
                                        ('東印度人', '東印度人'),
                                        ('美洲印第安人', '美洲印第安人'),	
                                        ('其他', '其他'),
				]),
			 'interest': forms.CheckboxSelectMultiple(
                                    choices=[
					('校友聯誼','校友聯誼'),
                                        ('外出就餐','外出就餐'),
                                        ('音樂與音樂會','音樂與音樂會'),
                                        ('宗教/精神','宗教/精神'),
                                        ('品酒','品酒'),
                                        ('讀書俱樂部/討論','讀書俱樂部/討論'),
                                        ('釣魚/打獵','釣魚/打獵'),
                                        ('夜總會/跳舞','夜總會/跳舞'),
                                        ('購物/古董','購物/古董'),
                                        ('露營','露營'),
                                        ('園藝/景觀','園藝/景觀'),
                                        ('表演藝術','表演藝術'),
                                        ('旅遊/觀光','旅遊/觀光'),
                                        ('喝咖啡聊天','喝咖啡聊天'),
                                        ('愛好與手工藝','愛好與手工藝'),
                                        ('玩紙牌遊戲','玩紙牌遊戲'),
                                        ('電玩遊戲','電玩遊戲'),
                                        ('商務社交','商務社交'),
                                        ('電影/視頻','電影/視頻'),
                                        ('做運動','做運動'),
                                        ('志願服務','志願服務'),
                                        ('烹飪','烹飪'),
                                        ('博物館與藝術','博物館與藝術'),
                                        ('政治興趣','政治興趣'),
                                        ('觀看體育賽事','觀看體育賽事'),
			]),
			'sport': forms.CheckboxSelectMultiple(
                                    choices=[
					('有氧運動','有氧運動'),
                                        ('騎腳踏車','騎腳踏車'),
                                        ('跑步','跑步'),
                                        ('舉重/器械運動','舉重/器械運動'),
                                        ('賽車/越野車','賽車/越野車'),
                                        ('橄欖球','橄欖球'),
                                        ('滑雪','滑雪'),
                                        ('瑜珈','瑜珈'),
                                        ('棒球','棒球'),
                                        ('高爾夫','高爾夫'),
                                        ('足球','足球'),
                                        ('其他類型運動','其他類型運動'),
                                        ('籃球','籃球'),
                                        ('跳舞','跳舞'),
                                        ('游泳','游泳'),
                                        ('曲棍球','曲棍球'),
                                        ('撞球/桌球','撞球/桌球'),
                                        ('輪滑','輪滑'),
                                        ('小球類運動','小球類運動'),
                                        ('排球','排球'),
                                        ('保齡球','保齡球'),
                                        ('武術','武術'),
                                        ('散步','散步'),
			]),
		}
		checkbox_value = forms.ChoiceField()
	def __init__(self, *args, **kwargs):
        	super(RegistrationForm, self).__init__(*args, **kwargs)
        	self.fields['account_name'].label = '您的名字'
        	self.fields['matchgender'].label = '尋找對象性別'
        	self.fields['gender'].label = '您的性別'
        	self.fields['star'].label = '星座'
        	self.fields['height'].label = '身高'
       	 	self.fields['hair'].label = '髮色'
		self.fields['sport_habbit'].label = '運動習慣'
		self.fields['smoke'].label = '抽菸'
		self.fields['drink'].label = '喝酒'
		self.fields['figure'].label = '身材'		
       	 	self.fields['eye'].label = '眼睛'
		self.fields['job'].label = '職業'
		self.fields['faith'].label = '信仰'
		self.fields['children'].label = '有無孩子'
		self.fields['income'].label = '收入'
                self.fields['language'].label = '語言'
		self.fields['political'].label = '政治觀點'
		self.fields['education'].label = '教育'
                self.fields['wantchild'].label = '想要小孩'
                self.fields['relationship'].label = '關係'
		self.fields['race'].label = '種族'
		self.fields['sport'].label = '運動與健身'
		self.fields['interest'].label = '我的興趣'
#        	self.fields['captcha'].label = '確定你不是機器人'

class ChooseForm(forms.ModelForm):
        class Meta:
                model = Choose
                fields =['star',]
                widgets = {
	            'star': forms.CheckboxSelectMultiple(
                             choices=[
				('林依晨','林依晨'),
                                ('郭書瑤','郭書瑤'),
                                ('豆花妹','豆花妹'),
                                ('王心凌','王心凌'),
				('舒淇','舒淇'),
                                ('蕭亞軒','蕭亞軒'),
                                ('Angelababy','Angelababy'),
                                ('蔡依林','蔡依林'),
                                ('楊丞琳','楊丞琳'),
                                ('陳意涵','陳意涵'),
                                ('林心如','林心如'),
                                ('Selina','Selina'),
                                ('楊冪','楊冪'),
                                ('林志玲','林志玲'),
                                ('田馥甄','田馥甄'),
                                ('范冰冰','范冰冰'),
                                ('Janet','Janet'),
                                ('張鈞甯','張鈞甯'),
                                ('Ella','Ella'),
                                ('賈永婕','賈永婕'),
                                ('張懸','張懸'),
                                ('陳綺貞','陳綺貞'),
                                ('桂綸鎂','桂綸鎂'),
                                ('魏如萱','魏如萱'),
                                ('吳尊','吳尊'),
                                ('炎亞綸','炎亞綸'),
                                ('賀軍翔','賀軍翔'),
                                ('鄭元暢','鄭元暢'),
                                ('楊祐寧','楊祐寧'),
                                ('彭于晏','彭于晏'),
                                ('阮經天','阮經天'),
                                ('明道','明道'),
                                ('周渝民','周渝民'),
                                ('藍正龍','藍正龍'),
                                ('吳彥祖','吳彥祖'),
                                ('謝霆鋒','謝霆鋒'),
                                ('張孝全','張孝全'),
                                ('陳柏霖','陳柏霖'),
                                ('周杰倫','周杰倫'),
                                ('王力宏','王力宏'),
                                ('蔡旻佑','蔡旻佑'),
                                ('劉以豪','劉以豪'),
                                ('林宥嘉','林宥嘉'),
                                ('潘瑋柏','潘瑋柏'),
                                ('王陽明','王陽明'),
                                ('柯震東','柯震東'),
                                ('王大陸','王大陸'),
                                ('黃曉明','黃曉明'),
                                ('方大同','方大同'),
                                ('盧廣仲','盧廣仲'),
                                ('李榮浩','李榮浩'),
                                ('林俊傑','林俊傑'),
                                ('劉德華','劉德華'),
                                ('金城武','金城武'),
                                ('梁朝偉','梁朝偉'),
                                ('高以翔','高以翔'),
]),
		}
