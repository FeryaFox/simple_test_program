import json
import math


def parse_answers(answers):
    answers_string = ''
    j = 1
    for il in answers:
        answers_string += f'    {j}) {il}\n'
        j += 1
    return answers_string


def parse_data_with_correct_and_wrong_answer():
    data = ''

    for il in wrong_answers:
        j = 1
        data += f"{il['question_num']}) {questions[il['question_num']-1]['question']}\n"
        for jl in questions[il['question_num']-1]['answers']:
            if j == il['answer']:
                data += f'×{j}) {questions[il["question_num"]-1]["answers"][j-1]}\n'
            elif j == questions[il['question_num']-1]['correct_answer']:
                data += f'*{j}) {questions[il["question_num"]-1]["answers"][j-1]}\n'
            else:
                data += f' {j}) {questions[il["question_num"]-1]["answers"][j-1]}\n'
            j += 1
        data += '\n'
    return data


def get_grade():
    grade_from_one_question = 5/len(questions)
    grade = math.ceil(grade_from_one_question*count_of_correct)
    return grade


with open('questions.json', 'r', encoding='utf-8') as r:
    questions = json.load(r)
    r.close()

questions_num = 1
wrong_answers = []
count_of_correct = 0
count_of_wrong = 0

for i in questions:
    print(f'Вопрос № {questions_num} {i["question"]}\n{parse_answers(i["answers"])}')
    while True:
        answer = input('Введите номер ответа: ')
        if not answer.isdigit() or int(answer) > len(i["answers"]):
            print('Вы ввели некоректный ответ')
            continue
        else:
            answer_int = int(answer)
            if answer_int == i['correct_answer']:
                count_of_correct += 1
            else:
                wrong_answers.append({'question_num': questions_num, 'answer': answer_int})
                count_of_wrong += 1
            break
    print('')
    questions_num += 1

show_the_correct_answer = False
wrong_answers_r = ''
if count_of_wrong != 0:
    wrong_answers_r = parse_data_with_correct_and_wrong_answer()

print(f"""
Вы правильно ответили на {count_of_correct}, вы неправльно ответили на {count_of_wrong}.
Ваша оценка {get_grade()}
{wrong_answers_r}
""")
