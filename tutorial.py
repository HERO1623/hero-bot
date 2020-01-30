#再井字符號後面的都是註解
#不會干擾程式運作


import discord #載入剛剛安裝的Discord

from discord.ext import commands #載入Discord裡的指令組鍵

bot = commands.Bot(command_prefix='*') #這行是指 : BOT(機器人)的指令開頭為 >，而bot代表discord的一個元素 : client(客戶端，你的電腦)
token = "NjcyMDIwNjg2ODgwODk5MDgz.XjFlqA.eUrB_kAldaIjt_g27iDSHKfBDas" #每個使用者都有Token(跟ID很像)，但是是登入時需要的ID。機器人當然也有

#使用 <變數名> = <變數的數值> 可以設定變數，而變數可以處存幾乎全部的物件，像是str(文字),int(數字),Bool(像是True(真)或者False(假))
#或者是discord機器人裡的member
#類別。如果有玩過Scratch(現代國小都有教吧?)，那麼應該就清楚了解變數的意思



@bot.event #一個事件
async def on_ready(): #覆蓋掉原本在檔案中事件(原本是pass，代表不做任何事)
    await bot.change_presence(activity=discord.Game(name='*help'))  #每次要做 "動作" 時就要先用"await"，Discord Bot 的規定
    print(f'本機器人已與Discord連線，使用者名稱為{bot.user} !'f'Created by FANA Owner') #傳送連線的訊息




@bot.command() #另一個事件，指令事件
async def 幹嘛(ctx): #自訂一個事件，指令事件，當指令 >hi時執行
    await ctx.send("你好") #指令事件觸發時要做的事，這裡是傳訊息，ctx是一個物件，send是ctx裡面的其中一個動作。
                        #跟前面一樣屬於動作類，所以一樣要用await


@bot.command() #一樣，指令事件
async def hi(ctx,*,你好): #ctx是context，意思是"指令"這個物件。是指後方文字可以有空格。*只能放在倒數第2個，否則無效。
    #saymsg 是可以隨便亂取的名稱，像是 >say i am good， saymsg 就會是 i am good。
    await ctx.send("嗨囉") #saymsg就是變數，而在輸入指令時就設定玩了(>say i am good，則變數就是i am good)


@bot.command()


async def 伺服器資訊(ctx): #一個沒有arg(>say hi，hi就是arg)的指令
    embed = discord.Embed(title = "群組資訊",descirption = "來看看吧",colour = discord.Colour.green())#一個EMBED，就是我家機器人用>help會跑出來的東西，那種格式的訊息就要用embed
    #discord算一個資料夾，他在前面的import discord就被載入
    #而discord裡面有很多項目，這裡是使用discord裡面的動作 :embed(title,description,colour)。
    #他們的動作就跟我們做指令很像，只是沒有ctx。而title就好比>say hi的"hi"字串，這裡是設定title這個變數為"群組資訊"
    #而description這個變數設為"來看看吧"，#colour設定為discord.Colour.red()。Discord(之前載入的資料夾).Colour(裡面的資料夾)
    #.red()(裡面的一個"檔案")。而這個red檔案他會傳給我們程式 紅色 這個資料(不是字串)
    embed.add_field(name = "資訊~",value="伺服器名稱:Pride Of Doom 末日尊嚴 伺服器區域:Japan")#Embed這個資料夾剛剛創建了(上一行程式碼，discord.embed那個)
    #embed.add_field可以新增一個field(使用此指令時就知道field是什麼了)
    await ctx.send(embed=embed)#讓前面那個ctx資料夾(serverinfo後面有設定，意旨指令本身)找到send檔案，並且給send檔案資訊:embed=embed
    #意思是要discord機器人在傳指令的頻道傳出剛剛的EMBED
    #平時很容易忘了這一句，因此embed要記得傳到群組。
    #(因為send發送算是動做，因此要加上await)



bot.run(token) #與機器人連線，而token在前面程式碼有，在這段程式中寫token是因為前面已經"定義"出一個token(token = <機器人的token>)
