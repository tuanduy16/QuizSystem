from tkinter import *
import tkinter as tk
from Question import *

index = 0
quizes = ListQuestion('data.txt')
original = quizes.qs
result = quizes.clone()
confirmed = False
def goto_previous_question(event):
    global index
    if index>0:
        index-=1
    btn_previous['state'] ='normal' 
    btn_next['state'] ='normal' 
    if index ==0 :
        btn_previous['state'] ='disabled' 
    display_question(index)

def goto_next_question(event):
    global index
    if index<(len(result)-1):
        index+=1
    btn_previous['state'] ='normal' 
    btn_next['state'] ='normal' 
    if index == len(result)-1 :
        btn_next['state'] ='disabled' 
    display_question(index)

def confirm(event):
    global confirmed
    confirmed = True
    evaluation = Evaluation(original,result)
    ans, non_ans, correct, incorrect = evaluation.evaluate()
    lb_report["text"] ="Kết quả: Trả lời {}/{}, trả lời đúng {}, trả lời sai {}, đạt {}%".format(ans, ans+non_ans, correct, incorrect,correct*100/(correct+incorrect))
    btn_confirm['state'] ='disabled' 
    
def display_question(index):
    groupbox_question['text']="Nội dung câu hỏi {}/{}".format(index+1,len(result))
    question_text.delete(1.0,'end')
    question_text.insert(1.0, result[index].text)
    
    text_answer1.delete(1.0,'end')
    text_answer1.insert(1.0, result[index].aws[0].text)
    cb1.set(result[index].aws[0].flag)
    
    text_answer2.delete(1.0,'end')
    text_answer2.insert(1.0, result[index].aws[1].text)
    cb2.set(result[index].aws[1].flag)

    text_answer3.delete(1.0,'end')
    text_answer3.insert(1.0, result[index].aws[2].text)
    cb3.set(result[index].aws[2].flag)
    
    text_answer4.delete(1.0,'end')
    text_answer4.insert(1.0, result[index].aws[3].text)
    cb4.set(result[index].aws[3].flag)
    
    if confirmed:
        clear()
        for i in range(4):
            if original[index].aws[i].flag == result[index].aws[i].flag and result[index].aws[i].flag == True:
                if i==0:
                    ckbnt1['bg'] = 'green'
                    text_answer1['bg'] = 'green'
                if i==1:
                    ckbnt2['bg'] = 'green'
                    text_answer2['bg'] = 'green'
                if i==2:
                    ckbnt3['bg'] = 'green'
                    text_answer3['bg'] = 'green'
                if i==3:
                    ckbnt4['bg'] = 'green'
                    text_answer4['bg'] = 'green'
            elif original[index].aws[i].flag != result[index].aws[i].flag and result[index].aws[i].flag == True:
                if i==0:
                    ckbnt1['bg'] = 'red'
                    text_answer1['bg'] = 'red'
                if i==1:
                    ckbnt2['bg'] = 'red'
                    text_answer2['bg'] = 'red'
                if i==2:
                    ckbnt3['bg'] = 'red'
                    text_answer3['bg'] = 'red'
                if i==3:
                    ckbnt4['bg'] = 'red'
                    text_answer4['bg'] = 'red'
def clear():
    ckbnt1['bg'] = 'SystemButtonFace'
    ckbnt2['bg'] = 'SystemButtonFace'
    ckbnt3['bg'] = 'SystemButtonFace'
    ckbnt4['bg'] = 'SystemButtonFace'
    text_answer1['bg'] = 'white'
    text_answer2['bg'] = 'white'
    text_answer3['bg'] = 'white'
    text_answer4['bg'] = 'white'
    ckbnt1['state'] ='disabled' 
    ckbnt2['state'] ='disabled' 
    ckbnt3['state'] ='disabled' 
    ckbnt4['state'] ='disabled' 
    
def get_aws1(event):
    result[index].aws[0].flag = not eval(str(cb1.get()))
    
