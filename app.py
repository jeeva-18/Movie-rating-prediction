import streamlit as st
import tensorflow as tf

tf.get_logger().setLevel('ERROR')

st.header('Hello da')

model = tf.saved_model.load('./models')
