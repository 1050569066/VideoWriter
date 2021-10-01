import cv2,time,os

input("Press Enter to start...")
rt = 5
while rt>0:
    print(f"Start in {rt} seconds")
    time.sleep(1)
    rt -= 1

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("movie.mp4",fc,16,(800,600))
cap.set(3,800)
cap.set(4,600)
while True:
    try:
        ret,frame = cap.read()
        cv2.imshow("capture",frame)
        out.write(frame)
        memory = round(os.path.getsize("movie.mp4")/(1024*1024),1)
        print(f"{memory} MB was taken.")
        if cv2.waitKey(1) == ord("q"):
            cv2.imwrite("end.png",frame)
            break
    except KeyboardInterrupt:
        break
    except:
        print("Error!")
        continue
cap.release()
cv2.destroyAllWindows()