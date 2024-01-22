#!/usr/bin/env python3

import streamlit as st
import tensorflow as tf
import tensorflow_text as text


tf.get_logger().setLevel('ERROR')

model = tf.saved_model.load('./models')
text = ["happy happy happy "]
t = str(st.text_input('comments'))
if t.isalnum():
  score = tf.sigmoid(model(tf.constant(list(t))))
  st.write(score)

