import roslib; roslib.load_manifest('tf')
import rospy
import rosbag
from tf.msg import tfMessage
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Transform, Vector3, Quaternion

def add_tf(inbag, outbag, frame_id = 'base_link', child_frame_id = 'livox_frame', transform = None):
    with rosbag.Bag(outbag, 'w') as outbag:
        if transform is None:
            transform = Transform()
            transform.translation = Vector3(0.0, 0.0, 0.0)
            transform.rotation = Quaternion(0.0, 0.0, 0.0, 1.0)
        for topic, msg, t in rosbag.Bag(inbag).read_messages():
            if topic == "/tf" and msg.transforms:
                outbag.write(topic, msg, t)
            else:
                tfm = TransformStamped()
                tfm.header.frame_id = frame_id
                tfm.child_frame_id = child_frame_id
                tfm.transform = transform
                tfm.header.stamp = rospy.Time.from_sec(t.to_sec())
                tfmsg = tfMessage([tfm])
                outbag.write("/tf", tfmsg, t)
                outbag.write(topic, msg, t)

if __name__ == '__main__':
    add_tf('/home/alfayoung/Workspace/Calibration/src/livox_camera_calib/input/0.bag', \
           '/home/alfayoung/Workspace/Calibration/src/livox_camera_calib/input/0_tf.bag')