def get_aws2(event):
    result[index].aws[1].flag = not eval(str(cb2.get()))
    
def get_aws3(event):
    result[index].aws[2].flag = not eval(str(cb3.get()))
    
def get_aws4(event):
    result[index].aws[3].flag = not eval(str(cb4.get()))
    
root = tk.Tk()
root.geometry("750x650")
root.resizable(0,0)

groupbox_question = tk.LabelFrame(master=root, text="Nội dung câu hỏi 1/{}".format(len(result)))
groupbox_question.pack(expand=True, fill=BOTH)
question_text = tk.Text(master=groupbox_question, width=80, height=10)
question_text.pack(expand=True, fill=BOTH)

groupbox_answers = tk.LabelFrame(master=root, text='Các đáp án')
groupbox_answers.pack(expand=True, fill=BOTH)

cb1 = tk.BooleanVar()
cb2 = tk.BooleanVar()
cb3 = tk.BooleanVar()
cb4 = tk.BooleanVar()

ckbnt1 = tk.Checkbutton(groupbox_answers, variable=cb1, text="", onvalue=True, offvalue=False)
ckbnt1.grid(row=0, column=0, padx=5, pady=5)
ckbnt1.bind('<Button-1>',get_aws1)

ckbnt2 = tk.Checkbutton(groupbox_answers, variable=cb2, text="", onvalue=True, offvalue=False)
ckbnt2.grid(row=0, column=2, padx=5, pady=5)
ckbnt2.bind('<Button-1>',get_aws2)

ckbnt3 = tk.Checkbutton(groupbox_answers, variable=cb3, text="", onvalue=True, offvalue=False)
ckbnt3.grid(row=1, column=0, padx=5, pady=5)
ckbnt3.bind('<Button-1>',get_aws3)

ckbnt4 = tk.Checkbutton(groupbox_answers, variable=cb4, text="", onvalue=True, offvalue=False)
ckbnt4.grid(row=1, column=2, padx=5, pady=5)
ckbnt4.bind('<Button-1>',get_aws4)

text_answer1 = tk.Text(groupbox_answers, width=20, height=6)
text_answer1.grid(row=0, column=1, padx=5, pady=5, ipady=8)

text_answer2 = tk.Text(groupbox_answers, width=20, height=6)
text_answer2.grid(row=0, column=3, padx=5, pady=5, ipady=8)

text_answer3 = tk.Text(groupbox_answers, width=20, height=6)
text_answer3.grid(row=1, column=1, padx=5, pady=5, ipady=8)
 
text_answer4 = tk.Text(groupbox_answers, width=20, height=6)
text_answer4.grid(row=1, column=3, padx=5, pady=5, ipady=8)

# photo_previous = tk.PhotoImage(file=r'D:\Hoc_ol_python\previous.png')
# btn_previous = tk.Button(groupbox_answers, text="Câu hỏi trước", image=photo_previous, compound=LEFT)
btn_previous = tk.Button(groupbox_answers, text="Câu hỏi trước",  compound=LEFT)
btn_previous.grid(row=2, column=1)
btn_previous.bind("<Button-1>", goto_previous_question)

# photo_next = tk.PhotoImage(file=r'next.jpg')
btn_next = tk.Button(groupbox_answers, text="Câu hỏi tiếp theo", compound=LEFT)
btn_next.grid(row=2, column=2)
btn_next.bind("<Button-1>", goto_next_question)

# photo_done = tk.PhotoImage(file=r'done.jpg')
btn_confirm = tk.Button(groupbox_answers, text="Kết thúc", compound=LEFT)
btn_confirm.grid(row=2, column=3, sticky='e')
btn_confirm.bind("<Button-1>", confirm)

lb_report = tk.Label(groupbox_answers, text="")
lb_report.grid(row=3, column=0, columnspan=4, pady=6, sticky='w')

