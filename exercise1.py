confidences = [.92,.45,.78,.1,.85,.68]

def classification(confidences):

    for i in confidences:
        if(i<.5):
            print('low confidence')
        elif(i<.79):
            print('middle confidence')
        else:
            print('high confidence')

    print(len(confidences))
    print(confidences)

classification(confidences)