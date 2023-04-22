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
    questiontest = []

    iAnswerthetest = answerusr.objects.filter(answerusrMember=request.user.member).count()

    formtest = testform.objects.get(pk=pk)

    data1_questiontest =  question.objects.all().filter(questionTestform=pk)
    data2_anwsertest = answer.objects.all().filter()
    total_forms= testform.objects.all().filter(isEnabled=True).count()
    total_responses= formtest.responseOrder - 1
    get_countQuestion = []
    get_countQuestion = len(question.objects.all().filter(questionTestform=pk))

    print(get_countQuestion)

    form1_answerToquestion = AnswerusrForm() 
    # |======== Validación de método POST ==================|
    if request.method == 'POST':
        form1_answerToquestion = AnswerusrForm(request.POST)
        print('Aquí entro a post')
        # |============ Validación de primer formulario ==============|
        if form1_answerToquestion.is_valid():
            print('Sí soy válido1')
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
                print('Ya leí datos1')
                answerusrx.save()
            return redirect(reverse('home'))
    else:
        print('Válio madres')
        print('valio quezo')
        print('valio cheto')
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
    'totalresponses': total_responses
    }
    return render(request, 'member/home.html', context)

