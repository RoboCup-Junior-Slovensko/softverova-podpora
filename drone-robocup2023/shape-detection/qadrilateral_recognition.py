from cv2 import cv2

cap = cv2.VideoCapture(0)
while True:

    f, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #transformacia obrazu do greyscale
    imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 1) #jemné rozmazanie obrazu pre odstránenie šumu
    imgCanny = cv2.Canny(imgBlur, 40, 80) #transformácia do verzie obrazu Canny -> následné využívanie tzv "Canny edge detectora"

    contours, hierarchy = cv2.findContours(imgCanny,
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE) #nájdenie kontúr obrazu

    for c in contours: #prechádzanie kontúr každého frameu
        area = cv2.contourArea(c)

        if area > 1000:
            cv2.drawContours(img, c, -1, (0,255,0), 3) #zakreslovanie kontúr
            approx = cv2.approxPolyDP(c, 0.04*cv2.arcLength(c, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1] #zistenie súradníc (pre nasledovne zakreslenie textu vyhodnoteného útvaru do obrazu)

            if len(approx) == 4: # zistenie počtu uhlov daného útvaru, v tomto prípade hľadáme štvoruholníky
                cv2.putText(imgCanny, "stvoruholnik", (x - 20, y - 20),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))

            else:
                cv2.putText(imgCanny, "Nezadefinovany utvar", (x - 20, y - 20),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))

    cv2.imshow("original", img)
    cv2.imshow("result", imgCanny) #zobrazenie obrazov

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
