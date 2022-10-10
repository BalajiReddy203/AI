pairs=[
	["My name is(.*)",["Hello %1,How are you today"]],
	["(.*)help",["yes,I can help you",]],
	["(.*)your name?",["my name is swarna,i am a chatbot",]],
	["how are you(.*)?",["i am great"]],
	["sorry(.*)",["its ok, never mind that",]],
	["(hi|hey|hello|hola|holla)(.*)",["hello","hey there","hi"]],
	["(.*)not feeling (.*)",["ok,tell me your problem",]],
	["(.*)created(.*)",["Mmvc created me using pythons nltk library","top secret:)",]],
        ["(.*)cough(.*)",["take ginger tea and take cough syrup",]],
        ["(.*)(headache/fever)(.*)",["please take paracetamol tablet after food",]],
        ["(.*)stomach(.*)",["please take lightweight food",]],
        ["quit",["bye for now,see you soon ,it was nice talking to you...:)"]],
        ]
from nltk.chat.util import Chat,reflections
print("hi,i am swarna and i am chat bot\n please type lowercase english language to start a conversion \n type quit to leave")
#create chat bot
chat=Chat(pairs,reflections)
#start coversation
chat.converse()


 Output:
 
hi,i am swarna and i am chat bot
 please type lowercase english language to start a conversion 
 type quit to leave
>hi
hello
>how are you
i am great
>cough
take ginger tea and take cough syrup
>headache
None
>bye
None
>
