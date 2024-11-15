import unittest
import numpy as np

import ros2_numpy as rnp
from sensor_msgs.msg import PointCloud2, PointField, Image

class TestPointClouds(unittest.TestCase):
    def makeArray(self, npoints):
        points_arr = np.zeros((npoints,), dtype=[
            ('x', np.float32),
            ('y', np.float32),
            ('z', np.float32),
            ('r', np.uint8),
            ('g', np.uint8),
            ('b', np.uint8)])
        points_arr['x'] = np.random.random((npoints,))
        points_arr['y'] = np.random.random((npoints,))
        points_arr['z'] = np.random.random((npoints,))
        points_arr['r'] = np.floor(np.random.random((npoints,))*255)
        points_arr['g'] = 0
        points_arr['b'] = 255

        return points_arr

    def test_convert_dtype(self):
        fields = [
            PointField(name='x', offset=0, count=1,
                       datatype=PointField.FLOAT32),
            PointField(name='y', offset=4, count=1,
                       datatype=PointField.FLOAT32)
        ]
        dtype = np.dtype([
            ('x', np.float32),
            ('y', np.float32)
        ])
        conv_fields = rnp.msgify(PointField, dtype, plural=True)
        self.assertSequenceEqual(fields, conv_fields,
                                 'dtype->Pointfield Failed with simple values')

        conv_dtype = rnp.numpify(fields, point_step=8)
        self.assertSequenceEqual(dtype, conv_dtype,
                                 'dtype->Pointfield Failed with simple values')

    def test_convert_dtype_inner(self):
        fields = [
            PointField(name='x', offset=0, count=1,
                       datatype=PointField.FLOAT32),
            PointField(name='y', offset=4, count=1,
                       datatype=PointField.FLOAT32),
            PointField(name='vectors', offset=8, count=3,
                       datatype=PointField.FLOAT32)
        ]

        dtype = np.dtype([
            ('x', np.float32),
            ('y', np.float32),
            ('vectors', np.float32, (3,))
        ])

        conv_fields = rnp.msgify(PointField, dtype, plural=True)
        self.assertSequenceEqual(fields, conv_fields,
                                 'dtype->Pointfield with inner dimensions')

        conv_dtype = rnp.numpify(fields, point_step=8)
        self.assertEqual(dtype, conv_dtype,
                         'Pointfield->dtype with inner dimensions')


    def test_roundtrip(self):

        points_arr = self.makeArray(100)
        cloud_msg = rnp.msgify(PointCloud2, points_arr)
        new_points_arr = rnp.numpify(cloud_msg)

        np.testing.assert_equal(points_arr, new_points_arr)

    def test_roundtrip_numpy(self):
        points_arr = self.makeArray(100)
        cloud_msg = rnp.msgify(PointCloud2, points_arr)
        new_points_arr = rnp.numpify(cloud_msg)

        np.testing.assert_equal(points_arr, new_points_arr)

    def test_roundtrip_zero_points(self):
        """Test to make sure zero point arrays don't raise memoryview.cast(*) errors"""
        points_arr = self.makeArray(0)
        cloud_msg = rnp.msgify(PointCloud2, points_arr)
        new_points_arr = rnp.numpify(cloud_msg)

        np.testing.assert_equal(points_arr, new_points_arr)

    def test_field_access(self):
        points_arr = self.makeArray(3)
        cloud_msg = rnp.msgify(PointCloud2, points_arr)
        points_xyz = rnp.point_cloud2.pointcloud2_to_array(cloud_msg, fields=['x', 'y', 'z'])

        np.testing.assert_equal(points_xyz, rnp.point_cloud2.pointcloud2_to_xyz_array(cloud_msg))


if __name__ == '__main__':
    unittest.main()
