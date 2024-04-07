#!/usr/bin/env python3

import streamlit as st
import tensorflow as tf
import tensorflow_text as text


tf.get_logger().setLevel('ERROR')
st.set_page_config(layout="wide")
st.title("Integrated Review Analysis System using PHP, MySQL, and Streamlit with BERT NLP Model")

model = tf.saved_model.load('./models')
text = []
t = str(st.text_input('Comments/Review:'))
text.append(t)
# st.write(len(text))
# st.write(text)
if text[0] != ""  :
  # text.pop(0)
  score = tf.sigmoid(model(tf.constant(text)))
  ratings = score[0][0].numpy()
  st.write("Rating: %.2f"%(ratings*5))

