# UrbanScribe

UrbanScribe is a system that collects, analyses and visualises human movement through a space, completing the data feedback loop to empirically measure the quality of a space and enable urban and architectural A/B testing through spatial analytics.

Essentially UrbanScribe consists of an [OpenCV](http://opencv.org/) traking system running on a laptop with a webcam or attached camera, and an [Arduino Yun](https://www.arduino.cc/en/Main/ArduinoBoardYun) running Linux and an Atmel microcontroller. The laptop recognises faces or pedestrians, sends their positions in the frame to the Arduino which then plots them using a servo arm on a piece of paper.

This project was hastily constructed for a proof-of-concept demonstration in a design class called Ubiquitous Cities at UNSW. The course focused on the meaning of the term 'Smart City' and the considerations when weighing up tech solutions for an urban space.

# Setting up

**Please note:** I am not sure of these requirements. If you require extra packages (just look what package Python references in it's errors) please file a pull request.

## Mac

```
brew install numpy opencv
```

## Ubuntu

There are a lot of packages that the facial and pedestrian recognition rely on.

```
sudo apt-get -y install build-essential git cmake pkg-config
sudo apt-get -y install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

sudo apt-get -y install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install libgtk2.0-dev
sudo apt-get -y install libatlas-base-dev gfortran
sudo apt-get -y install python2.7-dev python3-dev
sudo apt-get -y install python-opencv
```

## All platforms: Install pip depenencies

```
pip install -r requirements.txt
```

# Usage

Spin up the Flask server

```
python app.py
```

This will launch a server at [localhost:5000](http://localhost:5000)

To stop the server:
- Follow the 'Kill Server' link at [localhost:5000](http://localhost:5000)
- Visit the [localhost:5000/kill](http://localhost:5000/kill) url (get request to keep it simple)
- Run the `kill_server.sh` script

# Further reading
Some more notes on image recognition with OpenCV and Python.

- [realpython.com/blog/python/face-detection-in-python-using-a-webcam/](https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/)
- [realpython.com/blog/python/face-recognition-with-python/](https://realpython.com/blog/python/face-recognition-with-python/)
- [pyimagesearch.com/tag/pedestrian-detection/](http://www.pyimagesearch.com/tag/pedestrian-detection/)
- [pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/](http://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/)
- [pyimagesearch.com/2015/09/21/opencv-track-object-movement/](http://www.pyimagesearch.com/2015/09/21/opencv-track-object-movement/)
- [pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/](http://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/)

# Author
- [Jake Coppinger](http://www.jakecoppinger.com)

# License
This project is licensed under the GNU GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details.