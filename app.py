#!/usr/bin/env python3

import streamlit as st
import tensorflow as tf
import tensorflow_text as text


tf.get_logger().setLevel('ERROR')

model = tf.saved_model.load('./models')
text = []
t = str(st.text_input('comments'))
text.append(t)
st.write(len(text))
st.write(text)
if text[0] != ""  :
  # text.pop(0)
  score = tf.sigmoid(model(tf.constant(text)))
  ratings = score[0][0].numpy()
  st.write("%.2f"%(ratings*5))

