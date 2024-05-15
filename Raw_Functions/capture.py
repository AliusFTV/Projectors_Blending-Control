import cv2


class Capture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Unable to open video capture device")
            exit()

    def check_hdmi(self):
        return self.cap.isOpened()

    def start_video(self):
        frames = []
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Unable to capture frame")
                break
            frames.append(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
        return frames





