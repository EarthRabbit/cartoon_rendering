# cartoon_rendering
cartoon rendering tool using opencv

## Modules used
* Numpy
* cv2

## Description
이미지를 만화 그림체로 바꾸는 과정은 다음과 같다.

1. 이미지를 흑백으로 바꾼다.
  ```bibtex
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  ```

2. Median blur(중간값 보정)를 이용하여 이미지에 있던 노이즈를 없앤다.
  ```bibtex
  gray = cv.medianBlur(gray, 5)
  ```
3. cv의 Adaptive thresholding(적응형 임계값)을 이용하여 테두리를 만든다. 
  ```bibtex
  edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 7)
  ```
  * 마지막 2개의 parameter를 조절함으로써 테두리를 적용하는 임계점을 조정할 수 있다.

4. 이미지를 컬러 이미지로 바꾼다.
  ```bibtex
  color = cv.bilateralFilter(img, 9, 300, 300)
  ```

4-1. k-means 기법을 이용하여 대표적인 색을 추려 가장 자주 나오는 이미지의 색을 대표로 하여 K색으로 바꾼다.

  ```bibtex
  data = np.float32(img).reshape(-1, 3)
  criteria = (cv.TermCriteria_EPS + cv.TermCriteria_MAX_ITER, 20, 0.1)
  _, labels, centers = cv.kmeans(data, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
  centers = np.uint8(centers)
  clustered_img = centers[labels.flatten()].reshape(img.shape)
  ```

5. cv.bitwise_and()를 이용하여 처리한 사진에 테두리를 더한다.
* cartoon = cv.bitwise_and(color, color, mask=edges)

## Results
* Good Results with original cartoon rendering tools
![Image](https://github.com/user-attachments/assets/bb2c2202-241b-47d9-8a37-12b1fec0a6ae)

* Good Results with k-mean cartoon rendering tools
![Image](https://github.com/user-attachments/assets/d8030a4d-b110-4b1d-8b6b-3fb174eeccf2)

* Bad Results with original cartoon rendering tools
![Image](https://github.com/user-attachments/assets/c3316c84-5718-4da9-a19e-2afd5e2f8f79)

* Bad Results with k-mean cartoon rendering tools
![Image](https://github.com/user-attachments/assets/4aab81de-3691-4cfa-a516-4a855ce1e4fc)

## Limitations for my algorithm

* 두 모델에서 테두리를 완전히 보존하면서도 노이즈를 적게 하는 방안은 찾지 못했다.
* 두 모델에서 작은 개체에 대해 테두리를 설정하는 과정에서 기존의 그림이 흐릿해지는 것에 대한 해결책을 제시하지 못했다.
* 원래 이미지가 흐릿한 경우 만화 그림체로 바꾸는 과정에서 기존의 그림이 상당 부분 손실되었다.
