import Lexema
import Litera
import FSM_model as fms

if __name__ == '__main__':
    namefile='input.txt'
    try:
        fileInput = open(namefile, 'r')
    except:
        print('Error while oppening file')
        exit()

    fileOutput = open('output.txt', 'w')
    FiniteStateMachine = fms.FSM_Model(fileInput, fileOutput)
    FiniteStateMachine.Start()

    fileInput.close()
    fileOutput.close()
