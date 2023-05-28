# |=============================================================|
# |===============|         BIBLIOTECAS         |===============|
# |=============================================================|

# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.http import JsonResponse


# |=========================================|
# |=====|       BIBLIOTECAS BASE      |=====|
# |=========================================|
from django.contrib import messages

# |=========================================|
# |=====|     BIBLILIOTECAS EXTRAS    |=====|
# |=========================================|

# |=========================================|
# |=====|     REFERENCIAS A MODELOS   |=====|
# |=========================================|
from .models import testform,question,answer,answerusr

# |=========================================|
# |=====|  REFERENCIAS A FORMULARIOS  |=====|
# |=========================================|
from .forms import AnswerusrForm
# |=============================================================|
# |===============|      COMIENZAN VISTAS       |===============|
# |=============================================================|
def formQuestion(request,pk):
    graphicQuest = 1
    questiontest = []
    if request.user.is_authenticated:
        iAnswerthetest = answerusr.objects.filter(answerusrMember=request.user.member.pk).count()
        formtest = testform.objects.get(pk=pk)

        data1_questiontest =  question.objects.all().filter(questionTestform=pk)
        data2_anwsertest = answer.objects.all().filter()
        total_forms= testform.objects.all().filter(isEnabled=True).count()
        total_responses= formtest.responseOrder - 1
        get_countQuestion = []
        get_countQuestion = len(question.objects.all().filter(questionTestform=pk))

        formAnswered= answerusr.objects.filter(answerusrMember = request.user.member,answerusrQuestion__in=data1_questiontest).count()

        print(get_countQuestion)

        form1_answerToquestion = AnswerusrForm() 
        # |======== Validación de método POST ==================|
        if request.method == 'POST':
            form1_answerToquestion = AnswerusrForm(request.POST)
            # |============ Validación de primer formulario ==============|
            if form1_answerToquestion.is_valid():
                # |= Ciclo for de 1 hasta la cantidad de respuestas registradas =|
                for nQuestion in range(1,get_countQuestion+1):
                    # |========== Asignación de pregunta más el contador=========|
                    answerusrToquestionx = "answerusrToquestion" + str(nQuestion)
                    answerusrQuestionx = "answerusrQuestion" + str(nQuestion)
                    answerusrx = "answerusrx" + str(nQuestion)
                    
                    answerusrToquestion = request.POST[answerusrToquestionx]
                    answerusrQuestion = question.objects.get(id = request.POST[answerusrQuestionx])  

                    # |===== Creación de inserción de respuesta del usuario =====|
                    answerusrx = answerusr.objects.create(
                        answerusrToquestion = answerusrToquestion,
                        answerusrQuestion = answerusrQuestion,
                        answerusrMember = request.user.member
                    )

                    text = "Tus respuestas han sido enviadas correctamente, gracias por tu tiempo."
                    messages.success(request, text)
                    answerusrx.save()
                return redirect(reverse('home'))
        else:
            print('Error al entrar a POST')
        print('Primary key: '+ str(pk))
        print(formtest.testName)

        context = {
        'formtest': formtest,
        'questiontest':data1_questiontest,
        'anwsertest': data2_anwsertest,
        'count_question': get_countQuestion,
        'answerdone': iAnswerthetest,
        'form': form1_answerToquestion,
        'totalforms':total_forms,
        'totalresponses': total_responses,
        'formanswered':formAnswered,
        'graphicQuest':graphicQuest,
        }
        return render(request, 'member/home.html', context)
    else:
        return redirect(reverse('home'))



# |=========================================|
# |=====|  Calculo de promedio forms  |=====|
# |=====|  jsonAverage                |=====|
# |=========================================|
# |=| Es parte de home, se utiliza para   |=|
# |=| obtener de forma automática las     |=|
# |=| respuestas del formulario.          |=|
# |=========================================|
def jsonAverage(request):
    result1 = [0,0,0]

    result1[0] = CalProm(1)
    result1[1] = CalProm(2)
    result1[2] = CalProm(3)
    
    if (result1[0] > 0 or result1[1] > 0 or result1[2] > 0 ):
        data1 = {'message': "Success","result":result1}
    else:
        data1 = {'message': "No se encontro"}

    return JsonResponse(data1)

# |=========================================|
# |=====|  Calculo de promedio forms  |=====|
# |=========================================|
# |=| Es parte de home, se utiliza para   |=|
# |=| obtener de forma automática las     |=|
# |=| respuestas del formulario.          |=|
# |=========================================|
def CalProm(num):
    # |=========================================|
    # |=|Sub-resultados de obtención de datos |=|
    # |=========================================|
    result1 = []

    result1_1 = []
    result2_2 = []

    result1_1_1 = []

    result1_1_1_1 = []

    quest1 = question.objects.filter(questionTestform=num)
    # |=========================================|
    # |===| Obtencion de pk de preguntas    |===|
    # |===| correspondientes al formulario. |===|
    # |=========================================|
    for data1 in quest1:
        result1.append(data1.pk)
    # |=========================================|
    # |===| Obtención de respuestas         |===|
    # |===| correspondientes al formulario. |===|
    # |=========================================|
    for answerData1 in result1:
        answer1 = answer.objects.filter(answerQuestion = answerData1).filter(answerRight=True)
        for answerForData1 in answer1:
            result1_1.append(answerForData1.pk)
            answerUsrData1 = answerusr.objects.filter(answerusrToquestion = answerForData1.pk) 
            for answerForData2 in answerUsrData1:
                result1_1_1.append(answerForData2.pk)
    # |=========================================|
    # |===| Obtención de respuestas T and F |===|
    # |===| correspondientes al formulario. |===|
    # |=========================================|
    for answerData2_2 in result1:
        answer2 = answer.objects.filter(answerQuestion = answerData2_2).filter(answerRight=False) 
        for answerForData2_2 in answer2:
            result2_2.append(answerForData2_2.pk)
            answerUsrData2_2 = answerusr.objects.filter(answerusrToquestion = answerForData2_2.pk)
            for answerForData2_2_2 in answerUsrData2_2:
                result1_1_1_1.append(answerForData2_2_2.pk)
    # |=========================================|
    # |==| Operaciones para obtener promedio |==|
    # |==| de cada formulario en automático. |==|
    # |=========================================|
    Fres = ((len(result1_1_1))/(len(result1_1_1_1) + (len(result1_1_1))) * 100)

    return Fres


