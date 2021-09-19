import json


def parse_answers(answers):
    answers_string = ''
    j = 1
    for i in answers:
        answers_string += f'    {j}) {i}\n'
        j += 1
    return answers_string


def create_questions():
    num_of_questions = 1
    num_of_answer = 1
    questions = []
    answers = []
    while True:
        question = input(f'Введите текст вопроса номер {num_of_questions} или нажмите Enter для завершения создания '
                         f'вопросов: ')
        if question != '':
            while True:
                answer = input(f'Теперь введите вариант ответа под номером {num_of_answer} или нажмите Enter, если '
                               f'вариант ответа последний: ')
                if answer != '':
                    answers.append(answer)
                    num_of_answer += 1
                    continue
                else:
                    correct_answer = input(f'Теперь введите номер правильного ответа\n{parse_answers(answers)}')
                    while True:
                        if not correct_answer.isdigit() or int(correct_answer) > len(answers):
                            correct_answer = input('Вы ввели номер ответа, которого не существует, введите корректный '
                                                   'номер: ')
                            continue
                        questions.append({'question': question, 'answers': answers, 'correct_answer': int(correct_answer)})
                        num_of_answer = 1
                        answers = []
                        break
                    break
            num_of_questions += 1
        else:
            return questions


def main():
    questions = create_questions()
    if questions != []:
        with open('questions.json', 'w', encoding='utf-8') as f:
            json.dump(questions, f, ensure_ascii=False, indent=4)
            f.close()
        print('Вопросы созданы и успешно записаны')


if __name__ == "__main__":
    main()
