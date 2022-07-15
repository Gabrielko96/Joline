import speech_recognition as sr #biblioteca para ouvir o microfone
import pyttsx3 # biblioteca para retorno de som
import wikipedia
import datetime
import pywhatkit as py

audio = sr.Recognizer() # Criar reconhecedor
maquina = pyttsx3.init() # iniciar o sistema de voz

#Preciso de uma função para apenas 'Joline' e uma funcao para 'joline + funcao de comandos'


def ouvindo_usuario():
    with sr.Microphone() as source:
        try:
            #audio.adjust_for_ambient_noise(source) #diminuir o ruido do microfone
            #melhorar o reconhecimento de voz
            voz = audio.listen(source, timeout=5, phrase_time_limit=5)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()  # transformar em minusculo
            #comando.RunAndWait()
            print(f'voce disse: {comando}')
            #return comando
            if 'joline, jolyne' in comando:  # se ouvir o nome dele (trocar pelo nome do seu assistente)
                #comando = comando.replace('Joline', '')  # retira o nome do assistente para não ficar repetindo
                print('Ativando programa Joline...')
                #joline_ativa()
                return comandos_apenas_joline()
        except:
            print('...')
            return ouvindo_usuario()


'''
def joline_ativa():
    with sr.Microphone() as source:
        try:
            audio.adjust_for_ambient_noise(source) #diminuir o ruido do microfone
            print('Joline ativa, diga o que deseja fazer...')
            voz = audio.listen(source)  # ouvir o microfone
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()  # transformar em minusculo
            #comando.RunAndWait()
            print(f'voce disse: {comando}')
            #return comando
            if 'joline' in comando:  # se ouvir o nome dele (trocar pelo nome do seu assistente)
                comando = comando.replace('Joline', '')  # retira o nome do assistente para não ficar repetindo
                print('Ativando programa Joline...')
                #joline_ativa()
                return joline_ativa()
            elif 'jolyne' in comando:  # se ouvir o nome dele (trocar pelo nome do seu assistente)
                comando = comando.replace('Jolyne', '')  # retira o nome do assistente para não ficar repetindo
                print('Ativando programa Joline...')
                #joline_ativa()
                return joline_ativa()
        except:
            print('...')
            return ouvindo_usuario()
'''


def comandos_apenas_joline():
    print('aqui está na parte COMANDOS JOLINE: ')
    comando = comando
    if 'dia' in comando:
        dia = datetime.datetime.now().strftime("%d/%m/%Y")
        maquina.say('Hoje é ' + dia)
        maquina.runAndWait()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'pesquise' in comando:
        pesquise = comando.replace('pesquise', '')
        wikipedia.set_lang('pt')
        resultado_pesquise = wikipedia.summary(pesquise, 2)
        print(resultado_pesquise)
        maquina.say(resultado_pesquise)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = py.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
    elif 'toca botafogo' in comando:
        musica_botafogo = comando.replace('toca botafogo', '')
        resultado_botafogo = py.playonyt('hino do botafogo')
        maquina.runAndWait()
    elif 'toca raul' in comando:
        musica_botafogo = comando.replace('toca raul', '')
        resultado_botafogo = py.playonyt('Raul seixas')
        maquina.say('Tocando Raul Seixas')
        maquina.runAndWait()
    else:
        maquina.say('Não entendi')
        return ouvindo_usuario()


while True:
    ouvindo_usuario()
