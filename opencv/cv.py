import cv2

cap= cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Captura um quadro da webcam

    cv2.imshow('Webcam', frame)  # Exibe o quadro na janela chamada 'Webcam'

    if cv2.waitKey(1) == ord('q'):  # Aguarda 1ms e verifica se a tecla 'q' foi pressionada
        break

cap.release()  # Libera a webcam
cv2.destroyAllWindows()  # Fecha todas as janelas