display_question(index)
root.mainloop()from tkinter import *
import tkinter as tk
from Question import *

index = 0
quizes = ListQuestion('data.txt')
original = quizes.qs
result = quizes.clone()
confirmed = False
def goto_previous_question(event):
    global index
    if index>0:
        index-=1
    btn_previous['state'] ='normal' 
    btn_next['state'] ='normal' 
    if index ==0 :
        btn_previous['state'] ='disabled' 
    display_question(index)

def goto_next_question(event):
    global index
    if index<(len(result)-1):
        index+=1
    btn_previous['state'] ='normal' 
    btn_next['state'] ='normal' 
    if index == len(result)-1 :
        btn_next['state'] ='disabled' 
    display_question(index)

def confirm(event):
    global confirmed
    confirmed = True
    evaluation = Evaluation(original,result)
    ans, non_ans, correct, incorrect = evaluation.evaluate()
    lb_report["text"] ="Kết quả: Trả lời {}/{}, trả lời đúng {}, trả lời sai {}, đạt {}%".format(ans, ans+non_ans, correct, incorrect,correct*100/(correct+incorrect))
    btn_confirm['state'] ='disabled' 
    
def display_question(index):
    groupbox_question['text']="Nội dung câu hỏi {}/{}".format(index+1,len(result))
    question_text.delete(1.0,'end')
    question_text.insert(1.0, result[index].text)
    
    text_answer1.delete(1.0,'end')
    text_answer1.insert(1.0, result[index].aws[0].text)
    cb1.set(result[index].aws[0].flag)
    
    text_answer2.delete(1.0,'end')
    text_answer2.insert(1.0, result[index].aws[1].text)
    cb2.set(result[index].aws[1].flag)

    text_answer3.delete(1.0,'end')
    text_answer3.insert(1.0, result[index].aws[2].text)
    cb3.set(result[index].aws[2].flag)
    
    text_answer4.delete(1.0,'end')
    text_answer4.insert(1.0, result[index].aws[3].text)
    cb4.set(result[index].aws[3].flag)
    
    if confirmed:
        clear()
        for i in range(4):
            if original[index].aws[i].flag == result[index].aws[i].flag and result[index].aws[i].flag == True:
                if i==0:
                    ckbnt1['bg'] = 'green'
                    text_answer1['bg'] = 'green'
                if i==1:
                    ckbnt2['bg'] = 'green'
                    text_answer2['bg'] = 'green'
                if i==2:
                    ckbnt3['bg'] = 'green'
                    text_answer3['bg'] = 'green'
                if i==3:
                    ckbnt4['bg'] = 'green'
                    text_answer4['bg'] = 'green'
            elif original[index].aws[i].flag != result[index].aws[i].flag and result[index].aws[i].flag == True:
                if i==0:
                    ckbnt1['bg'] = 'red'
                    text_answer1['bg'] = 'red'
                if i==1:
                    ckbnt2['bg'] = 'red'
                    text_answer2['bg'] = 'red'
                if i==2:
                    ckbnt3['bg'] = 'red'
                    text_answer3['bg'] = 'red'
                if i==3:
                    ckbnt4['bg'] = 'red'
                    text_answer4['bg'] = 'red'
def clear():
    ckbnt1['bg'] = 'SystemButtonFace'
    ckbnt2['bg'] = 'SystemButtonFace'
    ckbnt3['bg'] = 'SystemButtonFace'
    ckbnt4['bg'] = 'SystemButtonFace'
    text_answer1['bg'] = 'white'
    text_answer2['bg'] = 'white'
    text_answer3['bg'] = 'white'
    text_answer4['bg'] = 'white'
    ckbnt1['state'] ='disabled' 
    ckbnt2['state'] ='disabled' 
    ckbnt3['state'] ='disabled' 
    ckbnt4['state'] ='disabled' 
    
def get_aws1(event):
    result[index].aws[0].flag = not eval(str(cb1.get()))
    
