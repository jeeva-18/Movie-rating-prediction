#!/usr/bin/env python3

import streamlit as st
import tensorflow as tf
import tensorflow_text as text


tf.get_logger().setLevel('ERROR')
def main():
    model = tf.saved_model.load('./models')
    text = st.text_input('Comments')
    if text != None:
        score = tf.sigmoid(model(tf.constant(list(text))))
        st.write(score)

if __name__ == '__main__':
    main()
