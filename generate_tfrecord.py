"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import os
from collections import namedtuple

import pandas as pd
import tensorflow as tf
from PIL import Image
# from object_detection.utils import dataset_util
# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Utility functions for creating TFRecord data sets."""

import tensorflow as tf


def int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def int64_list_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


def bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def bytes_list_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))


def float_list_feature(value):
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def read_examples_list(path):
  """Read list of training or validation examples.

  The file is assumed to contain a single example per line where the first
  token in the line is an identifier that allows us to find the image and
  annotation xml for that example.

  For example, the line:
  xyz 3
  would allow us to find files xyz.jpg and xyz.xml (the 3 would be ignored).

  Args:
    path: absolute path to examples list file.

  Returns:
    list of example identifiers (strings).
  """
  with tf.gfile.GFile(path) as fid:
    lines = fid.readlines()
  return [line.strip().split(' ')[0] for line in lines]


def recursive_parse_xml_to_dict(xml):
  """Recursively parses XML contents to python dict.

  We assume that `object` tags are the only ones that can appear
  multiple times at the same level of a tree.

  Args:
    xml: xml tree obtained by parsing XML file contents using lxml.etree

  Returns:
    Python dictionary holding XML contents.
  """
  if not xml:
    return {xml.tag: xml.text}
  result = {}
  for child in xml:
    child_result = recursive_parse_xml_to_dict(child)
    if child.tag != 'object':
      result[child.tag] = child_result[child.tag]
    else:
      if child.tag not in result:
        result[child.tag] = []
      result[child.tag].append(child_result[child.tag])
  return {xml.tag: result}


def make_initializable_iterator(dataset):
  """Creates an iterator, and initializes tables.

  This is useful in cases where make_one_shot_iterator wouldn't work because
  the graph contains a hash table that needs to be initialized.

  Args:
    dataset: A `tf.data.Dataset` object.

  Returns:
    A `tf.data.Iterator`.
  """
  iterator = dataset.make_initializable_iterator()
  tf.add_to_collection(tf.GraphKeys.TABLE_INITIALIZERS, iterator.initializer)
  return iterator


def read_dataset(file_read_func, decode_func, input_files, config):
  """Reads a dataset, and handles repetition and shuffling.

  Args:
    file_read_func: Function to use in tf.data.Dataset.interleave, to read
      every individual file into a tf.data.Dataset.
    decode_func: Function to apply to all records.
    input_files: A list of file paths to read.
    config: A input_reader_builder.InputReader object.

  Returns:
    A tf.data.Dataset based on config.
  """
  # Shard, shuffle, and read files.
  filenames = tf.concat([tf.matching_files(pattern) for pattern in input_files],
                        0)
  filename_dataset = tf.data.Dataset.from_tensor_slices(filenames)
  if config.shuffle:
    filename_dataset = filename_dataset.shuffle(
        config.filenames_shuffle_buffer_size)
  filename_dataset = filename_dataset.repeat(config.num_epochs or None)

  records_dataset = filename_dataset.apply(
      tf.contrib.data.parallel_interleave(
          file_read_func, cycle_length=config.num_readers, sloppy=True))
  if config.shuffle:
    records_dataset.shuffle(config.shuffle_buffer_size)
  tensor_dataset = records_dataset.map(
      decode_func, num_parallel_calls=config.num_parallel_map_calls)
  return tensor_dataset.prefetch(config.prefetch_size)


flags = tf.app.flags
flags.DEFINE_string("csv_input", 'C:\\Users\sunwoo\PycharmProjects\\untitled2\data\\recycle_labels.csv', 'Path to csv')
flags.DEFINE_string("output_path", 'C:\\Users\sunwoo\PycharmProjects\\untitled2\data\\a.tfrecord', 'Path to output')
FLAGS = flags.FLAGS


# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'recycle':
        return 1
    else:
        None


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': int64_feature(height),
        'image/width': int64_feature(width),
        'image/filename': bytes_feature(filename),
        'image/source_id': bytes_feature(filename),
        'image/encoded': bytes_feature(encoded_jpg),
        'image/format': bytes_feature(image_format),
        'image/object/bbox/xmin': float_list_feature(xmins),
        'image/object/bbox/xmax': float_list_feature(xmaxs),
        'image/object/bbox/ymin': float_list_feature(ymins),
        'image/object/bbox/ymax': float_list_feature(ymaxs),
        'image/object/class/text': bytes_list_feature(classes_text),
        'image/object/class/label': int64_list_feature(classes),
    }))
    return tf_example


def main(_):

    writer = tf.python_io.TFRecordWriter(FLAGS.output_path) # FLAGS.output_path
    path = os.path.join(os.getcwd(), 'images')
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
