from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime 
from spy import *

async def command_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')
    
async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f"""Сommands menu:
        /hello
        /time
        /date
        /help
        /sum A C         <Sum of rational numbers>
        /sum A,Bi C,Di <Sum of complex numbers> 
        /diff A C        <Diff of rational numbers> 
        /diff A,Bi C,Di <Diff of complex numbers>
        /mult A C <Mult of rational numbers>
        /mult A,Bi C,Di <Mult of complex numbers> 
        /div a c         <Div of rational numbers>
        /div A,Bi C,Di <Div of complex numbers>
        """
                                    )
    
async def command_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    # await update.message.reply_text(f'{datetime.datetime.now().time()}')
    await update.message.reply_text(f'{datetime.datetime.now().strftime("%H:%M:%S")}')
    
async def command_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    # await update.message.reply_text(f'{datetime.datetime.now().time()}')
    await update.message.reply_text(f'{datetime.datetime.now().strftime("%d.%m.%Y")}')
    
def getABCD(msg):
    isComplex = 0
    
    lst = msg.split() #/command a,bi c,di
    lst1 = lst[1].split(",") # a bi 
    a = int(lst1[0]) 
    if len(lst1)>1:
        string1 = lst1[1].replace('i','')
        b = int(string1)  
        isComplex = 1
    else:
        b = 0
    
    lst2 = lst[2].split(",")
    c = int(lst2[0]) 
    if len(lst2)>1:
        string2 = lst2[1].replace('i',' ')
        d = int(string2)
        isComplex = 1
    else:
        d = 0
    
    return isComplex,a,b,c,d

async def command_sum(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.effective_message.text
    
    print(msg)
    
    isComplex,a,b,c,d = getABCD(msg)
    
    if isComplex:  
        if b>=0:
            char1 = '+'
        else:
            char1 = '-'

        if d>=0:
            char2 = '+'
        else:
            char2 = '-' 
        
        if b+d>=0:
            char3 = '+'
        else:
            char3 = '-' 
        
        await update.message.reply_text(f'({a} {char1} {abs(b)}i) + ({c} {char2} {abs(d)}i) = ({a+c} {char3} {abs(b+d)}i)')
    
    else:
        if c>=0:
            char1 = '+'
        else:
            char1 = '-'
        await update.message.reply_text(f'{a} {char1} {abs(c)} = {a+c}')
    
async def command_diff(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.effective_message.text
    
    print(msg)
    
    isComplex,a,b,c,d = getABCD(msg)
    
    if isComplex:
        if b>=0:
            char1 = '+'
        else:
            char1 = '-'

        if d>=0:
            char2 = '+'
        else:
            char2 = '-' 
        
        if b-d>=0:
            char3 = '+'
        else:
            char3 = '-' 
        
        await update.message.reply_text(f'({a} {char1} {abs(b)}i) - ({c} {char2} {abs(d)}i) = ({a-c} {char3} {abs(b-d)}i)')
    else: 
        if c>=0:
            await update.message.reply_text(f'{a} - {c} = {a-c}')
        else:
            await update.message.reply_text(f'{a} - ({c}) = {a-c}')
    
async def command_mult(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.effective_message.text
    
    print(msg)
    
    isComplex,a,b,c,d = getABCD(msg)
    
    if isComplex:
        if b>=0:
            char1 = '+'
        else:
            char1 = '-'

        if d>=0:
            char2 = '+'
        else:
            char2 = '-' 
        
        if a*d+b*c>=0:
            char3 = '+'
        else:
            char3 = '-' 
        
        await update.message.reply_text(f'({a} {char1} {abs(b)}i) * ({c} {char2} {abs(d)}i) = ({a*c-b*d} {char3} {abs(a*d+b*c)}i)')
    else:
        if c>=0:
            await update.message.reply_text(f'{a} * {c} = {a*c}')
        else:
            await update.message.reply_text(f'{a} * ({c}) = {a*c}')
    
async def command_div(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.effective_message.text
    
    print(msg)
    
    isComplex,a,b,c,d = getABCD(msg)
    
    if isComplex:
        if b>=0:
            char1 = '+'
        else:
            char1 = '-'

        if d>=0:
            char2 = '+'
        else:
            char2 = '-' 
            
        denom = c*c+d*d
        if denom == 0:
            await update.message.reply_text(f'input error')
            return
            
        
        if (b*c-a*d)/(denom)>=0:
            char3 = '+'
        else:
            char3 = '-' 
        
        await update.message.reply_text(f'({a} {char1} {abs(b)}i) / ({c} {char2} {abs(d)}i) = ({(a*c+b*d)/(denom)} {char3} {abs(b*c-a*d)/denom}i)')
    else:
        if c == 0:
            await update.message.reply_text(f'input error')
            return 
        elif c>=0:
            await update.message.reply_text(f'{a} / {c} = {a/c}')
        else:
            await update.message.reply_text(f'{a} / ({c}) = {a/c}')