#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/videoio.hpp"
#include <iostream>
#include <chrono>

/* Build instructions until I get around to a Makefile:
g++ -ggdb test_simple.cpp -o test_simple `pkg-config --cflags --libs opencv4`
.... and make sure you have OpenCV 4.2.0 installed on your system.
*/

using namespace cv;
using namespace std;
using namespace std::chrono;

int main(int argc, char* argv[])
{
    Mat image, hsv, thresh;
    int fc = 10000;
    image = imread("target1.jpg");
    auto start = high_resolution_clock::now();
    vector<vector<Point> > conts;
    vector<Vec4i> hier;
    for(int x = 0; x < fc; x++) {
        cvtColor(image, hsv, COLOR_BGR2HSV);
        // Detect the object based on HSV Range Values
        inRange(hsv, Scalar(46, 47, 126), Scalar(106, 255, 249), thresh);
        findContours(thresh, conts, hier, RETR_TREE, CHAIN_APPROX_SIMPLE);
    }
    auto finish = high_resolution_clock::now();
    duration<double> elapsed = finish - start;
    cout << "Time in seconds: " << elapsed.count() << " (" << fc << " loops)" << endl;
    return 0;
}
