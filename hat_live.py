import jetson.inference
import jetson.utils

net = jetson.inference.poseNet()
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("rtp://192.168.55.100:1234")

while True:
	img = camera.Capture()
	poses = net.Process(img)

	for pose in poses:
	    left_eye_idx = pose.FindKeypoint(net.FindKeypointID('left_eye'))
	    #left_eye_idx = pose.FindKeypoint(net.FindKeypointID('left_eye'))
	    right_eye_idx = pose.FindKeypoint(net.FindKeypointID('right_eye'))
	    #right_shoulder_idx = pose.FindKeypoint(net.FindKeypointID('right_shoulder'))

	    if left_eye_idx < 0 or right_eye_idx < 0:
                continue

	    left_eye = pose.Keypoints[left_eye_idx]
	    #left_shoulder = pose.Keypoints[left_shoulder_idx]
	    right_eye = pose.Keypoints[right_eye_idx]
	    #right_shoulder = pose.Keypoints[right_shoulder_idx]

	    length = abs(left_eye.x - right_eye.x)
	    point_x = left_eye.x - (length/2)
	    point_y = left_eye.y - length

	jetson.utils.cudaDrawCircle(img, (point_x, point_y), 10, (255, 0, 0, 200))
	jetson.utils.cudaDrawRect(img, (point_x-70, point_y,  point_x+100, point_y+10), (0, 0, 0))
	jetson.utils.cudaDrawRect(img, (point_x-50, point_y+10, point_x+80, point_y-200), (0, 0, 0))
	display.Render(img)
#	print(f"person {pose.ID} is pointing towards ({x}, {y})")

	if not display.IsStreaming():
	    break