def get_aws2(event):
    result[index].aws[1].flag = not eval(str(cb2.get()))
    
def get_aws3(event):
    result[index].aws[2].flag = not eval(str(cb3.get()))
    
def get_aws4(event):
    result[index].aws[3].flag = not eval(str(cb4.get()))
    
root = tk.Tk()
root.geometry("750x650")
root.resizable(0,0)

groupbox_question = tk.LabelFrame(master=root, text="Nội dung câu hỏi 1/{}".format(len(result)))
groupbox_question.pack(expand=True, fill=BOTH)
question_text = tk.Text(master=groupbox_question, width=80, height=10)
question_text.pack(expand=True, fill=BOTH)

groupbox_answers = tk.LabelFrame(master=root, text='Các đáp án')
groupbox_answers.pack(expand=True, fill=BOTH)

cb1 = tk.BooleanVar()
cb2 = tk.BooleanVar()
cb3 = tk.BooleanVar()
cb4 = tk.BooleanVar()

ckbnt1 = tk.Checkbutton(groupbox_answers, variable=cb1, text="", onvalue=True, offvalue=False)
ckbnt1.grid(row=0, column=0, padx=5, pady=5)
ckbnt1.bind('<Button-1>',get_aws1)

ckbnt2 = tk.Checkbutton(groupbox_answers, variable=cb2, text="", onvalue=True, offvalue=False)
ckbnt2.grid(row=0, column=2, padx=5, pady=5)
ckbnt2.bind('<Button-1>',get_aws2)

ckbnt3 = tk.Checkbutton(groupbox_answers, variable=cb3, text="", onvalue=True, offvalue=False)
ckbnt3.grid(row=1, column=0, padx=5, pady=5)
ckbnt3.bind('<Button-1>',get_aws3)

ckbnt4 = tk.Checkbutton(groupbox_answers, variable=cb4, text="", onvalue=True, offvalue=False)
ckbnt4.grid(row=1, column=2, padx=5, pady=5)
ckbnt4.bind('<Button-1>',get_aws4)

text_answer1 = tk.Text(groupbox_answers, width=20, height=6)
text_answer1.grid(row=0, column=1, padx=5, pady=5, ipady=8)

text_answer2 = tk.Text(groupbox_answers, width=20, height=6)
text_answer2.grid(row=0, column=3, padx=5, pady=5, ipady=8)

text_answer3 = tk.Text(groupbox_answers, width=20, height=6)
text_answer3.grid(row=1, column=1, padx=5, pady=5, ipady=8)
 
text_answer4 = tk.Text(groupbox_answers, width=20, height=6)
text_answer4.grid(row=1, column=3, padx=5, pady=5, ipady=8)

# photo_previous = tk.PhotoImage(file=r'D:\Hoc_ol_python\previous.png')
# btn_previous = tk.Button(groupbox_answers, text="Câu hỏi trước", image=photo_previous, compound=LEFT)
btn_previous = tk.Button(groupbox_answers, text="Câu hỏi trước",  compound=LEFT)
btn_previous.grid(row=2, column=1)
btn_previous.bind("<Button-1>", goto_previous_question)

# photo_next = tk.PhotoImage(file=r'next.jpg')
btn_next = tk.Button(groupbox_answers, text="Câu hỏi tiếp theo", compound=LEFT)
btn_next.grid(row=2, column=2)
btn_next.bind("<Button-1>", goto_next_question)

# photo_done = tk.PhotoImage(file=r'done.jpg')
btn_confirm = tk.Button(groupbox_answers, text="Kết thúc", compound=LEFT)
btn_confirm.grid(row=2, column=3, sticky='e')
btn_confirm.bind("<Button-1>", confirm)

lb_report = tk.Label(groupbox_answers, text="")
lb_report.grid(row=3, column=0, columnspan=4, pady=6, sticky='w')

display_question(index)


root.mainloop()
