import streamlit as st
from PIL import Image
import numpy as np
import cv2
from model_utils import load_mask_model, predict_mask

def show():
    st.markdown("""
    <div style="padding: 2rem 0 1.5rem 0;">
        <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                    color: #00ff88; letter-spacing: 0.2em; text-transform: uppercase;
                    margin-bottom: 0.5rem;">Detection</div>
        <h1 style="font-family: 'Syne', sans-serif; font-size: 2.8rem; font-weight: 800;
                   color: #e8f0fe; margin: 0 0 0.5rem 0;">Upload Image</h1>
        <p style="color: #6b7fa3; font-size: 1rem; margin: 0;">
            Upload a photo and the AI will detect faces and classify mask usage instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drop your image here or click to browse",
        type=["jpg", "jpeg", "png"],
        help="Supports JPG and PNG images"
    )

    if uploaded_file is not None:
        image    = Image.open(uploaded_file).convert("RGB")
        img_array= np.array(image)
        img_bgr  = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("""
            <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                        color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                        margin-bottom: 0.8rem;">Original Image</div>
            """, unsafe_allow_html=True)
            st.image(image, use_column_width=True)

        with st.spinner("🔍 Analysing image..."):
            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
            gray  = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) == 0:
                with col2:
                    st.markdown("""
                    <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                                color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                                margin-bottom: 0.8rem;">Result</div>
                    """, unsafe_allow_html=True)
                    st.warning("⚠️ No face detected. Try a clearer photo with a visible face.")
                return

            model   = load_mask_model()
            results = []

            for (x, y, w, h) in faces:
                face_img            = img_bgr[y:y+h, x:x+w]
                label, confidence, color = predict_mask(face_img, model)
                results.append((label, confidence))

                cv2.rectangle(img_bgr, (x, y), (x+w, y+h), color, 3)
                bg_color = (0, 180, 80) if label == "Mask" else (180, 0, 60)
                cv2.rectangle(img_bgr, (x, y-40), (x+w, y), bg_color, -1)
                cv2.putText(img_bgr, f"{label}  {confidence:.1f}%",
                            (x+8, y-12), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (255,255,255), 2)

        result_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        with col2:
            st.markdown("""
            <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                        color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                        margin-bottom: 0.8rem;">Detection Result</div>
            """, unsafe_allow_html=True)
            st.image(result_img, use_column_width=True)

        # ── Result cards ───────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-family: 'Syne', sans-serif; font-size: 0.75rem; font-weight: 700;
                    color: #6b7fa3; letter-spacing: 0.15em; text-transform: uppercase;
                    margin-bottom: 1rem;">Detection Summary</div>
        """, unsafe_allow_html=True)

        res_cols = st.columns(len(results) if len(results) <= 4 else 4)
        for i, (label, confidence) in enumerate(results):
            with res_cols[i % 4]:
                if label == "Mask":
                    st.markdown(f"""
                    <div style="background: rgba(0,255,136,0.08);
                                border: 1px solid rgba(0,255,136,0.3);
                                border-radius: 12px; padding: 1.4rem; text-align: center;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">✅</div>
                        <div style="font-family: 'Syne', sans-serif; font-size: 1rem;
                                    font-weight: 700; color: #00ff88;">Mask Detected</div>
                        <div style="font-size: 1.8rem; font-weight: 700; color: #00ff88;
                                    font-family: 'Syne', sans-serif; margin: 0.3rem 0;">
                            {confidence:.1f}%
                        </div>
                        <div style="font-size: 0.78rem; color: #6b7fa3;">confidence</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background: rgba(255,51,102,0.08);
                                border: 1px solid rgba(255,51,102,0.3);
                                border-radius: 12px; padding: 1.4rem; text-align: center;">
                        <div style="font-size: 2rem; margin-bottom: 0.5rem;">❌</div>
                        <div style="font-family: 'Syne', sans-serif; font-size: 1rem;
                                    font-weight: 700; color: #ff3366;">No Mask</div>
                        <div style="font-size: 1.8rem; font-weight: 700; color: #ff3366;
                                    font-family: 'Syne', sans-serif; margin: 0.3rem 0;">
                            {confidence:.1f}%
                        </div>
                        <div style="font-size: 0.78rem; color: #6b7fa3;">confidence</div>
                    </div>
                    """, unsafe_allow_html=True)

        # ── Summary stats ──────────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        total     = len(results)
        masked    = sum(1 for l, _ in results if l == "Mask")
        unmasked  = total - masked
        avg_conf  = np.mean([c for _, c in results])

        s1, s2, s3, s4 = st.columns(4)
        s1.metric("Faces Detected", total)
        s2.metric("Wearing Mask",   masked)
        s3.metric("No Mask",        unmasked)
        s4.metric("Avg Confidence", f"{avg_conf:.1f}%")