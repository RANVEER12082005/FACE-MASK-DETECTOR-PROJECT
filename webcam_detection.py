import streamlit as st
import cv2
import numpy as np
from model_utils import load_mask_model, predict_mask

def show():
    st.markdown("""
    <div style="padding: 2rem 0 1.5rem 0;">
        <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                    color: #00ff88; letter-spacing: 0.2em; text-transform: uppercase;
                    margin-bottom: 0.5rem;">Real-Time</div>
        <h1 style="font-family: 'Syne', sans-serif; font-size: 2.8rem; font-weight: 800;
                   color: #e8f0fe; margin: 0 0 0.5rem 0;">Live Webcam</h1>
        <p style="color: #6b7fa3; font-size: 1rem; margin: 0;">
            Real-time face mask detection using your camera. Green = mask, Red = no mask.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Status indicators
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(0,255,136,0.15);
                    border-radius: 10px; padding: 1rem; text-align: center;">
            <div style="font-size: 1.5rem; margin-bottom: 0.3rem;">🟢</div>
            <div style="font-size: 0.78rem; color: #6b7fa3; text-transform: uppercase;
                        letter-spacing: 0.1em; font-family: 'Syne', sans-serif; font-weight: 600;">
                Mask Detected</div>
            <div style="font-size: 0.75rem; color: #00ff88; margin-top: 0.2rem;">Green box</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(255,51,102,0.15);
                    border-radius: 10px; padding: 1rem; text-align: center;">
            <div style="font-size: 1.5rem; margin-bottom: 0.3rem;">🔴</div>
            <div style="font-size: 0.78rem; color: #6b7fa3; text-transform: uppercase;
                        letter-spacing: 0.1em; font-family: 'Syne', sans-serif; font-weight: 600;">
                No Mask</div>
            <div style="font-size: 0.75rem; color: #ff3366; margin-top: 0.2rem;">Red box</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background: #0d1321; border: 1px solid rgba(255,204,0,0.15);
                    border-radius: 10px; padding: 1rem; text-align: center;">
            <div style="font-size: 1.5rem; margin-bottom: 0.3rem;">📊</div>
            <div style="font-size: 0.78rem; color: #6b7fa3; text-transform: uppercase;
                        letter-spacing: 0.1em; font-family: 'Syne', sans-serif; font-weight: 600;">
                Confidence</div>
            <div style="font-size: 0.75rem; color: #ffcc00; margin-top: 0.2rem;">Shown on box</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.info("💡 Make sure your model is trained first. Allow camera access when your browser asks.")

    # Live stats placeholders
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    frames_count    = stat_col1.empty()
    masked_count    = stat_col2.empty()
    unmasked_count  = stat_col3.empty()
    conf_display    = stat_col4.empty()

    st.markdown("<br>", unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        start = st.button("▶️ Start Camera", type="primary", use_container_width=True)

    if start:
        stop_btn = st.button("⏹️ Stop Camera", use_container_width=False)

        try:
            model = load_mask_model()
        except Exception as e:
            st.error(f"❌ Could not load model: {e}\n\nMake sure you've run `python3 train_mask_detector.py` first.")
            return

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("❌ Cannot access webcam. Please check camera permissions in System Preferences → Privacy → Camera.")
            return

        frame_placeholder = st.empty()

        frame_num     = 0
        total_masked  = 0
        total_unmasked= 0
        last_conf     = 0.0

        while cap.isOpened() and not stop_btn:
            ret, frame = cap.read()
            if not ret:
                st.error("⚠️ Lost camera connection.")
                break

            frame_num += 1
            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            frame_masked   = 0
            frame_unmasked = 0

            for (x, y, w, h) in faces:
                face_img             = frame[y:y+h, x:x+w]
                label, confidence, color = predict_mask(face_img, model)
                last_conf = confidence

                # Draw styled bounding box
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
                bg = (0, 160, 70) if label == "Mask" else (160, 0, 50)
                cv2.rectangle(frame, (x, y-42), (x+w, y), bg, -1)
                cv2.putText(frame, f"{label}  {confidence:.1f}%",
                            (x+8, y-14), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (255, 255, 255), 2)

                if label == "Mask":
                    frame_masked += 1
                else:
                    frame_unmasked += 1

            total_masked   += frame_masked
            total_unmasked += frame_unmasked

            # Update live stats every 10 frames
            if frame_num % 10 == 0:
                frames_count.metric("Frames",    frame_num)
                masked_count.metric("Masked ✅",  total_masked)
                unmasked_count.metric("Unmasked ❌", total_unmasked)
                conf_display.metric("Last Conf", f"{last_conf:.1f}%")

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

        cap.release()
        st.success(f"✅ Session ended — {frame_num} frames processed, "
                   f"{total_masked} masked detections, {total_unmasked} unmasked detections.")