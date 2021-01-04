# practice_deep_learning

1. 아나콘다 설치
2. 파이참 설치
3. 파이참 - 깃허브 연동
4. 아나콘다에 파이썬 3.7버전으로 가상환경 추가(conda create -n kjy python=3.7)
5. 파이참 - 아나콘다 연동(setting - python interpreter에 자신이 만든 가상환경 선택)
6. cuda 11.0.3_451.82 설치 (RTX 2080 super에서 사용하였음)
7. cudnnn-11.0 v8.0.5 설치 (사실상 cuda 11버전 지원하는 최근 cudnn 설치)
8. 가상환경 들어가서 conda install pip (이상하게 conda로 텐서플로우 설치할땐 2.3버전으로 설치되는데, 이 경우 gpu 인식이 안됨)
9. pip install tensorflow-gpu (텐서플로우 2.4버전 설치되며, numpy는 1.19.4로 자동설치되는데, 1.19.4때문에 텐서플로우 import가 안됨)
10. pip install numpy==1.19.3 (1.19.3으로 다운그레이드)
11. 텐서플로우가 gpu 인식하는지 확인해볼 것. 가상환경에 python 들어가서 from tensorflow.python.client import device_lib 입력 후 device_lib.list_local_devices() 입력해서 gpu가 뜨는지 확인
12. conda install opencv 로 opencv 설치
