import matplotlib.pyplot as plt
import cv2
from mtcnn import MTCNN


def show_faces(result, img):
    for i in range(len(result)):
        x1, y1, width, height = result[i]["box"]
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        output = cv2.rectangle(
            img, (x1, y1), (x2, y2), (0, 0, 255), 5
        )  # draws a red rectangle around the face
    return output


def main():
    model = MTCNN()  # Initializes the MTCNN with default values
    img = cv2.imread("images/sample.jpg")  # reads the image
    result = model.detect_faces(img)  # Detects bounding boxes from the specified image
    print(
        f"The imported picture contains {len(result)} persons"
    )  # prints no of faces in the given image
    pic = show_faces(result, img)  # calls the show_faces()
    pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)  # convert BGR -> RGB
    plt.imshow(pic)  # plots the result image
    plt.savefig("images/result.png")  # saves the result image


if __name__ == "__main__":
    main()  # calls main() first
